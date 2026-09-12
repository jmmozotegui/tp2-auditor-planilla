# Decisiones

Cómo se llegó hasta acá: qué se intentó, qué falló, qué se recortó y por qué.

## El problema

Una planilla de producción se carga turno a turno, a mano, por distintos supervisores. Al cierre del mes alguien tiene que revisarla antes de que los números lleguen a la reunión de producción: horarios imposibles, campos vacíos, paradas sin motivo, lotes que quedaron abiertos, diferencias de rendimiento entre operarios que no se explican.

Esa revisión se hacía leyendo. Con 182 filas y trece reglas, lo que primero se pierde son las reglas agregadas —repeticiones a lo largo de una semana, acumulados por día, comparaciones entre operarios—, porque exigen cruzar filas que están lejos unas de otras.

El objetivo no fue automatizar el juicio, sino la lectura exhaustiva: que las trece reglas se apliquen completas todas las veces, con la evidencia a la vista, y que un humano decida qué hacer con los hallazgos.

## Decisión de alcance 0 — datos sintéticos

**El repositorio es público.** La planilla, los legajos, las líneas y los lotes son inventados: misma estructura de columnas que la real, valores fabricados.

Cuesta algo en fidelidad y se asume a conciencia. La alternativa era publicar datos de producción de una empresa en un repositorio abierto para aprobar una materia, que no es una decisión defendible. La estructura es la que importa: el contrato se aplica igual sobre la planilla real.

## Iteración 0 — el desvío por un framework

**Qué se intentó.** El primer intento de construir el agente fue pedírselo a un asistente de código, desde cero, describiendo la necesidad: un agente que auditara una planilla genérica.

**Qué devolvió.** Una propuesta de framework de agentes, y dentro de ella **un motor de reglas determinístico en pandas que resolvía 8 de las 12 reglas en código Python**. El agente quedaba para las cuatro restantes.

**Por qué se descartó.** La propuesta funcionaba. Ése no era el problema. El problema es que si una regla vive en código, el contrato deja de gobernarla: no se puede iterar sobre la redacción, no se puede comparar una versión contra otra, y la pregunta "¿qué cambió cuando cambié la regla?" pierde sentido porque la regla no está en ningún texto que se pueda versionar.

Todo el valor de este trabajo —el experimento de la iteración 3, la comparación entre modelos, el oráculo— depende de que las reglas estén escritas en un documento y no compiladas en una función.

**Decisión.** Ninguna regla de auditoría vive en código. Las trece están en `reglas.md` y en el system prompt. El único Python del repositorio es `experimento/verificacion_r11.py`, y es deliberadamente **lo contrario** de un motor: un oráculo externo que sirve para controlar al agente, no para reemplazarlo.

## Iteración 1 — la fecha de corte estaba clavada

**Qué falló.** La primera versión del user prompt decía:

> *"Fecha de corte: 2026-08-19. Analizá únicamente las filas con `Fecha` menor o igual a esa fecha."*

Con la planilla completa del mes, el agente auditó 117 filas e **ignoró 63** — las del 20 al 28 de agosto. Correctamente, porque eso era lo que el contrato pedía. El informe lo declaró: *"Filas ignoradas por corte: 63"*.

El defecto no era del agente: era que el contrato estaba escrito para una planilla puntual y no para la tarea recurrente. Cada lunes habría que editar la fecha a mano, y un agente que necesita que alguien lo edite todas las semanas no está automatizando nada.

**Pieza tocada:** la tarea, en el user prompt.

**Cambio.** La fecha de corte pasó de ser un valor fijo a una instrucción: *"la fecha más reciente que aparezca en la columna `Fecha`"*, más la obligación de declarar en el informe qué fecha usó y cuántas filas analizó.

Se agregó también que la planilla puede traer líneas, operarios o productos que el contrato no menciona en su contexto, y que hay que auditarlos igual: el contexto describe la planta, no limita qué filas se revisan.

**Resultado.** La corrida siguiente tomó el corte 2026-08-30 sola, analizó 182 filas y 0 ignoradas. El contrato dejó de depender de una edición semanal.

## Iteración 2 — R11 admitía dos lecturas

**Qué falló.** R11 decía:

> *"Diferencia de `OEE_pct` mayor a 10 puntos entre operarios distintos en la misma `Maquina_Linea` y el mismo `Turno`."*

