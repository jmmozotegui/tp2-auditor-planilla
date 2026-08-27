# Auditor de planilla de producción — contrato de prompts

**TP2 — Creación de Agentes de IA — MBA UCEMA**
Autor: Juan Mozotegui · Agosto 2026

Un agente que audita la planilla de carga de una planta industrial y devuelve un informe estructurado y comparable entre corridas. Corre solo, todos los lunes a las 8, sin intervención humana.

> **Datos sintéticos.** La planilla es inventada: líneas `EXT-01`, `EXT-02`, `TRZ-01`, operarios `OP-101` a `OP-106`, empresa sin nombrar. Ninguna instalación, persona ni dato real está representado. La estructura, las reglas de negocio y el comportamiento del agente sí son reales.

---

## 1. La tarea recurrente

Todos los turnos, los supervisores cargan a mano una planilla con lo que produjo cada línea: horarios, paradas, motivos, cantidades, rechazos. De ahí salen después los indicadores de eficiencia de la planta, así que **un dato mal cargado se propaga a todos los reportes que vienen abajo**.

Hoy esa planilla la revisa alguien a ojo, todas las semanas, y se le pasan cosas. Es una tarea repetitiva, con criterios estables, sobre un formato fijo — exactamente el perfil de lo que conviene delegar.

Elegí esta tarea sobre otras candidatas (el resumen semanal de eficiencia, la respuesta tipo a clientes) por una razón concreta: **una auditoría tiene verdad objetiva**. Un hallazgo está bien o está mal, y se verifica contra la fila que cita. Eso permite describir las fallas del contrato en términos contables —"16 falsos positivos, todos de turno noche"— en vez de "quedó raro". Un resumen semanal se evalúa por criterio, y eso no da material para iterar.

## 2. El contrato

Dos archivos de texto. Lo que **no cambia entre corridas** vive en el system prompt; lo que **sí cambia** vive en el user prompt.

| Pieza | Dónde está |
|---|---|
| **Rol** | `system_prompt.md` § 1 |
| **Contexto** | `system_prompt.md` § 2 |
| **Tarea** | `system_prompt.md` § 3 |
| **Restricciones** | `system_prompt.md` § 4 |
| **Formato** | `system_prompt.md` § 5 |
| **Ejemplos** | `system_prompt.md` § 6 |
| Pedido puntual de la corrida | `user_prompt.md` |

Las seis secciones están rotuladas en el archivo con comentarios HTML (`<!-- PIEZA 1 · ROL -->`) que no se ven al renderizar el markdown pero permiten ubicarlas sin buscar.

El corazón del contrato son **14 reglas de auditoría** con umbrales explícitos, repartidas en dos familias:

- **Hallazgos** (R01–R05, R08a, R08b, R09, R11, R12, R13) — excepciones puntuales, se enumeran una por una.
- **Métricas** (R06, R07, R10) — el estado del proceso, siempre tiene un valor, se resume.

Esa separación no estaba en el diseño original y fue la decisión más importante del trabajo. La regla de cumplimiento de meta dispara en **117 de 180 turnos**: si se enumeraran todas, el informe tendría 175 líneas y nadie lo leería. Un auditor que devuelve todo no auditó nada.

### Los umbrales

Ninguno es genérico. Salieron de decidirlos uno por uno:

| Regla | Umbral | Criterio |
|---|---|---|
| R06 · OEE | 60% | Piso inicial, con intención de subirlo |
| R07 · Meta | <100% no cumplida · <80% crítica | Cumplido o no cumplido, más un nivel de alarma |
| R08a · Paradas | más de 2 no planificadas por línea/día | Detecta inestabilidad |
| R08b · Paradas | más de 120 min acumulados | Detecta la parada única larga que el conteo no ve |
| R09 · Recurrencia | 4 o más veces en la semana | |
| R10 · Calidad | 95% | Con proyección de cierre semanal y mensual |
| R11 · Desvío entre operarios | 10 puntos | "No debería existir diferencia; si la hay, la necesito para estandarizar" |
| R12 · Lotes sin cerrar | 5 días hábiles | Deja fuera el ciclo normal de 1 a 3 días |

Redactar el documento de reglas dejó a la vista que **cinco de las doce originales decían "el umbral definido (ej. 65%)"**. Ese "ej." es la palabra más cara del documento: obliga al modelo a adivinar si el número es el umbral o un ejemplo, y puede adivinar distinto en cada corrida. Fijarlos fue la condición previa a que las corridas fueran comparables.

