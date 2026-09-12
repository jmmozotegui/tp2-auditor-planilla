# Las trece reglas de auditoría

> R01 a R13. Se listan catorce filas porque **R08 se evalúa en dos variantes**, `R08a` y `R08b`.

Umbrales fijados por decisión de negocio, no genéricos. Esta es la versión de referencia;
el texto operativo y vinculante vive en `prompts/system_prompt.md`. Ante cualquier diferencia entre
esta tabla y el contrato, **manda el contrato**.

## Hallazgos — se enumeran uno por uno

| ID | Condición | Severidad | Alcance |
|---|---|---|---|
| R01 | `Hora_Fin` ≤ `Hora_Inicio` **cuando el turno no es Noche**. En turno Noche es correcto: cruza la medianoche | Alta | Fila |
| R02 | `Tiempo_Setup_min` + `Tiempo_Parada_min` mayor que `Tiempo_Total_min` | Alta | Fila |
| R03 | Parada sin motivo cargado, o motivo `Otros` sin observaciones que lo expliquen | Media | Fila |
| R04 | Alguno de los 12 campos obligatorios vacío. Un `0` es valor válido, no vacío | Alta | Fila |
| R05 | `Cant_Producida` = 0 con `Tiempo_Productivo_min` mayor a 60 | Media | Fila |
| R08a | Más de 2 paradas No Planificadas en la misma línea y día | Media | Agregado |
| R08b | `Tiempo_Parada_min` acumulado mayor a 120 min por línea y día | Media | Agregado |
| R09 | Mismo motivo 4 o más veces en la semana y línea, comparado normalizado | Alta | Agregado |
| R11 | Diferencia mayor a 10 puntos entre el OEE de dos operarios en la misma línea y turno. El OEE de un operario es el **promedio simple de sus filas**; solo entran los que tienen **2 o más turnos** en esa combinación | Baja | Agregado |
| R12 | Lote `Abierto` con **6 o más días hábiles** sin cerrarse. Se cuentan los hábiles **posteriores** a la fecha de la fila, hasta el corte inclusive | Media | Fila |
| R13 | `Motivo_Parada` fuera del catálogo cerrado, después de normalizar | Baja | Fila |

## Métricas — se resumen, no se enumeran

| ID | Qué mide | Umbral | Qué se detalla |
|---|---|---|---|
| R06 | `OEE_pct` por turno | 60% | Promedio, cantidad bajo umbral, los 5 peores |
| R07 | `Cumplimiento_Meta_pct` | <100% no cumplida · <80% crítica | Promedio, cantidad no cumplida, todos los críticos |
| R10 | `Calidad_pct` por operario y línea | 95% | Promedio, quiénes están debajo, proyección de cierre |

## Regla descartada

La versión original incluía una regla de trazabilidad: *"OF_Lote sin registros de cierre dentro
del plazo esperado"*. **La planilla no tenía ningún campo de cierre**, así que la regla pedía algo
que los datos no contenían. Se agregaron `Estado_Lote` y `Fecha_Cierre_Lote` a la planilla y la
regla pasó a ser R12, ya evaluable.

## Definiciones que usan varias reglas

- Un turno dura **480 minutos**. `T1`/Mañana 06:00–14:00 · Tarde 14:00–22:00 · Noche 22:00–06:00.
- **Normalizar** un motivo: minúsculas, sin tildes, sin espacios sobrantes. Con eso
  `Falla eléctrica`, `falla electrica` y `Falla Electrica` son el mismo motivo.
- Catálogo cerrado de motivos: `Cambio de formato`, `Falla mecanica`, `Falla electrica`,
  `Falta de insumo`, `Ajuste de calidad`, `Mantenimiento programado`, `Otros`.
- **Días hábiles** excluye sábados y domingos.

## Por qué los umbrales importan tanto

Cinco de las reglas originales decían *"el umbral definido (ej. 65%)"*. Ese `ej.` obliga al modelo
a decidir si el número es el umbral o un ejemplo de umbral, y puede decidir distinto en cada
corrida. Un solo umbral ambiguo alcanza para que dos corridas dejen de ser comparables — que es
justamente lo único que se le pide a la salida.

## Historial de las reglas

- **R11** se precisó en la iteración 2: se definió el promedio simple y el mínimo de dos turnos.
- **R12** se precisó en la iteración 3: el umbral pasó a ser un número y se fijó qué días entran
  al conteo, con el caso de borde resuelto como ejemplo dentro de la propia regla.

La redacción anterior de ambas queda en `prompts/system_prompt_v1.md` y `prompts/system_prompt_v2.md`.
El efecto medido de cada cambio está en `EXPERIMENTO.md`.