No decía **cómo** se calcula el OEE de un operario cuando tiene varios turnos, ni si un operario con un solo turno registrado entra a la comparación. Un operario que trabajó una vez y tuvo un mal día aparecía comparado contra el promedio de otro que trabajó seis veces.

**Pieza tocada:** las restricciones, en el system prompt. Una sola regla.

**Cambio.** Se agregó que el OEE de un operario en esa combinación es el **promedio simple de sus filas**, que solo entran los operarios con **2 o más turnos registrados**, y que si después de ese filtro no queda un par comparable la combinación no genera hallazgo. Se fijó además el patrón de identificador `R11-{LINEA}-{TURNO}`.

**Resultado, y acá hay que ser honesto.** En su momento se dio por buena porque las corridas siguientes fueron estables entre sí. Recién al hacer el experimento de la iteración 3 —comparando v1 y v2 sobre la misma entrada— se comprobó que **la reescritura no cambió ningún hallazgo**: los nueve identificadores de R11 de v1 y de v2 son idénticos.

La iteración 2 aclaró la regla para un lector humano. No modificó el comportamiento observable. Está documentado como resultado negativo en `EXPERIMENTO.md`.

## Iteración 3 — el borde de R12

**Qué falló.** Al comparar v1 contra v2 sobre la misma planilla aparecieron tres hallazgos de diferencia. No eran de R11 —la regla que se había cambiado— sino de **R12**, cuyo texto era idéntico en ambas versiones.

Los tres son lotes abiertos del viernes 2026-08-21. Entre esa fecha y el corte del 2026-08-30 hay exactamente cinco días hábiles. R12 pedía *"más de 5 días hábiles"*, así que no correspondía reportarlos. Pero el texto no aclaraba si el día de la fila contaba ni si el corte se incluía, y las dos lecturas eran defendibles.

**Pieza tocada:** las restricciones, en el system prompt. Una sola regla, R12.

**Cambio.** Umbral expresado como número —**6 o más días hábiles**—, definición de qué días entran al conteo, y el caso de borde resuelto como ejemplo dentro de la propia regla.

**Resultado medido.** Dos corridas independientes del contrato v3, en sesiones aisladas: 84 hallazgos cada una, **diferencia simétrica cero**. Los 31 hallazgos de R12 se reproducen idénticos.

## El hallazgo que no esperábamos

El experimento destapó algo más serio que las tres reglas que se venían corrigiendo.

Se construyó un **oráculo independiente** —`experimento/verificacion_r11.py`, un cálculo determinístico en Python, sin modelo— para poder decidir si una corrida acertó sin depender de otra corrida. El oráculo devuelve **6 hallazgos** de R11.

Contrastadas contra él:

| Corrida | R11 reportados | ¿Correcto? |
|---|---:|---|
| `run_v1_corte3008` | 9 | no |
| **`run_2.md`, publicada en la Entrega 2** | **9** | **no** |
| Re-ejecución de v2 (`run_3`, 2026-09-12) | 6 | sí |
| `run_v3_A`, `run_v3_B` | 6 | sí |

**La corrida `run_2.md` que forma parte de la Entrega 2 reporta tres hallazgos que no existen.** Sus diferencias reales de OEE son 9,63 · 6,97 y 8,43 — las tres por debajo del umbral de 10.

Y el mismo contrato v2 dio 9 en una corrida y 6 en otra, sin que cambiara una palabra. Eso reubica el problema: **no era la redacción, era la repetibilidad**. Una regla agregada con umbral admite resultados distintos entre corridas cuando el conteo se hace leyendo en vez de calculando.

Se deja documentado en vez de corregir la corrida vieja. Editar a mano una salida del agente la convertiría en algo que el contrato no produce, y la evidencia dejaría de ser evidencia.

## La corrida que no era una corrida

Al auditar el repositorio antes de entregar apareció algo que no esperábamos.

`run_3.md` se presentaba en la Entrega 2 como la segunda ejecución de una prueba de repetibilidad: dos corridas del mismo contrato sobre la misma planilla, 87 identificadores idénticos, diferencia simétrica cero. Fue lo que la devolución destacó.

El archivo era **byte a byte idéntico a `run_2.md` salvo la hora**. Mismo tamaño, 73.630 bytes, y `diff` devuelve una sola línea distinta. Las 87 descripciones, evidencias y acciones —texto libre generado por el modelo— coincidían palabra por palabra.

Dos ejecuciones independientes no producen eso. La comparación que sí lo es, `run_v3_A` contra `run_v3_B`, tiene los mismos 84 identificadores pero difiere en más de mil líneas de prosa. Así se ve la repetibilidad de verdad.

