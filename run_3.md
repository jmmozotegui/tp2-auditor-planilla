# Corrida de auditoría — planilla de producción

- **Fecha y hora de la corrida:** 2026-08-27 21:26 UTC (2026-08-27 18:26 ART)
- **Fecha de corte usada:** 2026-08-30 (fecha más reciente presente en la columna `Fecha`)
- **Filas analizadas:** 182 (todas las filas con `Fecha` ≤ 2026-08-30)
- **Filas ignoradas por corte:** 0

```json
{
  "meta": {
    "periodo_desde": "2026-08-03",
    "periodo_hasta": "2026-08-30",
    "fecha_corte": "2026-08-30",
    "filas_analizadas": 182,
    "filas_ignoradas_por_corte": 0
  },
  "hallazgos": [
    {
      "id": "R01-TRZ-02-2026-08-29-Tarde",
      "regla": "R01",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-29",
      "turno": "Tarde",
      "linea": "TRZ-02",
      "operario": "OP-102",
      "descripcion": "Hora_Fin menor a Hora_Inicio en un turno que no es Noche.",
      "evidencia": "OF-4281: Turno = \"Tarde\", Hora_Inicio = 22:01, Hora_Fin = 06:01",
      "accion": "Solicitar al supervisor SUP-04 la verificación y corrección del horario de inicio y fin cargado en la fila."
    },
    {
      "id": "R04-TRZ-01-2026-08-04-Tarde",
      "regla": "R04",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Campo obligatorio Hora_Fin vacío.",
      "evidencia": "OF-4115: Hora_Inicio = 14:00, Hora_Fin = \"\" (vacío)",
      "accion": "Solicitar al supervisor SUP-02 que complete la Hora_Fin de esta fila."
    },
    {
      "id": "R04-EXT-02-2026-08-11-Tarde",
      "regla": "R04",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-11",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Campo obligatorio Operario vacío.",
      "evidencia": "OF-4159: Operario = \"\" (vacío), Supervisor = SUP-02",
      "accion": "Solicitar al supervisor SUP-02 que identifique el legajo del operario del turno y lo cargue."
    },
    {
      "id": "R09-EXT-02-2026-W32",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-07",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma línea.",
      "evidencia": "6 ocurrencias tras normalizar: 03/08 Mañana 'falla electrica' (85 min), 04/08 Mañana 'Falla electrica' (80 min), 04/08 Noche 'Falla eléctrica' (50 min), 05/08 Mañana 'Falla electrica' (65 min), 05/08 Noche 'Falla electrica' (165 min), 06/08 Noche 'falla electrica' (100 min).",
      "accion": "Investigar la causa raíz de la falla eléctrica recurrente en EXT-02 durante esa semana."
    },
    {
      "id": "R09-TRZ-01-2026-W32",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-07",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "El motivo de parada 'falla mecanica' se repite 7 veces en la semana en la misma línea.",
      "evidencia": "7 ocurrencias tras normalizar, todas cargadas como 'Falla mecanica': 03/08 Mañana (50 min), 03/08 Noche (45 min), 04/08 Mañana (45 min), 06/08 Mañana (35 min), 06/08 Tarde (20 min), 06/08 Noche (60 min), 07/08 Noche (45 min).",
      "accion": "Investigar la causa raíz de la falla mecánica recurrente en TRZ-01 durante esa semana."
    },
    {
      "id": "R09-EXT-01-2026-W33",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-10..2026-08-14",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "El motivo de parada 'falta de insumo' se repite 5 veces en la semana en la misma línea.",
      "evidencia": "5 ocurrencias tras normalizar, todas cargadas como 'Falta de insumo': 10/08 Noche (45 min), 12/08 Tarde (60 min), 13/08 Mañana (80 min), 14/08 Mañana (15 min), 14/08 Tarde (45 min).",
      "accion": "Investigar la causa raíz de la falta de insumo recurrente en EXT-01 durante esa semana."
    },
    {
      "id": "R09-EXT-02-2026-W33",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-10..2026-08-14",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma línea.",
      "evidencia": "5 ocurrencias tras normalizar: 12/08 Mañana 'falla electrica' (50 min), 12/08 Noche 'Falla electrica' (100 min), 13/08 Mañana 'Falla electrica' (140 min), 13/08 Tarde 'Falla eléctrica' (80 min), 14/08 Tarde 'falla electrica' (130 min).",
      "accion": "Investigar la causa raíz de la falla eléctrica recurrente en EXT-02 durante esa semana."
    },
    {
      "id": "R09-EXT-02-2026-W34",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-17..2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 4 veces en la semana en la misma línea.",
      "evidencia": "4 ocurrencias tras normalizar: 17/08 Noche 'falla electrica' (100 min), 20/08 Noche 'Falla electrica' (90 min), 21/08 Tarde 'Falla eléctrica' (115 min), 21/08 Noche 'falla electrica' (95 min).",
      "accion": "Investigar la causa raíz de la falla eléctrica recurrente en EXT-02 durante esa semana."
    },
    {
      "id": "R09-TRZ-01-2026-W34",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-17..2026-08-21",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "El motivo de parada 'mantenimiento programado' se repite 4 veces en la semana en la misma línea.",
      "evidencia": "4 ocurrencias tras normalizar, todas cargadas como 'Mantenimiento programado': 17/08 Noche (30 min), 18/08 Tarde (45 min), 19/08 Tarde (15 min), 19/08 Noche (30 min).",
      "accion": "Verificar con Mantenimiento el plan de intervenciones sobre TRZ-01 en esa semana y su carga en la planilla."
    },
    {
      "id": "R09-EXT-02-2026-W35",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-24..2026-08-28",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 7 veces en la semana en la misma línea.",
      "evidencia": "7 ocurrencias tras normalizar: 24/08 Mañana 'Falla electrica' (35 min), 25/08 Noche 'Falla eléctrica' (85 min), 26/08 Tarde 'falla electrica' (110 min), 26/08 Noche 'falla electrica' (145 min), 27/08 Mañana 'Falla electrica' (150 min), 27/08 Noche 'falla electrica' (85 min), 28/08 Mañana 'Falla electrica' (180 min).",
      "accion": "Investigar la causa raíz de la falla eléctrica recurrente en EXT-02 durante esa semana."
    },
    {
      "id": "R03-EXT-02-2026-08-07-Mañana",
      "regla": "R03",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": "OP-106",
      "descripcion": "Parada registrada sin motivo cargado.",
      "evidencia": "OF-4138: Tiempo_Parada_min = 20, Motivo_Parada = \"\" (vacío), Tipo_Parada = \"\" (vacío)",
      "accion": "Solicitar al supervisor SUP-01 que complete el motivo de parada de esta fila."
    },
    {
      "id": "R03-EXT-02-2026-08-19-Tarde",
      "regla": "R03",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Motivo de parada 'Otros' sin Observaciones que lo expliquen.",
      "evidencia": "OF-4213: Motivo_Parada = \"Otros\", Tiempo_Parada_min = 15, Observaciones = \"\" (vacío)",
      "accion": "Solicitar al supervisor SUP-02 que detalle en Observaciones a qué corresponde la parada 'Otros'."
    },
    {
      "id": "R05-TRZ-01-2026-08-21-Tarde",
      "regla": "R05",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-21",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Cant_Producida igual a 0 con tiempo productivo mayor a 60 minutos.",
      "evidencia": "OF-4232: Cant_Producida = 0, Tiempo_Productivo_min = 480.0, Tiempo_Parada_min = 0, Observaciones = \"Linea detenida por espera de material\"",
      "accion": "Solicitar al supervisor SUP-02 que registre la parada correspondiente o corrija la cantidad producida de la fila."
    },
    {
      "id": "R08a-EXT-02-2026-08-05",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla electrica' (65 min), Tarde 'Falta de insumo' (120 min), Noche 'Falla electrica' (165 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 05/08."
    },
    {
      "id": "R08a-EXT-01-2026-08-06",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (45 min), Tarde 'Ajuste de calidad' (45 min), Noche 'Falla mecanica' (45 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-01 del 06/08."
    },
    {
      "id": "R08a-TRZ-01-2026-08-06",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla mecanica' (35 min), Tarde 'Falla mecanica' (20 min), Noche 'Falla mecanica' (60 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de TRZ-01 del 06/08."
    },
    {
      "id": "R08a-TRZ-01-2026-08-07",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-07",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Falta de insumo' (20 min), Tarde 'Falta de insumo' (20 min), Noche 'Falla mecanica' (45 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de TRZ-01 del 07/08."
    },
    {
      "id": "R08a-TRZ-01-2026-08-11",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (45 min), Tarde 'Falta de insumo' (95 min), Noche 'Ajuste de calidad' (30 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de TRZ-01 del 11/08."
    },
    {
      "id": "R08a-EXT-02-2026-08-12",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-12",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'falla electrica' (50 min), Tarde 'Ajuste de calidad' (20 min), Noche 'Falla electrica' (100 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 12/08."
    },
    {
      "id": "R08a-EXT-02-2026-08-13",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-13",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla electrica' (140 min), Tarde 'Falla eléctrica' (80 min), Noche 'Falta de insumo' (30 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 13/08."
    },
    {
      "id": "R08a-EXT-02-2026-08-20",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-20",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (45 min), Tarde 'Ajuste de calidad' (15 min), Noche 'Falla electrica' (90 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 20/08."
    },
    {
      "id": "R08a-EXT-02-2026-08-21",
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas No Planificada en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (60 min), Tarde 'Falla eléctrica' (115 min), Noche 'falla electrica' (95 min); las tres con Tipo_Parada = \"No Planificada\".",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 21/08."
    },
    {
      "id": "R08b-EXT-01-2026-08-03",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-03",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 120 + Tarde 0 + Noche 45 = 165 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-01 del 03/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-03",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-03",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 85 + Tarde 0 + Noche 65 = 150 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 03/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-04",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-04",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 80 + Tarde 45 + Noche 50 = 175 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 04/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-05",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 65 + Tarde 120 + Noche 165 = 350 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 05/08."
    },
    {
      "id": "R08b-TRZ-01-2026-08-05",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 90 + Noche 110 = 200 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de TRZ-01 del 05/08."
    },
    {
      "id": "R08b-EXT-01-2026-08-06",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 45 + Noche 45 = 135 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-01 del 06/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-11",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 45 + Noche 80 = 170 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 11/08."
    },
    {
      "id": "R08b-TRZ-01-2026-08-11",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 95 + Noche 30 = 170 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de TRZ-01 del 11/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-12",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-12",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 50 + Tarde 20 + Noche 100 = 170 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 12/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-13",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-13",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 140 + Tarde 80 + Noche 30 = 250 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 13/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-14",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-14",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 120 + Tarde 130 + Noche 0 = 250 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 14/08."
    },
    {
      "id": "R08b-TRZ-01-2026-08-14",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-14",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 60 + Tarde 95 + Noche 45 = 200 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de TRZ-01 del 14/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-17",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-17",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 50 + Tarde 0 + Noche 100 = 150 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 17/08."
    },
    {
      "id": "R08b-EXT-01-2026-08-19",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-19",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 80 + Noche 65 = 145 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-01 del 19/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-20",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-20",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 15 + Noche 90 = 150 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 20/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-21",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 60 + Tarde 115 + Noche 95 = 270 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 21/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-25",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-25",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 20 + Tarde 70 + Noche 85 = 175 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 25/08."
    },
    {
      "id": "R08b-EXT-01-2026-08-26",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 50 + Tarde 60 + Noche 55 = 165 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-01 del 26/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-26",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 110 + Noche 145 = 255 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 26/08."
    },
    {
      "id": "R08b-TRZ-01-2026-08-26",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 90 + Noche 0 = 135 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de TRZ-01 del 26/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-27",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-27",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 150 + Tarde 15 + Noche 85 = 250 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 27/08."
    },
    {
      "id": "R08b-EXT-02-2026-08-28",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-28",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 180 + Tarde 0 + Noche 20 = 200 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de EXT-02 del 28/08."
    },
    {
      "id": "R08b-TRZ-01-2026-08-28",
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-28",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado en el día superior a 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 75 + Noche 60 = 135 min.",
      "accion": "Verificar con el jefe de línea el detalle de las paradas de TRZ-01 del 28/08."
    },
    {
      "id": "R12-EXT-01-2026-08-03-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-03",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4104: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 19 días hábiles entre 2026-08-03 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4104 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-04-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4114: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 18 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4114 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-04-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4117: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 18 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4117 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-04-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4115: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 18 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4115 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-04-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4118: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 18 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4118 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-06-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-06",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4130: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 16 días hábiles entre 2026-08-06 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4130 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-06-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-06",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4133: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 16 días hábiles entre 2026-08-06 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4133 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-07-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4140: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 15 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4140 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-07-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4143: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 15 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4143 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-07-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4139: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 15 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4139 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-10-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-10",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-103",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4146: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 14 días hábiles entre 2026-08-10 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4146 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-11-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-11",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-103",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4155: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 13 días hábiles entre 2026-08-11 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4155 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-12-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4167: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 12 días hábiles entre 2026-08-12 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4167 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-12-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-103",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4171: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 12 días hábiles entre 2026-08-12 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4171 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-12-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4166: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 12 días hábiles entre 2026-08-12 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4166 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-13-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4173: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-13 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4173 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-13-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4179: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-13 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4179 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-13-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4178: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-13 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4178 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-14-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-14",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4190: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 10 días hábiles entre 2026-08-14 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4190 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-17-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-17",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-104",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4198: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 9 días hábiles entre 2026-08-17 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4198 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-18-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": "OP-103",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4201: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-18 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4201 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-18-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-104",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4204: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-18 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4204 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-18-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4202: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-18 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4202 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-18-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4205: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-18 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4205 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-18-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4208: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-18 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4208 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-19-Tarde",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4213: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 7 días hábiles entre 2026-08-19 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4213 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-19-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4211: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 7 días hábiles entre 2026-08-19 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4211 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-19-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4217: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 7 días hábiles entre 2026-08-19 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4217 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-01-2026-08-20-Mañana",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4218: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 6 días hábiles entre 2026-08-20 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4218 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-EXT-02-2026-08-20-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-101",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4225: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 6 días hábiles entre 2026-08-20 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4225 o la corrección de su Estado_Lote."
    },
    {
      "id": "R12-TRZ-01-2026-08-20-Noche",
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto con más de 5 días hábiles desde la fecha de la fila hasta la fecha de corte.",
      "evidencia": "OF-4226: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 6 días hábiles entre 2026-08-20 y la fecha de corte 2026-08-30.",
      "accion": "Solicitar el cierre del lote OF-4226 o la corrección de su Estado_Lote."
    },
    {
      "id": "R11-EXT-01-Mañana",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 64.6 (OP-106, 03/08); máximo = 90.6 (OP-103, 11/08); diferencia = 26.0 puntos.",
      "accion": "Comparar el método de trabajo de OP-106 y OP-103 en EXT-01 turno Mañana."
    },
    {
      "id": "R11-EXT-01-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 68.1 (OP-101, 19/08); máximo = 88.4 (OP-102, 25/08); diferencia = 20.3 puntos.",
      "accion": "Comparar el método de trabajo de OP-101 y OP-102 en EXT-01 turno Tarde."
    },
    {
      "id": "R11-EXT-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 62.0 (OP-101, 19/08); máximo = 92.5 (OP-106, 07/08); diferencia = 30.5 puntos.",
      "accion": "Comparar el método de trabajo de OP-101 y OP-106 en EXT-01 turno Noche."
    },
    {
      "id": "R11-EXT-02-Mañana",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 44.7 (OP-104, 28/08); máximo = 91.6 (OP-101, 19/08); diferencia = 46.9 puntos.",
      "accion": "Comparar el método de trabajo de OP-104 y OP-101 en EXT-02 turno Mañana."
    },
    {
      "id": "R11-EXT-02-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 55.5 (OP-104, 26/08); máximo = 92.6 (OP-106, 24/08); diferencia = 37.1 puntos. Se excluyó la fila del 11/08 (OEE_pct = 73.9) por tener Operario vacío.",
      "accion": "Comparar el método de trabajo de OP-104 y OP-106 en EXT-02 turno Tarde."
    },
    {
      "id": "R11-EXT-02-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 50.1 (OP-103, 05/08); máximo entre operarios distintos = 85.2 (OP-105, 19/08); diferencia = 35.1 puntos. El máximo absoluto del grupo (87.8, 24/08) corresponde al mismo legajo OP-103 que el mínimo.",
      "accion": "Comparar el método de trabajo de OP-103 y OP-105 en EXT-02 turno Noche."
    },
    {
      "id": "R11-TRZ-01-Mañana",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 66.6 (OP-104, 25/08); máximo = 90.0 (OP-103, 17/08); diferencia = 23.4 puntos.",
      "accion": "Comparar el método de trabajo de OP-104 y OP-103 en TRZ-01 turno Mañana."
    },
    {
      "id": "R11-TRZ-01-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 62.9 (OP-104, 17/08); máximo = 93.3 (OP-103, 27/08); diferencia = 30.4 puntos. Se excluyeron las filas del 04/08 y 21/08 por tener OEE_pct vacío.",
      "accion": "Comparar el método de trabajo de OP-104 y OP-103 en TRZ-01 turno Tarde."
    },
    {
      "id": "R11-TRZ-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos en la misma línea y turno.",
      "evidencia": "Mínimo OEE_pct = 62.8 (OP-105, 05/08); máximo = 93.5 (OP-106, 12/08); diferencia = 30.7 puntos.",
      "accion": "Comparar el método de trabajo de OP-105 y OP-106 en TRZ-01 turno Noche."
    },
    {
      "id": "R13-TRZ-02-2026-08-29-Tarde",
      "regla": "R13",
      "severidad": "Baja",
      "alcance": "fila",
      "fecha": "2026-08-29",
      "turno": "Tarde",
      "linea": "TRZ-02",
      "operario": "OP-102",
      "descripcion": "Motivo_Parada fuera del catálogo cerrado tras normalizar.",
      "evidencia": "OF-4281: Motivo_Parada = \"aa\", Tiempo_Parada_min = 60.",
      "accion": "Solicitar al supervisor SUP-04 que reemplace el motivo por uno del catálogo cerrado."
    },
    {
      "id": "R13-TRZ-03-2026-08-30-Noche",
      "regla": "R13",
      "severidad": "Baja",
      "alcance": "fila",
      "fecha": "2026-08-30",
      "turno": "Noche",
      "linea": "TRZ-03",
      "operario": "OP-103",
      "descripcion": "Motivo_Parada fuera del catálogo cerrado tras normalizar.",
      "evidencia": "OF-4282: Motivo_Parada = \"x\", Tiempo_Parada_min = 60.",
      "accion": "Solicitar al supervisor SUP-05 que reemplace el motivo por uno del catálogo cerrado."
    }
  ],
  "metricas": {
    "oee": {
      "umbral_pct": 60,
      "promedio_pct": 76.4,
      "turnos_bajo_umbral": 8,
      "peores_5": [
        { "fecha": "2026-08-28", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-104", "oee_pct": 44.7 },
        { "fecha": "2026-08-05", "turno": "Noche", "linea": "EXT-02", "operario": "OP-103", "oee_pct": 50.1 },
        { "fecha": "2026-08-13", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-104", "oee_pct": 53.6 },
        { "fecha": "2026-08-27", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-101", "oee_pct": 54.2 },
        { "fecha": "2026-08-26", "turno": "Tarde", "linea": "EXT-02", "operario": "OP-104", "oee_pct": 55.5 }
      ]
    },
    "cumplimiento_meta": {
      "promedio_pct": 94.7,
      "turnos_no_cumplidos": 119,
      "turnos_criticos": 17,
      "criticos": [
        { "fecha": "2026-08-03", "turno": "Mañana", "linea": "EXT-01", "operario": "OP-106", "cumplimiento_pct": 79.3 },
        { "fecha": "2026-08-04", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-101", "cumplimiento_pct": 79.9 },
        { "fecha": "2026-08-05", "turno": "Noche", "linea": "EXT-02", "operario": "OP-103", "cumplimiento_pct": 61.7 },
        { "fecha": "2026-08-05", "turno": "Noche", "linea": "TRZ-01", "operario": "OP-105", "cumplimiento_pct": 77.5 },
        { "fecha": "2026-08-06", "turno": "Noche", "linea": "EXT-02", "operario": "OP-106", "cumplimiento_pct": 73.3 },
        { "fecha": "2026-08-12", "turno": "Noche", "linea": "EXT-02", "operario": "OP-103", "cumplimiento_pct": 74.9 },
        { "fecha": "2026-08-13", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-104", "cumplimiento_pct": 66.2 },
        { "fecha": "2026-08-14", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-106", "cumplimiento_pct": 76.8 },
        { "fecha": "2026-08-14", "turno": "Tarde", "linea": "EXT-02", "operario": "OP-105", "cumplimiento_pct": 77.4 },
        { "fecha": "2026-08-17", "turno": "Tarde", "linea": "TRZ-01", "operario": "OP-104", "cumplimiento_pct": 78.7 },
        { "fecha": "2026-08-17", "turno": "Noche", "linea": "EXT-02", "operario": "OP-104", "cumplimiento_pct": 72.9 },
        { "fecha": "2026-08-19", "turno": "Noche", "linea": "EXT-01", "operario": "OP-101", "cumplimiento_pct": 76.2 },
        { "fecha": "2026-08-21", "turno": "Tarde", "linea": "TRZ-01", "operario": "OP-105", "cumplimiento_pct": 0.0 },
        { "fecha": "2026-08-26", "turno": "Tarde", "linea": "EXT-02", "operario": "OP-104", "cumplimiento_pct": 68.6 },
        { "fecha": "2026-08-26", "turno": "Noche", "linea": "EXT-02", "operario": "OP-102", "cumplimiento_pct": 77.6 },
        { "fecha": "2026-08-27", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-101", "cumplimiento_pct": 67.2 },
        { "fecha": "2026-08-28", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-104", "cumplimiento_pct": 55.4 }
      ]
    },
    "calidad": {
      "umbral_pct": 95,
      "promedio_pct": 97.8,
      "por_debajo_umbral": [
        { "tipo": "operario", "clave": "OP-102", "calidad_pct": 94.5, "filas": 29 }
      ],
      "proyeccion_semana": {
        "acumulado_pct": null,
        "dias_transcurridos": null,
        "dias_totales": null,
        "proyectado_pct": null,
        "cumple": null
      },
      "proyeccion_mes": {
        "acumulado_pct": 97.8,
        "dias_transcurridos": 20,
        "dias_totales": 21,
        "proyectado_pct": 97.8,
        "cumple": true
      }
    }
  },
  "reglas_no_evaluables": [
    {
      "regla": "R01",
      "motivo": "En la fila 2026-08-04 Tarde TRZ-01 (OF-4115) el campo Hora_Fin está vacío; sin ese valor no se puede comparar contra Hora_Inicio. La regla se evaluó sobre las restantes 181 filas."
    },
    {
      "regla": "R02",
      "motivo": "En la fila 2026-08-04 Tarde TRZ-01 (OF-4115) el campo derivado Tiempo_Total_min está vacío; sin ese valor no se puede comparar contra Tiempo_Setup_min + Tiempo_Parada_min. La regla se evaluó sobre las restantes 181 filas y no arrojó hallazgos."
    },
    {
      "regla": "R06",
      "motivo": "Tres filas no tienen OEE_pct cargado y quedaron fuera del promedio y del conteo bajo umbral: 2026-08-04 Tarde TRZ-01 (OF-4115), 2026-08-17 Noche EXT-01 (OF-4197) y 2026-08-21 Tarde TRZ-01 (OF-4232). La métrica se calculó sobre 179 filas."
    },
    {
      "regla": "R10",
      "motivo": "Proyección de cierre de semana: la fecha de corte 2026-08-30 es domingo y no cae dentro de ninguna semana calendario según la definición del contrato (lunes a viernes), por lo que no hay criterio en el contrato para determinar la 'semana en curso' ni sus días hábiles transcurridos y restantes. No se proyecta."
    },
    {
      "regla": "R10",
      "motivo": "Calidad por operario: la fila 2026-08-11 Tarde EXT-02 (OF-4159, Calidad_pct = 99.3) tiene Operario vacío y no pudo asignarse a ningún legajo. Calidad por línea: la fila 2026-08-21 Tarde TRZ-01 (OF-4232) tiene Calidad_pct vacío y quedó fuera del promedio de TRZ-01 y del promedio general."
    },
    {
      "regla": "R11",
      "motivo": "En TRZ-02 turno Tarde hay una sola fila en todo el período (2026-08-29, OP-102); no hay dos operarios que comparar."
    },
    {
      "regla": "R11",
      "motivo": "En TRZ-03 turno Noche hay una sola fila en todo el período (2026-08-30, OP-103); no hay dos operarios que comparar."
    }
  ],
  "resumen": {
    "hallazgos_alta": 10,
    "hallazgos_media": 66,
    "hallazgos_baja": 11,
    "total_hallazgos": 87
  }
}
```

