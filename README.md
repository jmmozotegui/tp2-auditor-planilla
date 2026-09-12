# Auditor de planilla de producción

Agente que audita la planilla mensual de una planta contra trece reglas (R01 a R13) y devuelve un informe estructurado de hallazgos, con evidencia y acción sugerida para cada uno.

No es un chatbot ni un prompt suelto: es un contrato de prompts versionado, con una entrada definida, una salida con esquema, corridas registradas y un punto de supervisión humana antes de que un hallazgo se convierta en un reclamo.

**Los datos de este repositorio son sintéticos.** Misma estructura de columnas que la planilla real, valores inventados. El repositorio es público y no contiene información de producción de ninguna empresa.

---

## El problema

Una planilla de producción se carga turno a turno, a mano, por distintos supervisores. Antes de que los números lleguen a la reunión de producción alguien tiene que revisarla: horarios imposibles, campos obligatorios vacíos, paradas sin motivo, lotes que quedaron abiertos, diferencias de rendimiento entre operarios que no se explican.

Con 182 filas y trece reglas, lo primero que se pierde en una revisión visual son las **reglas agregadas** — repeticiones a lo largo de una semana, acumulados por día, comparaciones entre operarios. Exigen cruzar filas que están lejos unas de otras.

El agente no reemplaza el criterio: aplica las trece reglas completas todas las semanas, con la evidencia a la vista, y deja la decisión a una persona.

## El contrato

El agente son dos archivos. El modelo es solamente el motor que los ejecuta.

| Archivo | Qué define |
|---|---|
| `prompts/system_prompt.md` | Rol, contexto de la planta, las trece reglas con sus umbrales, restricciones y formato de salida |
| `prompts/user_prompt.md` | La tarea de cada corrida: cómo determinar la fecha de corte y qué entregar |
| `reglas.md` | Las trece reglas en tabla, para lectura humana |

Las seis piezas exigidas están en el contrato: **rol**, **contexto**, **tarea**, **restricciones**, **formato** y **ejemplos**.

**Ninguna regla de auditoría vive en código.** Es la decisión estructural del trabajo y está explicada en `DECISIONES.md`. El único Python del repositorio es `experimento/verificacion_r11.py`, que hace lo contrario de un motor: controla al agente desde afuera.

### Las trece reglas

Se listan catorce filas porque **R08 se evalúa en dos variantes**, `R08a` y `R08b`.

| | Qué detecta | Severidad | Alcance |
|---|---|---|---|
| R01 | Horarios imposibles | Alta | Fila |
| R02 | Tiempos que no cierran contra el total | Alta | Fila |
| R03 | Parada sin motivo cargado | Media | Fila |
| R04 | Campo obligatorio vacío | Alta | Fila |
| R05 | Producción cero con tiempo productivo | Media | Fila |
| R06 | OEE bajo el umbral | Media | Métrica |
| R07 | Cumplimiento de meta bajo el umbral | Media | Métrica |
| R08a | Tres paradas no planificadas en el mismo día y línea | Media | Agregado |
| R08b | Parada acumulada del día sobre el umbral | Media | Agregado |
| R09 | Motivo de parada que se repite en la semana | Alta | Agregado |
| R10 | Calidad bajo el umbral, con proyección | Media | Métrica |
| R11 | Diferencia de OEE entre operarios | Baja | Agregado |
| R12 | Lote abierto más de lo tolerado | Media | Fila |
| R13 | Motivo fuera del catálogo | Baja | Fila |

## La herramienta

La entrada es un archivo real: `planilla_produccion_mes.csv`, la exportación de la planilla del mes. El agente la lee entera, incluidas las líneas, operarios o productos que el contrato no menciona en su contexto.

La ejecución es una **tarea programada**: corre sola los lunes a la mañana, toma la última versión de la planilla y escribe el informe. No hay un paso manual en el medio. Una corrida no supervisada detectó filas cargadas en el ínterin, incluidas dos con motivos de parada fuera del catálogo, que R13 reportó correctamente.

## La salida

JSON con esquema fijo, más una tabla markdown legible.

Cada hallazgo trae **identificador determinístico**, regla, severidad, alcance, fecha, turno, línea, operario, descripción, evidencia con los valores concretos, y acción sugerida.

El identificador es lo que hace comparables dos corridas: `R12-EXT-01-2026-08-03-Tarde` significa lo mismo en cualquier ejecución. Comparar dos corridas es una diferencia de conjuntos, no una lectura.

El informe incluye además `reglas_no_evaluables`: el contrato obliga a distinguir **"no encontré"** de **"no pude evaluar"**, y a declarar el motivo. El agente no completa por inferencia.

## Supervisión

**Nivel L2.** El agente ejecuta el ciclo completo sin intervención, pero su salida no dispara ninguna acción hasta que una persona la revisa.

Revisa el Responsable de Planeamiento y Control de Producción, los lunes antes de la reunión: los hallazgos de severidad Alta uno por uno, los Media y Baja por muestreo, y el bloque de reglas no evaluables completo. Firma el mismo responsable al aprobar el informe para circulación. Sin firma, el informe no se distribuye.

No es L3 por una razón concreta: está probado que el agente puede equivocarse. El detalle está en `GOBIERNO_Y_RIESGO.md`.

## Las corridas

| Corrida | Contrato | Corte | Filas | Hallazgos |
|---|---|---|---:|---:|
| `corridas/run_1.md` | v1 | 2026-08-19 | 117 | 41 |
| `corridas/run_2.md` | v2 | 2026-08-30 | 182 | 87 |
| `corridas/run_3.md` | v2 | 2026-08-30 | 182 | 87 |
| `corridas/run_v3_A.md` | **v3** | 2026-08-30 | 182 | **84** |
| `corridas/run_v3_B.md` | **v3** | 2026-08-30 | 182 | **84** |