Una regla quedó afuera. La original pedía detectar lotes "sin registros de cierre dentro del plazo esperado", pero **la planilla no tenía ningún campo de cierre**: la regla pedía algo que los datos no contenían. Se agregaron `Estado_Lote` y `Fecha_Cierre_Lote` a la planilla, y recién entonces la regla pasó a ser evaluable.

## 3. El formato de salida

JSON con esquema fijo, más la misma información como tabla markdown debajo. El JSON hace la comparación mecánica; la tabla la hace legible.

Dos decisiones de diseño hacen que las corridas sean comparables de verdad:

**Identificadores determinísticos.** Cada hallazgo lleva un `id` armado siempre igual — `R03-EXT-02-2026-08-07-Mañana`. El mismo hallazgo produce el mismo identificador en todas las corridas, así que comparar dos salidas es cruzar dos listas de identificadores: los que están en las dos se encontraron, los que faltan se pasaron, los que sobran se inventaron. Tres restas de conjuntos, sin interpretación.

**Distinción entre "no encontré" y "no pude evaluar".** El bloque `reglas_no_evaluables` existe para que el agente pueda plantarse. Una corrida limpia y una corrida rota nunca se confunden.

## 4. Cómo se ejecuta

Una **tarea programada** que corre los lunes a las 8:00. Al dispararse arranca una sesión nueva y vacía, sin memoria de ninguna conversación previa. Lee el contrato y la planilla, audita, y escribe el informe.

Que la sesión sea nueva no es un detalle: **si el contrato se ejecutara dentro del chat donde fue escrito, el modelo arrastraría criterios aclarados de palabra y ejemplos mencionados al pasar, y la salida dejaría de ser atribuible al contrato.** Se estaría midiendo la conversación, no el contrato.

## 5. Las tres corridas

Las tres se ejecutan sobre **la misma planilla**, de modo que el contrato es la única variable. Cualquier diferencia en la salida es atribuible al cambio que se hizo y a nada más.

| Corrida | Contrato | Corte | Filas | Hallazgos | A / M / B | No evaluables |
|---|---|---|---|---|---|---|
| **run_1** | v1 | 2026-08-19 | 117 | **41** | 6 / 35 / 0 | 2 |
| **run_2** | v2 | 2026-08-30 | 182 | **87** | 10 / 66 / 11 | 7 |
| **run_3** | v2 | 2026-08-30 | 182 | **87** | 10 / 66 / 11 | 7 |

`run_2` y `run_3` son dos ejecuciones **independientes del mismo contrato**, en sesiones distintas,
sobre los mismos datos. Sirven como prueba de repetibilidad: los dos informes tienen **los mismos
87 identificadores de hallazgo, con diferencia simétrica cero**, y son iguales byte a byte salvo la
línea de hora en el encabezado. Que dos sesiones que no se conocen entre sí produzcan la misma
salida es la evidencia de que el contrato, y no el criterio del modelo, es lo que gobierna el
resultado.

Las salidas completas están en `salidas/`. Las versiones anteriores de los prompts, en `versiones/`.

**Resultado de la corrida 1** (contrato v1, corte 2026-08-19, 117 filas analizadas):
41 hallazgos — 6 Alta, 35 Media, 0 Baja — y 2 reglas declaradas no evaluables.
Contrastada contra un cálculo determinístico independiente de las mismas reglas: **cero falsos
positivos**, un único falso negativo (`R09-TRZ-01-2026-W34`, el caso que cae exactamente en el
umbral de "4 o más"), y los 8 hallazgos de R11 ausentes por la negativa razonada que se documenta
en la iteración 2.

## 6. Las dos iteraciones

### Iteración 1 — pieza tocada: **tarea**

**Qué falló.** La corrida 1 se ejecutó con fecha de corte fija al 2026-08-19, escrita a mano en el user prompt. Al cargarse días nuevos en la planilla, el agente los ignoró: siguió auditando hasta el 19 de agosto y reportó **63 filas ignoradas por corte** que en realidad eran datos vigentes. No es un error del agente — hizo exactamente lo que decía el contrato. El contrato estaba mal escrito.

