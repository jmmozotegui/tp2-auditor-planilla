# Análisis económico

## Cómo corre hoy, y qué cuesta

El auditor **no se factura por token**. Corre como tarea programada dentro de un plan de equipo de Claude, los lunes a la mañana, sin que nadie la dispare.

Eso significa que **el costo marginal de una corrida es cero**. La suscripción ya está paga y se usa para muchas otras cosas; una auditoría semanal no agrega un peso a la factura. Decir "esta corrida costó USD 0,11" sería falso: nadie emitió esa factura.

Lo que sí consume es **cupo de uso del plan y tiempo**. Ése es el recurso escaso y es lo que se mide acá.

Se informan dos escenarios, separados a propósito:

| Escenario | Quién paga | Unidad relevante |
|---|---|---|
| **Hoy** — tarea programada dentro del plan | La suscripción de equipo, ya existente | Tokens consumidos y minutos de corrida |
| **Productizado** — corriendo contra la API | Un costo nuevo, por consumo | USD por corrida |

## Lo que consume una corrida

Medido sobre los archivos reales de `run_v3_A`, no estimado a ojo:

| Componente | Caracteres |
|---|---:|
| `prompts/system_prompt.md` (contrato v3) | 12.496 |
| `prompts/user_prompt.md` | 738 |
| `planilla_produccion_mes.csv` (182 filas) | 37.120 |
| **Entrada total** | **50.354** |
| Salida completa del informe | 81.684 |

**El entorno no registró los tokens**, así que se estiman con la equivalencia que publica la documentación de Anthropic —*"1 token es aproximadamente 4 caracteres"*—:

```
tokens de entrada ≈ 50.354 / 4 ≈ 12.600
tokens de salida  ≈ 81.684 / 4 ≈ 20.400
consumo total     ≈ 33.000 tokens por corrida
```

Es una **estimación declarada**, no una lectura de contador. Se marca así porque el propio contrato del auditor penaliza afirmar como medido lo que fue calculado.

A una corrida por semana: **≈ 1,7 millones de tokens al año**. Para un plan de equipo es una fracción menor del uso disponible: el equivalente a unas pocas conversaciones largas repartidas en doce meses.

## Tiempo de corrida

Éste sí es un dato medido directamente, en las corridas del experimento:

| Modelo | Duración | Hallazgos |
|---|---:|---:|
| **Claude Haiku 4.5** | **2 min 57 s** | 84 |
| Claude Opus 5 | 3 min 18 s / 3 min 39 s | 84 |
| Claude Sonnet 5 | 3 min 47 s | 84 |

Para una tarea programada que corre de madrugada, tres o cuatro minutos es indistinto. El dato importa por otra razón: el modelo más chico no es más lento.

## Escenario productizado

Si el sistema saliera del plan y corriera contra la API —lo que corresponde si la planta lo adopta en serio y deja de depender de la cuenta de una persona— el costo se calcula así:

```
costo por corrida = (tokens_entrada / 1.000.000 × precio_entrada)
                  + (tokens_salida  / 1.000.000 × precio_salida)
```

Precios de lista publicados en `platform.claude.com/docs/en/about-claude/pricing`, consultados el **2026-09-12**.

| Modelo | Entrada USD/M | Salida USD/M | Por corrida | **Anual (52)** |
|---|---:|---:|---:|---:|
| **Claude Haiku 4.5** | 1 | 5 | USD 0,1146 | **USD 5,96** |
| Claude Sonnet 5 | 2 | 10 | USD 0,2292 | USD 11,92 |
| Claude Opus 5 | 5 | 25 | USD 0,5730 | USD 29,80 |

Verificación de la cuenta para Haiku 4.5:

```
(12.600 / 1.000.000 × 1) + (20.400 / 1.000.000 × 5)
= 0,0126 + 0,1020
= USD 0,1146 por corrida  →  × 52 = USD 5,96 al año
```

**Estas cifras son un escenario, no un gasto incurrido.** Hoy nadie las paga.

### Sensibilidad

**Tokenizador.** Los modelos Claude 4.7 y posteriores usan un tokenizador que produce alrededor de 30% más tokens para el mismo texto. Haiku 4.5 usa el anterior, así que la estimación le aplica directo; con un modelo más nuevo, el escenario anual pasaría de USD 5,96 a **USD 7,75**.