Cada corrida declara su fecha, la fecha de corte que usó, cuántas filas analizó y cuántas ignoró.

`run_2` y `run_3` son dos ejecuciones del contrato v2 sobre la misma entrada. Dan el mismo total, 87, y **difieren en seis identificadores**: el contrato v2 no era repetible, y el total coincidente lo disimulaba. `run_v3_A` y `run_v3_B` son la misma prueba sobre el contrato final: 84 identificadores idénticos, diferencia simétrica cero.

**`run_2.md` contiene tres hallazgos que no corresponden.** Se descubrió construyendo el oráculo de R11 y está documentado en `EXPERIMENTO.md`. La corrida se conserva sin editar: corregirla a mano la convertiría en algo que el contrato no produce.

`run_3.md` es una re-ejecución del 2026-09-12. Reemplaza a un archivo que la Entrega 2 presentaba como corrida independiente y que resultó ser una copia de `run_2`. El detalle está en `DECISIONES.md`.

## Las tres iteraciones

| | Pieza tocada | Causa | Efecto medido |
|---|---|---|---|
| 1 | Tarea | La fecha de corte estaba clavada y el agente ignoraba 63 filas | Corte dinámico: de 117 filas auditadas a 182 |
| 2 | Restricciones · R11 | La regla no decía cómo promediar ni a quién excluir | Ninguno sobre esta planilla — resultado negativo, documentado |
| 3 | Restricciones · R12 | El borde de "más de 5 días hábiles" admitía dos lecturas | Dos corridas con diferencia simétrica cero |

Ninguna falla fue fabricada. Salieron de correr el contrato. La historia completa está en `DECISIONES.md`.

## El experimento

La devolución de la Entrega 2 pedía mostrar qué hallazgos aparecían con la nueva R11. Al responderlo apareció que la comparación publicada tenía **la variable confundida**: entre `run_1` y `run_2` habían cambiado el contrato y el tamaño de la entrada a la vez.

Se rehizo fijando todo salvo el contrato. Los resultados, en `EXPERIMENTO.md`:

- La nueva R11 **no cambió ningún hallazgo**. Resultado negativo, informado tal cual.
- Las diferencias estaban en R12, una regla que no se había tocado — o sea, variabilidad entre corridas, no efecto del contrato.
- Un oráculo determinístico reveló que `run_2` tenía tres falsos positivos.
- El contrato v3 produce **la misma salida en Claude Haiku 4.5, Sonnet 5 y Opus 5**: 84 identificadores idénticos en los tres motores.

Esa última medición es la que justifica la elección de modelo: si el más chico devuelve exactamente lo mismo, corresponde el más chico.

## Economía

Corre dentro de un plan de equipo, así que **el costo marginal por corrida es cero**. Lo que consume es cupo del plan: ≈33.000 tokens por corrida, ≈1,7 millones al año con frecuencia semanal.

Como escenario de productización —corriendo contra la API en lugar del plan— serían **USD 0,1146 por corrida y USD 5,96 al año** con Haiku 4.5. Cifras estimadas y declaradas como tales, no facturadas. El detalle en `ANALISIS_ECONOMICO.md`.

## Qué queda abierto

Se declara en vez de omitirse:

- La inestabilidad de R11 entre corridas no está resuelta.
- La resistencia a instrucción inyectada en los datos no fue probada.
- El informe no registra con qué modelo corrió.
- El oráculo cubre solo R11.
- Falta definir el borde de la semana calendario para cortes en fin de semana.
- El bloque `reglas_no_evaluables` no tiene granularidad definida: distintas corridas declaran 2, 3 o 4 entradas para las mismas dos situaciones.
- El `.xlsx` quedó dos filas atrás del CSV y no se regeneró.

## Estructura

```
README.md                      este archivo
DECISIONES.md                  iteraciones, fallas y decisiones de alcance
EXPERIMENTO.md                 el experimento y sus resultados
ANALISIS_ECONOMICO.md          consumo, escenario productizado y elección de modelo
GOBIERNO_Y_RIESGO.md           permisos, supervisión, riesgos y contingencias
reglas.md                      las trece reglas en tabla

prompts/
   system_prompt.md            contrato vigente (v3)
   user_prompt.md              la tarea de cada corrida
   system_prompt_v1.md         versiones anteriores, para reconstruir
   system_prompt_v2.md           la evolución del contrato
   user_prompt_v1.md
   user_prompt_v2.md

corridas/                      las cinco corridas, con fecha, corte y filas

experimento/
   run_v1_corte3008.md         v1 sobre la entrada de 182 filas
   run_v3_sonnet.md            v3 sobre Claude Sonnet 5
   run_v3_haiku.md             v3 sobre Claude Haiku 4.5
   ids_*.txt                   identificadores de cada corrida
   verificacion_r11.py         oráculo determinístico de R11

planilla_produccion_mes.csv    la entrada
Planilla_Produccion.xlsx       instantánea anterior de la planilla (180 filas);
                               la entrada vigente de las corridas es el CSV (182 filas)
```

## Reproducir una corrida

1. Abrir una sesión nueva con un modelo que pueda leer archivos.
2. Cargar `prompts/system_prompt.md` como system prompt.
3. Enviar `prompts/user_prompt.md` seguido del contenido de `planilla_produccion_mes.csv`.
4. La salida debe ser el JSON del contrato más la tabla, sin texto adicional.

Verificar antes de darla por buena:

```bash
python3 experimento/verificacion_r11.py planilla_produccion_mes.csv
```

Si los hallazgos de R11 de la corrida no coinciden con los del oráculo, la corrida no es confiable.