Apareció además un segundo síntoma: la planilla incorporó dos líneas nuevas, `TRZ-02` y `TRZ-03`, que no figuraban en la sección de contexto del system prompt. Había riesgo real de que el agente las descartara por no estar en la lista.

**Qué se cambió.** Solo el user prompt. La fecha de corte pasó de un valor fijo a una regla: *"la fecha más reciente que aparezca en la columna Fecha"*. Y se agregó una línea aclarando que el contexto describe la planta pero no limita qué filas se revisan.

**Qué cambió en la salida.** El corte pasó del 19/08 al 30/08 y las filas analizadas de 117 a 182:
las 63 que antes se descartaban entraron al análisis, junto con las dos nuevas. Los hallazgos
pasaron de 41 a 87. Las líneas `TRZ-02` y `TRZ-03` fueron auditadas normalmente. Ver `salidas/run_2.md`.

Un efecto secundario que no anticipé: las reglas declaradas **no evaluables pasaron de 2 a 7**
(R01, R02, R06, R10 y R11). Con más datos aparecieron más casos donde el contrato no alcanza a
decidir, y el agente los reportó en vez de resolverlos por su cuenta. El contrato no empeoró: se
expuso más.

### Iteración 2 — pieza tocada: **restricciones**

**Qué falló.** En la corrida 1 el agente **se negó a evaluar la regla R11** y explicó por qué con precisión:

> *"El contrato no define cómo se obtiene el OEE de un operario cuando tiene más de una fila en la misma línea y turno, y el resultado cambia según el criterio que se use. En TRZ-01 turno Mañana: comparando filas individuales la diferencia es 20,5 puntos; promediando por operario la diferencia es 6,6 puntos. Tampoco existe en el contrato un formato de identificador para un alcance agregado por línea y turno sobre todo el período. No se evalúa para no inventar un criterio."*

Ocho hallazgos que la referencia esperaba no aparecieron. Y el argumento es correcto: la regla decía *"diferencia mayor a 10 puntos entre operarios"* sin decir entre qué números exactamente.

**Qué se cambió.** Una sola línea de la tabla de restricciones. La regla R11 pasó a definir tres cosas que antes no decía: que el OEE de un operario es el **promedio simple de sus filas**, que solo entran a la comparación los operarios con **2 o más turnos** registrados en esa combinación, y cuál es el patrón de identificador.

**Estado.** El cambio está aplicado en `system_prompt.md`, que es la versión final del contrato,
y el "antes" está guardado en `versiones/system_prompt_v1.md`. La corrida que lo verifica es la
próxima ejecución programada: no se forzó una corrida extra para no inflar el expediente con
ejecuciones fuera del ciclo real de la tarea. La diferencia entre las dos versiones es de una sola
línea y se ve con `diff versiones/system_prompt_v1.md system_prompt.md`.

**Una aclaración de método.** El agente había señalado *dos* huecos: el criterio de agregación y el formato de identificador. La consigna pide tocar una pieza por vez, así que ambos se resolvieron dentro de la misma pieza —restricciones—, especificando el identificador en la propia definición de la regla en lugar de modificar la sección de formato. Si se hubieran tocado las dos secciones, no se sabría cuál de los dos cambios produjo la mejora.

## 7. Lo que aprendí del contrato

**El contrato no es una instrucción, es una especificación.** La diferencia se ve en el "ej.". Cinco reglas decían "el umbral definido (ej. 65%)" y las cinco eran no determinísticas: el modelo tenía que elegir, y podía elegir distinto cada vez. Un contrato con un solo número ambiguo ya no produce salidas comparables, que es lo único que se le pedía.

**El agente falla donde el contrato calla.** Ninguna de las dos iteraciones vino de que el modelo se equivocara. La primera vino de una fecha que escribí a mano en vez de definir como regla. La segunda, de una regla que decía "la diferencia entre operarios" sin decir entre qué números. En los dos casos el agente hizo exactamente lo que decía el texto.

**Que se plante puede ser mejor que que responda.** Lo más valioso de la corrida 1 fue lo que el agente *no* hizo: se negó a evaluar R11 y demostró la ambigüedad con dos números concretos. Un motor de reglas determinístico escrito en paralelo eligió "promediar por operario" en silencio y devolvió ocho hallazgos sin avisar que había tomado una decisión. **El agente fue más riguroso que el código**, y solo porque el contrato le daba permiso explícito para no responder.

