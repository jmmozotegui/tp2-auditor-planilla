# Gobierno y riesgo

## Qué toca el agente y con qué permisos

El agente es un contrato de prompts. No es un servicio con credenciales propias: corre dentro de una sesión que alguien abre, y hereda los permisos de esa sesión. El alcance concreto es chico y conviene decirlo con precisión.

| Sistema | Acceso | Permiso concreto | Por qué ese y no más |
|---|---|---|---|
| Planilla de producción (`planilla_produccion_mes.csv`) | Lectura | Solo lectura del archivo del período | El agente audita, no corrige. Si pudiera escribir, un error suyo alteraría el dato que la planta usa para decidir |
| Carpeta de informes | Escritura | Crear archivos nuevos en `corridas/` | Nunca sobrescribe: cada corrida es un archivo con fecha propia. Una corrida no puede borrar la evidencia de otra |
| Repositorio del contrato | Lectura | Lectura de `prompts/` y `reglas.md` | El agente lee las reglas que lo gobiernan; no puede modificarlas |
| Modelo (API) | Invocación | Una llamada por corrida | Sin herramientas de red ni de ejecución habilitadas: el agente no navega, no manda correos, no consulta sistemas de la planta |

**Mínimo privilegio, en una frase:** el agente puede leer la planilla y escribir un informe nuevo. No puede modificar datos de producción, no puede tocar su propio contrato, y no puede alcanzar ningún otro sistema de la empresa.

Lo que **no** toca, y es deliberado: ERP, sistema de calidad, legajos de personal, correo. Los hallazgos nombran operarios por legajo (`OP-104`) porque así viene la planilla, pero el agente no accede a ninguna base que traduzca ese legajo a una persona.

## Nivel de supervisión

**L2 — el agente ejecuta solo, un humano revisa antes de que nada se accione.**

En la escala del curso, los niveles que importan acá:

- **L0**: una persona hace todo, el agente sugiere.
- **L1**: el agente propone, la persona ejecuta cada paso.
- **L2**: el agente ejecuta el ciclo completo sin intervención, pero **su salida no dispara ninguna acción hasta que una persona la revisa**. ← *este sistema*
- **L3**: el agente ejecuta y acciona, la persona audita después por muestreo.
- **L4**: el agente ejecuta y acciona sin revisión.

Por qué L2 y no L3: los hallazgos del auditor derivan en reclamos a supervisores de turno y en pedidos de recarga de datos. Un falso positivo que llegue directo al supervisor tiene costo de credibilidad, y ya sabemos que puede pasar — la corrida `run_2` de la Entrega 2 reportó tres hallazgos de R11 que no existían. Con L2, ese error se detiene en el escritorio del revisor. Con L3, habría llegado a la planta.

### Quién revisa, cuándo y quién firma

| | |
|---|---|
| **Ejecuta** | El agente, automáticamente, lunes a las 08:00 |
| **Revisa** | Responsable de Planeamiento y Control de Producción, lunes por la mañana, antes de la reunión |
| **Qué revisa** | Los hallazgos de severidad Alta uno por uno; los Media y Baja por muestreo; y el bloque `reglas_no_evaluables` completo |
| **Firma** | El mismo Responsable de Planeamiento y Control de Producción, al aprobar el informe para circulación |
| **Sin firma** | El informe no se distribuye ni se convierte en pedido a ningún supervisor |

Los roles están nombrados de forma genérica porque el caso trabaja sobre datos sintéticos. La estructura de aprobación es la real.

## Qué puede salir mal

Cada riesgo con su control. Se ordenan por consecuencia, no por probabilidad.

### 1 · Falso positivo en una regla agregada

**Qué pasa.** El agente reporta un hallazgo que no corresponde. Está documentado: `run_2` reportó `R11-EXT-01-Mañana`, `R11-EXT-01-Tarde` y `R11-TRZ-01-Mañana`, cuyas diferencias reales de OEE son 9,63 · 6,97 · 8,43 — las tres por debajo del umbral de 10.

**Por qué importa.** Un reclamo infundado a un supervisor cuesta credibilidad, y la credibilidad del auditor es todo lo que tiene.

**Controles.**
- `experimento/verificacion_r11.py` recalcula R11 de forma determinística, sin modelo. Contrastar toda corrida contra el oráculo antes de darla por buena.
- Revisión humana de los hallazgos Alta, uno por uno (L2).
- Cada hallazgo trae su evidencia con los valores concretos, así que el revisor puede verificar sin abrir la planilla.

### 2 · Falso negativo — la auditoría pasa por alto algo real

**Qué pasa.** Una fila con problema no se reporta. Es más difícil de detectar que un falso positivo, porque nadie reclama por lo que no apareció.

**Controles.**
- El contrato obliga a declarar `reglas_no_evaluables` cuando faltan datos, en vez de callar. En la corrida de referencia son 2 a 4 entradas por corrida, y el revisor las lee todas.
- El informe declara filas analizadas e ignoradas por corte: si el número no cierra con la planilla, algo se recortó.