## Tabla de hallazgos

| ID | Regla | Severidad | Fecha | Turno | Línea | Descripción | Evidencia |
|---|---|---|---|---|---|---|---|
| R01-TRZ-02-2026-08-29-Tarde | R01 | Alta | 2026-08-29 | Tarde | TRZ-02 | Hora_Fin menor a Hora_Inicio en un turno que no es Noche. | OF-4281: Turno = "Tarde", Hora_Inicio = 22:01, Hora_Fin = 06:01 |
| R04-TRZ-01-2026-08-04-Tarde | R04 | Alta | 2026-08-04 | Tarde | TRZ-01 | Campo obligatorio Hora_Fin vacío. | OF-4115: Hora_Inicio = 14:00, Hora_Fin = "" (vacío) |
| R04-EXT-02-2026-08-11-Tarde | R04 | Alta | 2026-08-11 | Tarde | EXT-02 | Campo obligatorio Operario vacío. | OF-4159: Operario = "" (vacío), Supervisor = SUP-02 |
| R09-EXT-02-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | EXT-02 | El motivo 'falla electrica' se repite 6 veces en la semana en la misma línea. | 03/08 M 'falla electrica' (85), 04/08 M 'Falla electrica' (80), 04/08 N 'Falla eléctrica' (50), 05/08 M 'Falla electrica' (65), 05/08 N 'Falla electrica' (165), 06/08 N 'falla electrica' (100) |
| R09-TRZ-01-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | TRZ-01 | El motivo 'falla mecanica' se repite 7 veces en la semana en la misma línea. | 'Falla mecanica' en 03/08 M (50), 03/08 N (45), 04/08 M (45), 06/08 M (35), 06/08 T (20), 06/08 N (60), 07/08 N (45) |
| R09-EXT-01-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-01 | El motivo 'falta de insumo' se repite 5 veces en la semana en la misma línea. | 'Falta de insumo' en 10/08 N (45), 12/08 T (60), 13/08 M (80), 14/08 M (15), 14/08 T (45) |
| R09-EXT-02-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-02 | El motivo 'falla electrica' se repite 5 veces en la semana en la misma línea. | 12/08 M 'falla electrica' (50), 12/08 N 'Falla electrica' (100), 13/08 M 'Falla electrica' (140), 13/08 T 'Falla eléctrica' (80), 14/08 T 'falla electrica' (130) |
| R09-EXT-02-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 | — | EXT-02 | El motivo 'falla electrica' se repite 4 veces en la semana en la misma línea. | 17/08 N 'falla electrica' (100), 20/08 N 'Falla electrica' (90), 21/08 T 'Falla eléctrica' (115), 21/08 N 'falla electrica' (95) |
| R09-TRZ-01-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 | — | TRZ-01 | El motivo 'mantenimiento programado' se repite 4 veces en la semana en la misma línea. | 'Mantenimiento programado' en 17/08 N (30), 18/08 T (45), 19/08 T (15), 19/08 N (30) |
| R09-EXT-02-2026-W35 | R09 | Alta | 2026-08-24..2026-08-28 | — | EXT-02 | El motivo 'falla electrica' se repite 7 veces en la semana en la misma línea. | 24/08 M (35), 25/08 N (85), 26/08 T (110), 26/08 N (145), 27/08 M (150), 27/08 N (85), 28/08 M (180) |
| R03-EXT-02-2026-08-07-Mañana | R03 | Media | 2026-08-07 | Mañana | EXT-02 | Parada registrada sin motivo cargado. | OF-4138: Tiempo_Parada_min = 20, Motivo_Parada = "" (vacío) |
| R03-EXT-02-2026-08-19-Tarde | R03 | Media | 2026-08-19 | Tarde | EXT-02 | Motivo 'Otros' sin Observaciones que lo expliquen. | OF-4213: Motivo_Parada = "Otros", Tiempo_Parada_min = 15, Observaciones = "" (vacío) |
| R05-TRZ-01-2026-08-21-Tarde | R05 | Media | 2026-08-21 | Tarde | TRZ-01 | Cant_Producida igual a 0 con tiempo productivo mayor a 60 minutos. | OF-4232: Cant_Producida = 0, Tiempo_Productivo_min = 480.0 |
| R08a-EXT-02-2026-08-05 | R08a | Media | 2026-08-05 | — | EXT-02 | 3 paradas No Planificada en la misma línea y fecha. | M 'Falla electrica' (65), T 'Falta de insumo' (120), N 'Falla electrica' (165) |
| R08a-EXT-01-2026-08-06 | R08a | Media | 2026-08-06 | — | EXT-01 | 3 paradas No Planificada en la misma línea y fecha. | M 'Ajuste de calidad' (45), T 'Ajuste de calidad' (45), N 'Falla mecanica' (45) |
| R08a-TRZ-01-2026-08-06 | R08a | Media | 2026-08-06 | — | TRZ-01 | 3 paradas No Planificada en la misma línea y fecha. | M 'Falla mecanica' (35), T 'Falla mecanica' (20), N 'Falla mecanica' (60) |
| R08a-TRZ-01-2026-08-07 | R08a | Media | 2026-08-07 | — | TRZ-01 | 3 paradas No Planificada en la misma línea y fecha. | M 'Falta de insumo' (20), T 'Falta de insumo' (20), N 'Falla mecanica' (45) |
| R08a-TRZ-01-2026-08-11 | R08a | Media | 2026-08-11 | — | TRZ-01 | 3 paradas No Planificada en la misma línea y fecha. | M 'Ajuste de calidad' (45), T 'Falta de insumo' (95), N 'Ajuste de calidad' (30) |
| R08a-EXT-02-2026-08-12 | R08a | Media | 2026-08-12 | — | EXT-02 | 3 paradas No Planificada en la misma línea y fecha. | M 'falla electrica' (50), T 'Ajuste de calidad' (20), N 'Falla electrica' (100) |
| R08a-EXT-02-2026-08-13 | R08a | Media | 2026-08-13 | — | EXT-02 | 3 paradas No Planificada en la misma línea y fecha. | M 'Falla electrica' (140), T 'Falla eléctrica' (80), N 'Falta de insumo' (30) |
| R08a-EXT-02-2026-08-20 | R08a | Media | 2026-08-20 | — | EXT-02 | 3 paradas No Planificada en la misma línea y fecha. | M 'Ajuste de calidad' (45), T 'Ajuste de calidad' (15), N 'Falla electrica' (90) |
| R08a-EXT-02-2026-08-21 | R08a | Media | 2026-08-21 | — | EXT-02 | 3 paradas No Planificada en la misma línea y fecha. | M 'Ajuste de calidad' (60), T 'Falla eléctrica' (115), N 'falla electrica' (95) |
| R08b-EXT-01-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-01 | Parada acumulada del día superior a 120 minutos. | 120 + 0 + 45 = 165 min |
| R08b-EXT-02-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 85 + 0 + 65 = 150 min |
| R08b-EXT-02-2026-08-04 | R08b | Media | 2026-08-04 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 80 + 45 + 50 = 175 min |
| R08b-EXT-02-2026-08-05 | R08b | Media | 2026-08-05 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 65 + 120 + 165 = 350 min |
| R08b-TRZ-01-2026-08-05 | R08b | Media | 2026-08-05 | — | TRZ-01 | Parada acumulada del día superior a 120 minutos. | 0 + 90 + 110 = 200 min |
| R08b-EXT-01-2026-08-06 | R08b | Media | 2026-08-06 | — | EXT-01 | Parada acumulada del día superior a 120 minutos. | 45 + 45 + 45 = 135 min |
| R08b-EXT-02-2026-08-11 | R08b | Media | 2026-08-11 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 45 + 45 + 80 = 170 min |
| R08b-TRZ-01-2026-08-11 | R08b | Media | 2026-08-11 | — | TRZ-01 | Parada acumulada del día superior a 120 minutos. | 45 + 95 + 30 = 170 min |
| R08b-EXT-02-2026-08-12 | R08b | Media | 2026-08-12 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 50 + 20 + 100 = 170 min |
| R08b-EXT-02-2026-08-13 | R08b | Media | 2026-08-13 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 140 + 80 + 30 = 250 min |
| R08b-EXT-02-2026-08-14 | R08b | Media | 2026-08-14 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 120 + 130 + 0 = 250 min |
| R08b-TRZ-01-2026-08-14 | R08b | Media | 2026-08-14 | — | TRZ-01 | Parada acumulada del día superior a 120 minutos. | 60 + 95 + 45 = 200 min |
| R08b-EXT-02-2026-08-17 | R08b | Media | 2026-08-17 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 50 + 0 + 100 = 150 min |
| R08b-EXT-01-2026-08-19 | R08b | Media | 2026-08-19 | — | EXT-01 | Parada acumulada del día superior a 120 minutos. | 0 + 80 + 65 = 145 min |
| R08b-EXT-02-2026-08-20 | R08b | Media | 2026-08-20 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 45 + 15 + 90 = 150 min |
| R08b-EXT-02-2026-08-21 | R08b | Media | 2026-08-21 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 60 + 115 + 95 = 270 min |
| R08b-EXT-02-2026-08-25 | R08b | Media | 2026-08-25 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 20 + 70 + 85 = 175 min |
| R08b-EXT-01-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-01 | Parada acumulada del día superior a 120 minutos. | 50 + 60 + 55 = 165 min |
| R08b-EXT-02-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 0 + 110 + 145 = 255 min |
| R08b-TRZ-01-2026-08-26 | R08b | Media | 2026-08-26 | — | TRZ-01 | Parada acumulada del día superior a 120 minutos. | 45 + 90 + 0 = 135 min |
| R08b-EXT-02-2026-08-27 | R08b | Media | 2026-08-27 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 150 + 15 + 85 = 250 min |
| R08b-EXT-02-2026-08-28 | R08b | Media | 2026-08-28 | — | EXT-02 | Parada acumulada del día superior a 120 minutos. | 180 + 0 + 20 = 200 min |
| R08b-TRZ-01-2026-08-28 | R08b | Media | 2026-08-28 | — | TRZ-01 | Parada acumulada del día superior a 120 minutos. | 0 + 75 + 60 = 135 min |
| R12-EXT-01-2026-08-03-Tarde | R12 | Media | 2026-08-03 | Tarde | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4104: Estado_Lote = "Abierto"; 19 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4114: Estado_Lote = "Abierto"; 18 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4117: Estado_Lote = "Abierto"; 18 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4115: Estado_Lote = "Abierto"; 18 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4118: Estado_Lote = "Abierto"; 18 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-06-Mañana | R12 | Media | 2026-08-06 | Mañana | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4130: Estado_Lote = "Abierto"; 16 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-06-Tarde | R12 | Media | 2026-08-06 | Tarde | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4133: Estado_Lote = "Abierto"; 16 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-07-Tarde | R12 | Media | 2026-08-07 | Tarde | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4140: Estado_Lote = "Abierto"; 15 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-07-Noche | R12 | Media | 2026-08-07 | Noche | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4143: Estado_Lote = "Abierto"; 15 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-07-Mañana | R12 | Media | 2026-08-07 | Mañana | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4139: Estado_Lote = "Abierto"; 15 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-10-Mañana | R12 | Media | 2026-08-10 | Mañana | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4146: Estado_Lote = "Abierto"; 14 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-11-Mañana | R12 | Media | 2026-08-11 | Mañana | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4155: Estado_Lote = "Abierto"; 13 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-12-Tarde | R12 | Media | 2026-08-12 | Tarde | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4167: Estado_Lote = "Abierto"; 12 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-12-Noche | R12 | Media | 2026-08-12 | Noche | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4171: Estado_Lote = "Abierto"; 12 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-12-Mañana | R12 | Media | 2026-08-12 | Mañana | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4166: Estado_Lote = "Abierto"; 12 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-13-Mañana | R12 | Media | 2026-08-13 | Mañana | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4173: Estado_Lote = "Abierto"; 11 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-13-Noche | R12 | Media | 2026-08-13 | Noche | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4179: Estado_Lote = "Abierto"; 11 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-13-Tarde | R12 | Media | 2026-08-13 | Tarde | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4178: Estado_Lote = "Abierto"; 11 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-14-Noche | R12 | Media | 2026-08-14 | Noche | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4190: Estado_Lote = "Abierto"; 10 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-17-Noche | R12 | Media | 2026-08-17 | Noche | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4198: Estado_Lote = "Abierto"; 9 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4201: Estado_Lote = "Abierto"; 8 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4204: Estado_Lote = "Abierto"; 8 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4202: Estado_Lote = "Abierto"; 8 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4205: Estado_Lote = "Abierto"; 8 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-18-Noche | R12 | Media | 2026-08-18 | Noche | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4208: Estado_Lote = "Abierto"; 8 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-19-Tarde | R12 | Media | 2026-08-19 | Tarde | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4213: Estado_Lote = "Abierto"; 7 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-19-Mañana | R12 | Media | 2026-08-19 | Mañana | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4211: Estado_Lote = "Abierto"; 7 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-19-Noche | R12 | Media | 2026-08-19 | Noche | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4217: Estado_Lote = "Abierto"; 7 días hábiles al 2026-08-30 |
| R12-EXT-01-2026-08-20-Mañana | R12 | Media | 2026-08-20 | Mañana | EXT-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4218: Estado_Lote = "Abierto"; 6 días hábiles al 2026-08-30 |
| R12-EXT-02-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | EXT-02 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4225: Estado_Lote = "Abierto"; 6 días hábiles al 2026-08-30 |
| R12-TRZ-01-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | TRZ-01 | Lote abierto con más de 5 días hábiles hasta la fecha de corte. | OF-4226: Estado_Lote = "Abierto"; 6 días hábiles al 2026-08-30 |
| R11-EXT-01-Mañana | R11 | Baja | 2026-08-03..2026-08-30 | Mañana | EXT-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 64.6 (OP-106, 03/08) vs máx 90.6 (OP-103, 11/08) = 26.0 puntos |
| R11-EXT-01-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | EXT-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 68.1 (OP-101, 19/08) vs máx 88.4 (OP-102, 25/08) = 20.3 puntos |
| R11-EXT-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 62.0 (OP-101, 19/08) vs máx 92.5 (OP-106, 07/08) = 30.5 puntos |
| R11-EXT-02-Mañana | R11 | Baja | 2026-08-03..2026-08-30 | Mañana | EXT-02 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 44.7 (OP-104, 28/08) vs máx 91.6 (OP-101, 19/08) = 46.9 puntos |
| R11-EXT-02-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | EXT-02 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 55.5 (OP-104, 26/08) vs máx 92.6 (OP-106, 24/08) = 37.1 puntos |
| R11-EXT-02-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-02 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 50.1 (OP-103, 05/08) vs máx entre legajos distintos 85.2 (OP-105, 19/08) = 35.1 puntos |
| R11-TRZ-01-Mañana | R11 | Baja | 2026-08-03..2026-08-30 | Mañana | TRZ-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 66.6 (OP-104, 25/08) vs máx 90.0 (OP-103, 17/08) = 23.4 puntos |
| R11-TRZ-01-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | TRZ-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 62.9 (OP-104, 17/08) vs máx 93.3 (OP-103, 27/08) = 30.4 puntos |
| R11-TRZ-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | TRZ-01 | Diferencia de OEE_pct mayor a 10 puntos entre operarios distintos. | mín 62.8 (OP-105, 05/08) vs máx 93.5 (OP-106, 12/08) = 30.7 puntos |
| R13-TRZ-02-2026-08-29-Tarde | R13 | Baja | 2026-08-29 | Tarde | TRZ-02 | Motivo_Parada fuera del catálogo cerrado tras normalizar. | OF-4281: Motivo_Parada = "aa", Tiempo_Parada_min = 60 |
| R13-TRZ-03-2026-08-30-Noche | R13 | Baja | 2026-08-30 | Noche | TRZ-03 | Motivo_Parada fuera del catálogo cerrado tras normalizar. | OF-4282: Motivo_Parada = "x", Tiempo_Parada_min = 60 |