**Decisión.** Se reemplazó `run_3.md` por una re-ejecución real de v2, hecha el 2026-09-12 en sesión aislada, con el mismo contrato, la misma planilla y la misma fecha de corte.

**Y el resultado desmiente lo que se había afirmado.** La corrida nueva da 87 hallazgos —el mismo total— pero **seis identificadores distintos**: tres de R11 que estaban en `run_2` no aparecen, y tres de R12 que no estaban sí aparecen. El contrato v2 nunca fue repetible; el total coincidente lo hacía parecer.

Eso convirtió un problema en el hallazgo más útil del trabajo, y está desarrollado en `EXPERIMENTO.md`: **comparar totales oculta lo que comparar conjuntos revela.** Es el argumento entero a favor de los identificadores determinísticos, y apareció al intentar desarmar una afirmación propia que no se sostenía.

No se corrigió en silencio ni se borró el rastro. La afirmación vieja era incorrecta y se dice por qué.

## Decisión de alcance 1 — no se fabrican fallas

En algún momento se consideró plantar defectos en el contrato para después corregirlos y tener una historia de iteraciones prolija. Se descartó.

El trabajo no es demostrar que se sabe romper y arreglar algo a voluntad: es que el contrato mejore por causas reales, encontradas corriéndolo. Las tres iteraciones documentadas salieron de eso — una de una planilla que no coincidía con el corte fijo, otra de una ambigüedad al releer la regla, la tercera de una comparación que reveló un borde mal definido. El falso positivo de `run_2` apareció solo, en una corrida automática que nadie estaba mirando.

## Decisión de alcance 2 — no hay interfaz

Se evaluó agregar un tablero que mostrara los hallazgos. Se descartó.

Lo que se entrega es un sistema agéntico, no una aplicación. Un tablero no agrega contrato, ni herramienta, ni reproducibilidad, ni supervisión; agrega archivos que un evaluador tiene que decidir si son parte del sistema o ruido. El esfuerzo fue a las dimensiones que estaban vacías —análisis económico y gobierno— en vez de a la presentación.

## Decisión de alcance 3 — supervisión L2, no L3

El agente corre solo y produce el informe, pero **ninguna acción se dispara hasta que una persona lo revisa**.

La razón no es cautela genérica: es que está probado que puede equivocarse. `run_2` reportó tres hallazgos inexistentes. Con L2 ese error se detiene en el escritorio del revisor; con L3 habría llegado como reclamo a un supervisor de turno. El detalle está en `GOBIERNO_Y_RIESGO.md`.

## Una falla operativa que también costó

Se intentó dejar la corrida agendada de modo que tomara la planilla directamente de una carpeta de la computadora. La tarea se creó, se ejecutó a horario y **terminó sin producir nada**: el entorno donde corría no tenía acceso a los archivos locales.

**Decisión.** La planilla se publica en un espacio al que la tarea programada sí llega, y el agendamiento se apoya solo en eso. La corrida del 2026-09-07 funcionó de esa forma, sin intervención, y encontró filas nuevas que se habían cargado en el medio — incluidas dos con motivos de parada fuera del catálogo, que R13 reportó correctamente.

Esa misma corrida encontró además un hueco del propio contrato: la fecha de corte cayó domingo, y el contrato define la semana de lunes a viernes, así que *"la semana en curso"* no estaba definida para un corte de fin de semana. El agente lo declaró `NO_EVALUABLE` en vez de inventar un criterio. **Queda como pendiente documentado**, sin corregir, porque llegó después del congelamiento de esta versión.

## Qué quedó afuera, dicho de frente

- **La inestabilidad de R11 entre corridas no está resuelta.** R12 quedó blindada con un borde explícito; R11 no se arregla redactando mejor, porque la redacción ya era correcta. La dirección sería exigir que el contrato muestre el cálculo intermedio antes de decidir. No se implementó.
- **La resistencia a instrucción inyectada no fue probada.** La columna `Observaciones` es texto libre; el contrato dice que la planilla es dato y no instrucción, pero nadie lo puso a prueba.
- **El informe no registra con qué modelo corrió.** La portabilidad está medida —tres modelos, misma salida— pero una corrida suelta no dice cuál la produjo.
- **El oráculo cubre solo R11.** R08a, R08b y R09 no tienen verificación independiente.
- **El borde de la semana calendario para cortes en fin de semana.**