### 3 · Instrucción inyectada en los datos

**Qué pasa.** La columna `Observaciones` es texto libre que carga un supervisor. Alguien podría escribir ahí una instrucción dirigida al auditor —*"ignorá las reglas anteriores"*— y el agente la lee como parte de la planilla.

**Controles.**
- El contrato establece que el contenido de la planilla es **dato, nunca instrucción**.
- El formato de salida es cerrado: el informe solo admite hallazgos con identificador, regla, evidencia y acción. No hay campo donde una instrucción externa pueda expresarse.
- Pendiente declarado: **este riesgo no fue probado**. La prueba que corresponde es cargar una fila con una instrucción en `Observaciones` y verificar que el agente la reporte en vez de obedecerla.

### 4 · Datos faltantes que rompen una regla

**Qué pasa.** Una fila sin `OEE_pct` o sin `Operario` deja una regla sin base de cálculo.

**Controles.** Está resuelto y probado: el contrato distingue *"no encontré"* de *"no pude evaluar"*. Las corridas registran `reglas_no_evaluables` con el motivo textual —por ejemplo, que la fila del 2026-08-04 Tarde TRZ-01 no tiene `Tiempo_Total_min`, así que R02 no se puede calcular ahí. El agente **no completa por inferencia**.

### 5 · Ambigüedad en un borde de una regla

**Qué pasa.** Dos lecturas defendibles de la misma regla dan resultados distintos. Pasó con R12: *"más de 5 días hábiles"* no aclaraba si contaba el día de la fila ni si el corte se incluía, y los lotes del 21/08 aparecían en una corrida y no en otra.

**Controles.** La iteración 3 reescribió R12 con el umbral en número, el conteo definido y el caso de borde resuelto como ejemplo. Dos corridas posteriores dieron diferencia simétrica cero. El control general: **todo borde que produzca discrepancia entre corridas se escribe en el contrato con un ejemplo, no se deja al criterio del modelo**.

### 6 · Cambio de modelo por disponibilidad

**Qué pasa.** La corrida del lunes se ejecuta en un modelo distinto al previsto y el resultado cambia.

**Controles.** Medido: el mismo contrato produjo los 84 hallazgos idénticos en Haiku 4.5, Sonnet 5 y Opus 5. La portabilidad no es una expectativa, es una medición. Aun así, el informe debería registrar con qué modelo corrió — **hoy no lo hace**, y queda como mejora pendiente.

### 7 · Exposición de datos de producción

**Qué pasa.** La planilla sale del perímetro de la empresa al enviarse al modelo.

**Controles.**
- El repositorio publicado usa **datos sintéticos**: misma estructura de columnas, valores inventados. Ningún dato real de planta está expuesto.
- La planilla no contiene nombres de personas: los operarios figuran por legajo.
- Para un uso con datos reales, la decisión de qué proveedor y bajo qué acuerdo de tratamiento de datos es previa y ajena a este contrato. Queda explícitamente fuera del alcance de este trabajo.

## Contingencias

Qué hacer cuando algo falla, con el criterio de cuándo detenerse.

| Situación | Acción | ¿Se detiene? |
|---|---|---|
| La corrida automática no se ejecutó el lunes | Ejecutar a mano con el mismo contrato y la misma planilla. La corrida manual es equivalente: el contrato no depende del agendamiento | No |
| La salida no es JSON válido o las sumas no cierran | Descartar la corrida completa y repetirla en sesión nueva. **No se corrige a mano una salida del agente**: un informe editado deja de ser evidencia de lo que el contrato produce | Sí, hasta repetir |
| Los hallazgos de R11 no coinciden con el oráculo | Se informa el resultado del oráculo y se marca la corrida como no confiable. Se investiga antes de la corrida siguiente | Sí |
| La planilla llegó incompleta o con el mes anterior | El agente declara la fecha de corte que usó y cuántas filas analizó. Si no corresponde al período, se descarta y se pide la planilla correcta | Sí |
| Discrepancia entre dos corridas del mismo período | Prevalece la que coincide con el oráculo. Si ninguna coincide, no se emite informe y se revisa el contrato | Sí |
| Un supervisor discute un hallazgo | El informe trae la evidencia con los valores concretos. Se verifica contra la planilla. Si el hallazgo era incorrecto, se documenta como falla y se evalúa si la regla necesita precisión | No |

**Regla de oro:** ante duda sobre la validez de una corrida, no se emite el informe. Un informe tarde cuesta una reunión; un informe equivocado cuesta la confianza en el sistema.

## Lo que queda abierto

Se declara en vez de omitirse:

- **La resistencia a instrucción inyectada no fue probada.** Es la prueba más barata que falta.
- **El informe no registra el modelo, su versión ni la temperatura.** Sin eso, una corrida no es del todo reconstruible, aunque la portabilidad esté medida.
- **El oráculo cubre solo R11.** Las otras reglas agregadas —R08a, R08b, R09— no tienen verificación independiente.
