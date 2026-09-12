# Experimento — aislar el efecto de un cambio de contrato

## Por qué existe este experimento

La devolución de la Entrega 2 pedía una cosa concreta:

> *"Para cerrar la historia experimental, ejecutá el contrato final con la nueva R11 y mostrá cuáles hallazgos aparecen frente a la versión anterior."*

Al ir a responderlo apareció un problema de diseño en la comparación que ya estaba publicada:

| Corrida publicada | Contrato | Fecha de corte | Filas | Hallazgos |
|---|---|---|---:|---:|
| `run_1` | v1 | 2026-08-19 | 117 | 41 |
| `run_2` | v2 | 2026-08-30 | 182 | 87 |

> **Sobre `run_3`.** La Entrega 2 presentaba una tercera corrida como prueba de repetibilidad de v2. Al auditar el repositorio se comprobó que ese archivo era **byte a byte idéntico a `run_2` salvo la hora**: las 87 descripciones, evidencias y acciones en texto libre coincidían palabra por palabra, algo que dos ejecuciones independientes no producen. No tenía valor probatorio, así que se reemplazó por una re-ejecución real de v2, hecha el 2026-09-12 en sesión aislada. El resultado está en el Hallazgo 3 y **desmiente** la repetibilidad que se había afirmado. Se documenta en vez de corregirse en silencio.

Entre 41 y 87 **cambiaron dos cosas a la vez**: la redacción de R11 y el tamaño de la entrada. La diferencia no es atribuible al contrato. Es un experimento con la variable confundida, y por eso la pregunta del corrector no tenía respuesta con lo que había.

## Diseño

Se fija todo salvo una variable.

- **Entrada:** la misma planilla de 182 filas en los cuatro casos.
- **Fecha de corte:** 2026-08-30 en los cuatro casos.
- **Sesiones:** cada corrida en una sesión nueva y aislada, sin acceso a las otras salidas. A cada ejecución se le indicó explícitamente no leer los archivos de las demás.
- **Variable:** únicamente la redacción del contrato.

Además se construyó un **oráculo independiente** (`experimento/verificacion_r11.py`): un cálculo determinístico en Python que aplica R11 tal como está escrita, sin modelo de por medio. Sirve para decidir si una corrida acertó, sin depender de otra corrida.

## Resultados

| Corrida | Contrato | Total | R11 | R12 | ¿R11 correcto? |
|---|---|---:|---:|---:|---|
| `run_v1_corte3008` | v1 | 90 | 9 | 34 | ✗ |
| `run_2` (publicada) | v2 | 87 | 9 | 31 | ✗ |
| `run_v3_A` | v3 | **84** | 6 | 31 | ✓ |
| `run_v3_B` | v3 | **84** | 6 | 31 | ✓ |

El oráculo devuelve **6 hallazgos** de R11: `EXT-01-Noche`, `EXT-02-Mañana`, `EXT-02-Noche`, `EXT-02-Tarde`, `TRZ-01-Noche`, `TRZ-01-Tarde`.

### Hallazgo 1 — la nueva R11 no cambió ningún hallazgo

Diferencia de conjuntos entre v1 y v2 sobre la misma entrada: los **nueve identificadores de R11 son idénticos**, uno por uno.

La respuesta a la pregunta del corrector es un **resultado negativo**: con la nueva R11 no aparece ningún hallazgo que antes no estuviera, ni desaparece ninguno. La reescritura —promedio simple, mínimo dos turnos, patrón de identificador— hizo la regla explícita, pero no modificó el comportamiento observable sobre esta planilla.

Es un resultado menos vistoso que el esperado y se informa tal cual. Forzar una diferencia habría requerido cambiar también la entrada, que es exactamente el defecto que este experimento vino a corregir.

### Hallazgo 2 — la corrida publicada tiene tres falsos positivos

Las tres diferencias entre v1 y v2 no están en R11 sino en **R12**, cuyo texto es idéntico en ambas versiones. O sea: no las causó el cambio de contrato.

Contrastadas contra el oráculo, las corridas `v1` y `run_2` reportan tres hallazgos de R11 que no corresponden:

| Identificador | Diferencia real de OEE | Umbral | ¿Corresponde? |
|---|---:|---:|---|
| `R11-EXT-01-Mañana` | 9,63 | > 10 | no |
| `R11-EXT-01-Tarde` | 6,97 | > 10 | no |
| `R11-TRZ-01-Mañana` | 8,43 | > 10 | no |

**`run_2.md`, la corrida que forma parte de la Entrega 2, contiene tres hallazgos inexistentes.** No es un defecto de la regla: la regla estaba bien escrita. Es la corrida la que contó mal.

### Hallazgo 3 — el problema real es de repetibilidad, no de redacción

La comprobación más directa llegó al final. Se ejecutó el contrato **v2 otra vez**, en sesión nueva y aislada, sobre la misma planilla y la misma fecha de corte que `run_2`. Sin cambiar una palabra del contrato.

| | `run_2` (2026-08-27) | `run_3` (2026-09-12) |
|---|---:|---:|
| Total | 87 | 87 |
| R11 | **9** | **6** |
| R12 | **31** | **34** |
| **Diferencia simétrica** | | **6 identificadores** |

**Los dos totales coinciden y las corridas son distintas.** Tres identificadores entran y tres salen:

| Solo en `run_2` | Solo en `run_3` |
|---|---|
| `R11-EXT-01-Mañana` | `R12-EXT-02-2026-08-21-Noche` |
| `R11-EXT-01-Tarde` | `R12-EXT-02-2026-08-21-Tarde` |
| `R11-TRZ-01-Mañana` | `R12-TRZ-01-2026-08-21-Noche` |

Ése es el argumento entero a favor de los identificadores determinísticos: **comparando totales, las dos corridas parecen idénticas. Comparando conjuntos, difieren en seis hallazgos.** Un informe que solo dijera "87 hallazgos" habría ocultado el problema por completo.

Y las seis diferencias caen exactamente en los dos puntos ambiguos del contrato v2: el conteo de R11 y el borde de R12. No es azar: es dónde la regla dejaba lugar a decidir.

Conclusión: el problema no estaba en cómo estaba redactada R11. Estaba en que **una regla agregada con umbral admite resultados distintos entre corridas** cuando el conteo se hace por lectura y no por cálculo.

### Hallazgo 4 — el borde de R12

Las tres diferencias de R12 entre `v1` y `v2` son lotes abiertos del viernes 2026-08-21. Entre esa fecha y el corte del 2026-08-30 hay **exactamente cinco días hábiles**: 24, 25, 26, 27 y 28.

R12 pedía *"más de 5 días hábiles"*. Cinco no es más que cinco, así que no correspondía reportarlos: `v2` acertó y `v1` sobre-reportó. Pero el texto no decía si el día de la fila contaba, ni si el corte se incluía, así que las dos lecturas eran defendibles.

## Iteración 3 — qué se cambió y qué efecto tuvo

**Pieza tocada:** restricciones del system prompt. Una sola regla, R12.

**Antes:**

> `Estado_Lote` igual a `Abierto` y pasaron más de **5 días hábiles** entre la `Fecha` de la fila y la fecha de corte

**Después:**

> `Estado_Lote` igual a `Abierto` y el lote lleva **6 o más días hábiles** sin cerrarse. El conteo son los días hábiles **posteriores** a la `Fecha` de la fila, hasta la fecha de corte **inclusive**: no se cuenta el día de la fila ni los sábados y domingos. Ejemplo de borde: fila del viernes 2026-08-21 con corte 2026-08-30 → hábiles posteriores 24, 25, 26, 27 y 28 = **5** → **no** genera hallazgo. Con 6 o más, sí.

Tres cambios de fondo: el umbral pasa de una comparación ambigua a un número, se define qué días entran al conteo, y se incluye el caso de borde resuelto como ejemplo.

**Efecto medido.** Dos corridas independientes del contrato v3, en sesiones aisladas:

| | `run_v3_A` | `run_v3_B` |
|---|---:|---:|
| Total | 84 | 84 |
| R11 | 6 | 6 |
| R12 | 31 | 31 |
| **Diferencia simétrica** | \-- | **0** |