**Volumen.** Si se pasara de una planilla mensual a una semanal por línea —cuatro líneas, cuatro corridas por semana— el escenario anual con Haiku 4.5 sería **USD 23,84**.

**Cacheo.** El contrato (≈3.100 tokens) se repite idéntico entre corridas y podría cachearse a 0,1x, ahorrando unos USD 0,0028 por corrida. Irrelevante: el grueso de la entrada es la planilla, que cambia cada semana. Se descarta por eso, no por desconocimiento.

**Lote.** La Batch API da 50% de descuento pero no aplica: el informe se necesita esa misma mañana.

## Elección de modelo

El criterio del curso es **el modelo más chico que hace bien la tarea**. Para decidirlo no alcanza con suponer: se midió.

El mismo contrato v3, sobre la misma planilla de 182 filas y la misma fecha de corte, se ejecutó en tres modelos, cada uno en sesión aislada:

| Corrida | Modelo | Hallazgos | R11 | ¿Coincide con el oráculo? |
|---|---|---:|---:|---|
| `run_v3_A` / `run_v3_B` | Claude Opus 5 | 84 | 6 | sí |
| `run_v3_sonnet` | Claude Sonnet 5 | 84 | 6 | sí |
| `run_v3_haiku` | Claude Haiku 4.5 | 84 | 6 | sí |

**Los 84 identificadores son idénticos en los tres.** Diferencia simétrica cero entre cualquier par. Y los 6 hallazgos de R11 coinciden uno a uno con `experimento/verificacion_r11.py`, el cálculo determinístico que no usa modelo.

Dos conclusiones:

1. **El contrato es portable.** Que tres motores distintos produzcan la misma salida es la prueba de que la lógica vive en la especificación. Si dependiera del modelo, no sería un contrato.

2. **Corresponde el más chico.** Haiku 4.5 entrega el mismo resultado que Opus 5, en menos tiempo, consumiendo menos cupo del plan. Y si el sistema se productizara, a un quinto del costo.

**Modelo elegido: Claude Haiku 4.5.**

La justificación no depende del escenario: dentro del plan gana porque consume menos y tarda menos; fuera del plan gana además por precio. Usar un modelo más grande sería pagar —en cupo o en dólares— por una salida idéntica.

### Cuándo revisar esta decisión

La equivalencia está medida sobre **una** planilla de 182 filas. No es una garantía universal. Corresponde repetir la comparación si:

- la planilla crece de forma significativa, porque las reglas agregadas son las más sensibles al volumen;
- se agregan reglas nuevas, sobre todo si requieren razonamiento en varios pasos;
- una corrida de Haiku difiere del oráculo de R11.

El control ya existe y es barato: `verificacion_r11.py` contrasta cualquier corrida contra el cálculo determinístico antes de darla por buena.

## Decisión de arquitectura para el uso real

Este trabajo corre sobre datos sintéticos. Para el uso real hay dos caminos, y la diferencia **no es económica**:

| | Tarea programada en el plan | API con agendamiento propio |
|---|---|---|
| Costo marginal | Cero | ≈ USD 6 al año |
| Clave de API | No hace falta | Hay que administrarla |
| Infraestructura | Ninguna | Alguien tiene que mantenerla |
| De quién depende | De la cuenta de una persona | De un servicio de la empresa |
| Dónde queda el informe | En el espacio de trabajo de Claude | Donde se lo mande: red interna, correo |

A una corrida por semana, **la tarea programada alcanza y es más simple**. La razón para mover el sistema a la API no sería el gasto —seis dólares al año no mueven ninguna decisión— sino dejar de depender de la cuenta de una persona: si esa persona se va o cambia de plan, la auditoría se corta.

La recomendación es empezar por la tarea programada y migrar recién cuando el informe tenga que llegar a otros sistemas o cuando la continuidad no pueda depender de un individuo.

**Estado actual:** la tarea programada existe y funcionó de forma no supervisada. Sobre datos sintéticos se mantiene activa solo mientras dure la evaluación de este trabajo; para el uso real hay que decidir antes quién es el dueño del proceso, que es una definición de gobierno y no de costo.