**Separar lo estable de lo variable es la decisión de arquitectura.** Cuando la fecha de corte estaba escrita a mano en el user prompt parecía correcto —es un dato de la corrida—. Pero un dato que hay que actualizar a mano cada semana no es un dato de la corrida: es una regla mal escrita. Lo que va en el user prompt es lo que cambia solo.

**Un auditor que devuelve todo no auditó nada.** La regla de cumplimiento de meta dispara en dos de cada tres turnos. Enumerarlas habría producido un informe técnicamente correcto y prácticamente inútil. La distinción entre hallazgo y métrica no salió de la teoría: salió de contar cuántas veces dispara cada regla contra datos reales, antes de escribir el contrato.

## 8. Nota de proceso: el desvío por Claude Code

Este TP se empezó en Claude Code, con la idea de que el agente corriera desde la terminal. Ese camino se abandonó, y vale la pena contarlo porque el error fue conceptual y no técnico.

Al pedirle "un agente", Claude Code preguntó qué framework usar —LangChain, CrewAI, el SDK de Anthropic— y propuso una arquitectura híbrida: un motor de reglas determinístico en pandas que resolvía 8 de las 12 reglas, más una capa LLM con tool-use, tests y CLI.

El problema no era que estuviera mal construido. Era que **8 de las 12 reglas quedaban hardcodeadas en Python, fuera del contrato**. Al iterar sobre el system prompt se estaría tuneando un tercio del sistema, y cualquier resultado bueno sería atribuible al código, no al contrato. La arquitectura vaciaba exactamente lo que el TP evalúa.

Se descartó todo eso: el motor de pandas, el tool-use, los tests, el CLI y la API key de pago que la solución requería. Las 12 reglas se reescribieron en lenguaje natural dentro del system prompt. **Si una regla vive en código, el contrato no la gobierna y no se puede iterar.**

El aprendizaje: "agente" no significa software que uno escribe. Significa el modelo ejecutando un contrato sobre una entrada. La palabra que usa la consigna —*contrato*— no es decorativa: rol, contexto, tarea, restricciones, formato y ejemplos es la estructura de una descripción de puesto.

## 9. Limitaciones conocidas

- **R08a no es del todo evaluable con este esquema.** La regla cuenta "paradas no planificadas por línea y día", pero la planilla registra un solo motivo y el total de minutos por turno: las paradas individuales no están en los datos. Se interpreta como "turnos con al menos una parada no planificada", que es una lectura razonable pero es *una* lectura.
- **La proyección de calidad usa un método deliberadamente simple**: los días restantes mantienen el promedio observado. No pondera tendencia ni estacionalidad. Está fijado así en el contrato para que sea reproducible, no porque sea el mejor método.
- **El agente no tiene quien lo audite.** Si devuelve un hallazgo mal fundado, no hay un segundo agente que lo revise. Es la falla más seria del diseño.
- **La tarea lee la planilla desde el proyecto, no desde la carpeta de trabajo del usuario.** El intento de que leyera directamente de OneDrive falló: la sesión que arranca la tarea programada no hereda el acceso a las carpetas conectadas. Queda un paso de sincronización manual entre la planilla que se edita y la que el agente lee.

## 10. Estructura del repositorio

```
.
├── README.md                    ← este documento
├── system_prompt.md             ← el contrato, versión final (v3)
├── user_prompt.md               ← el pedido de corrida, versión final (v2)
├── contrato/
│   └── reglas.md                ← las 14 reglas con sus umbrales, en detalle
├── datos/
│   ├── Planilla_Produccion.xlsx ← planilla de carga, con fórmulas y listas
│   └── planilla_produccion_mes.csv ← la misma, en el formato que lee el agente
├── salidas/
│   ├── run_1.md                 ← corrida con contrato v1
│   ├── run_2.md                 ← corrida con contrato v2
│   └── run_3.md                 ← corrida con contrato v3
└── versiones/
    ├── system_prompt_v1.md      ← el "antes" de la iteración 2
    ├── system_prompt_v2.md
    ├── user_prompt_v1.md        ← el "antes" de la iteración 1
    └── user_prompt_v2.md
```

**Agente:** Claude (Anthropic), ejecutando el contrato en una sesión nueva disparada por una tarea programada semanal.