Los 84 identificadores coinciden uno a uno. Y los 6 de R11 coinciden con el oráculo.


## Portabilidad entre modelos

Después de cerrar la iteración 3 se agregó una comprobación que el experimento original no contemplaba: **si el contrato es una especificación de verdad, motores distintos deberían producir la misma salida.**

Se ejecutó el contrato v3 sobre la misma planilla y la misma fecha de corte en tres modelos, cada uno en sesión aislada:

| Corrida | Modelo | Hallazgos | R11 |
|---|---|---:|---:|
| `run_v3_A`, `run_v3_B` | Claude Opus 5 | 84 | 6 |
| `run_v3_sonnet` | Claude Sonnet 5 | 84 | 6 |
| `run_v3_haiku` | Claude Haiku 4.5 | 84 | 6 |

**Los 84 identificadores de hallazgo coinciden uno a uno entre los tres modelos.** Diferencia simétrica cero para cualquier par, y los 6 de R11 coinciden con el oráculo.

Lo que coincide es el **conjunto de hallazgos**, que es lo que el contrato define y lo que se compara. No coincide todo lo demás: el bloque `reglas_no_evaluables` trae 4, 3 y 2 entradas según la corrida, porque el contrato no fija cuántas declarar ni con qué granularidad. Es una imprecisión del contrato, no una discrepancia de criterio — las tres corridas identifican las mismas dos combinaciones sin par comparable, TRZ-02/Tarde y TRZ-03/Noche. Precisar ese bloque queda pendiente.

Eso responde una pregunta que quedaba implícita: la lógica de auditoría vive en el contrato, no en el modelo. Si dependiera del motor, tres motores distintos habrían dado tres respuestas distintas.

La consecuencia económica está en `ANALISIS_ECONOMICO.md`: si el modelo más chico entrega el mismo resultado, corresponde usar el más chico.

## Qué queda abierto

El hallazgo 3 **no está resuelto**. R12 quedó blindada con un borde explícito, pero la inestabilidad de R11 entre corridas es un problema de otra naturaleza: no se arregla redactando mejor, porque la redacción ya era correcta.

La dirección de trabajo, no implementada acá, es que el contrato exija mostrar el cálculo intermedio —el promedio por operario y el conteo de turnos de cada combinación— antes de decidir si hay hallazgo. Un resultado que se puede auditar paso a paso es más difícil de errar que uno que se afirma de una.

Mientras tanto, `verificacion_r11.py` funciona como control: cualquier corrida puede contrastarse contra él antes de darla por buena.

## Archivos

```
prompts/system_prompt.md            contrato v3 vigente (única diferencia con v2: R12)
experimento/run_v1_corte3008.md     v1 sobre la entrada de 182 filas
corridas/run_v3_A.md                v3, primera corrida aislada
corridas/run_v3_B.md                v3, segunda corrida aislada
corridas/run_3.md                   v2 re-ejecutada, prueba de repetibilidad
experimento/ids_v2_nueva.txt        identificadores de esa re-ejecución
experimento/user_prompt_v1_corte3008.md   el user prompt exacto de la corrida v1
experimento/run_v3_sonnet.md        v3 sobre Claude Sonnet 5
experimento/run_v3_haiku.md         v3 sobre Claude Haiku 4.5
experimento/ids_v1.txt              identificadores de cada corrida,
experimento/ids_v2.txt                para reproducir las diferencias
experimento/ids_v3_A.txt              de conjuntos con comm o diff
experimento/ids_v3_B.txt
experimento/ids_v3_sonnet.txt
experimento/ids_v3_haiku.txt
experimento/verificacion_r11.py     oráculo determinístico de R11
```

Reproducir la comparación:

```bash
comm -13 ids_v3_A.txt ids_v2.txt      # hallazgos que v3 ya no reporta
diff ids_v3_A.txt ids_v3_B.txt        # repetibilidad de v3: sin salida
python3 experimento/verificacion_r11.py planilla_produccion_mes.csv   # desde la raíz del repo
```
