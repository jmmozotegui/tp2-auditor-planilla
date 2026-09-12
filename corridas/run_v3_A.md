# Corrida de auditoría — planilla de producción

- Fecha y hora de la corrida: 2026-09-12 17:24:39 UTC
- Fecha de corte usada: 2026-08-30 (fecha más reciente de la columna Fecha)
- Filas analizadas: 182
- Filas ignoradas por corte: 0

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
      "descripcion": "Hora_Fin anterior o igual a Hora_Inicio en un turno que no es Noche.",
      "evidencia": "Turno = \"Tarde\", Hora_Inicio = 22:01, Hora_Fin = 06:01, OF_Lote = OF-4281",
      "accion": "Verificar con el supervisor el horario real del turno y corregir Hora_Inicio/Hora_Fin o el Turno cargado."
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
      "descripcion": "Campo obligatorio vacio: Hora_Fin.",
      "evidencia": "Hora_Fin = \"\" (vacio); OF_Lote = OF-4115",
      "accion": "Completar el campo faltante con el dato del parte de turno."
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
      "descripcion": "Campo obligatorio vacio: Operario.",
      "evidencia": "Operario = \"\" (vacio); OF_Lote = OF-4159",
      "accion": "Completar el campo faltante con el dato del parte de turno."
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
      "descripcion": "El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma linea.",
      "evidencia": "6 ocurrencias tras normalizar: 'Falla electrica' (3), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-03, 2026-08-04, 2026-08-05, 2026-08-06",
      "accion": "Investigar la causa raiz de la recurrencia de \"falla electrica\" en EXT-02."
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
      "descripcion": "El motivo de parada 'falla mecanica' se repite 7 veces en la semana en la misma linea.",
      "evidencia": "7 ocurrencias tras normalizar: 'Falla mecanica' (7); fechas: 2026-08-03, 2026-08-04, 2026-08-06, 2026-08-07",
      "accion": "Investigar la causa raiz de la recurrencia de \"falla mecanica\" en TRZ-01."
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
      "descripcion": "El motivo de parada 'falta de insumo' se repite 5 veces en la semana en la misma linea.",
      "evidencia": "5 ocurrencias tras normalizar: 'Falta de insumo' (5); fechas: 2026-08-10, 2026-08-12, 2026-08-13, 2026-08-14",
      "accion": "Investigar la causa raiz de la recurrencia de \"falta de insumo\" en EXT-01."
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
      "descripcion": "El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma linea.",
      "evidencia": "5 ocurrencias tras normalizar: 'Falla electrica' (2), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-12, 2026-08-13, 2026-08-14",
      "accion": "Investigar la causa raiz de la recurrencia de \"falla electrica\" en EXT-02."
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
      "descripcion": "El motivo de parada 'falla electrica' se repite 4 veces en la semana en la misma linea.",
      "evidencia": "4 ocurrencias tras normalizar: 'Falla electrica' (1), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-17, 2026-08-20, 2026-08-21",
      "accion": "Investigar la causa raiz de la recurrencia de \"falla electrica\" en EXT-02."
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
      "descripcion": "El motivo de parada 'mantenimiento programado' se repite 4 veces en la semana en la misma linea.",
      "evidencia": "4 ocurrencias tras normalizar: 'Mantenimiento programado' (4); fechas: 2026-08-17, 2026-08-18, 2026-08-19",
      "accion": "Investigar la causa raiz de la recurrencia de \"mantenimiento programado\" en TRZ-01."
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
      "descripcion": "El motivo de parada 'falla electrica' se repite 7 veces en la semana en la misma linea.",
      "evidencia": "7 ocurrencias tras normalizar: 'Falla electrica' (3), 'Falla eléctrica' (1), 'falla electrica' (3); fechas: 2026-08-24, 2026-08-25, 2026-08-26, 2026-08-27, 2026-08-28",
      "accion": "Investigar la causa raiz de la recurrencia de \"falla electrica\" en EXT-02."
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
      "evidencia": "Tiempo_Parada_min = 20, Motivo_Parada = \"\" (vacio), OF_Lote = OF-4138",
      "accion": "Solicitar al supervisor del turno que complete el motivo de parada."
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
      "descripcion": "Parada con motivo \"Otros\" y sin observaciones que la expliquen.",
      "evidencia": "Motivo_Parada = \"Otros\", Tiempo_Parada_min = 15, Observaciones = \"\" (vacio), OF_Lote = OF-4213",
      "accion": "Pedir al supervisor que detalle en Observaciones a que corresponde la parada \"Otros\"."
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
      "descripcion": "Produccion cero con tiempo productivo mayor a 60 minutos.",
      "evidencia": "Cant_Producida = 0, Tiempo_Productivo_min = 480, Tiempo_Parada_min = 0, Observaciones = \"Linea detenida por espera de material\"",
      "accion": "Verificar si la produccion no se cargo o si el tiempo debio imputarse como parada."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Falla electrica (65 min); Tarde: Falta de insumo (120 min); Noche: Falla electrica (165 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Ajuste de calidad (45 min); Tarde: Ajuste de calidad (45 min); Noche: Falla mecanica (45 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Falla mecanica (35 min); Tarde: Falla mecanica (20 min); Noche: Falla mecanica (60 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Falta de insumo (20 min); Tarde: Falta de insumo (20 min); Noche: Falla mecanica (45 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Ajuste de calidad (45 min); Tarde: Falta de insumo (95 min); Noche: Ajuste de calidad (30 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: falla electrica (50 min); Tarde: Ajuste de calidad (20 min); Noche: Falla electrica (100 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Falla electrica (140 min); Tarde: Falla eléctrica (80 min); Noche: Falta de insumo (30 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Ajuste de calidad (45 min); Tarde: Ajuste de calidad (15 min); Noche: Falla electrica (90 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "3 paradas No Planificadas en la misma linea y fecha.",
      "evidencia": "3 filas con Tipo_Parada = \"No Planificada\" — Mañana: Ajuste de calidad (60 min); Tarde: Falla eléctrica (115 min); Noche: falla electrica (95 min)",
      "accion": "Revisar con mantenimiento la concentracion de paradas no planificadas de ese dia en la linea."
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
      "descripcion": "Tiempo de parada acumulado de 165 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 165 min — Mañana: 120 min (Mantenimiento programado); Noche: 45 min (Mantenimiento programado)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 150 min — Mañana: 85 min (falla electrica); Noche: 65 min (Ajuste de calidad)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 175 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 175 min — Mañana: 80 min (Falla electrica); Tarde: 45 min (Mantenimiento programado); Noche: 50 min (Falla eléctrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 350 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 350 min — Mañana: 65 min (Falla electrica); Tarde: 120 min (Falta de insumo); Noche: 165 min (Falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 200 min — Tarde: 90 min (Cambio de formato); Noche: 110 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 135 min — Mañana: 45 min (Ajuste de calidad); Tarde: 45 min (Ajuste de calidad); Noche: 45 min (Falla mecanica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 170 min — Mañana: 45 min (Mantenimiento programado); Tarde: 45 min (Mantenimiento programado); Noche: 80 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 170 min — Mañana: 45 min (Ajuste de calidad); Tarde: 95 min (Falta de insumo); Noche: 30 min (Ajuste de calidad)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 170 min — Mañana: 50 min (falla electrica); Tarde: 20 min (Ajuste de calidad); Noche: 100 min (Falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 250 min — Mañana: 140 min (Falla electrica); Tarde: 80 min (Falla eléctrica); Noche: 30 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 250 min — Mañana: 120 min (Falta de insumo); Tarde: 130 min (falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 200 min — Mañana: 60 min (Mantenimiento programado); Tarde: 95 min (Mantenimiento programado); Noche: 45 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 150 min — Mañana: 50 min (Mantenimiento programado); Noche: 100 min (falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 145 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 145 min — Tarde: 80 min (Falta de insumo); Noche: 65 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 150 min — Mañana: 45 min (Ajuste de calidad); Tarde: 15 min (Ajuste de calidad); Noche: 90 min (Falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 270 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 270 min — Mañana: 60 min (Ajuste de calidad); Tarde: 115 min (Falla eléctrica); Noche: 95 min (falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 175 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 175 min — Mañana: 20 min (Falla mecanica); Tarde: 70 min (Mantenimiento programado); Noche: 85 min (Falla eléctrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 165 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 165 min — Mañana: 50 min (Cambio de formato); Tarde: 60 min (Falta de insumo); Noche: 55 min (Mantenimiento programado)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 255 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 255 min — Tarde: 110 min (falla electrica); Noche: 145 min (falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 135 min — Mañana: 45 min (Cambio de formato); Tarde: 90 min (Cambio de formato)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 250 min — Mañana: 150 min (Falla electrica); Tarde: 15 min (Cambio de formato); Noche: 85 min (falla electrica)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 200 min — Mañana: 180 min (Falla electrica); Noche: 20 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min.",
      "evidencia": "Suma Tiempo_Parada_min = 135 min — Tarde: 75 min (Cambio de formato); Noche: 60 min (Falta de insumo)",
      "accion": "Revisar el detalle de paradas del dia en esa linea y validar la imputacion de minutos."
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
      "descripcion": "Lote abierto hace 19 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4104, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-03, corte = 2026-08-30 -> 19 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 18 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4114, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 18 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4117, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 18 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4115, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 18 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4118, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 16 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4130, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-06, corte = 2026-08-30 -> 16 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 16 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4133, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-06, corte = 2026-08-30 -> 16 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 15 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4140, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 15 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4143, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 15 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4139, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 14 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4146, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-10, corte = 2026-08-30 -> 14 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 13 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4155, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-11, corte = 2026-08-30 -> 13 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 12 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4167, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 12 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4171, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 12 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4166, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 11 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4173, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 11 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4179, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 11 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4178, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 10 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4190, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-14, corte = 2026-08-30 -> 10 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 9 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4198, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-17, corte = 2026-08-30 -> 9 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 8 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4201, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 8 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4204, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 8 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4202, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 8 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4205, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 8 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4208, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 7 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4213, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 7 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4211, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 7 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4217, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 6 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4218, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 6 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4225, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
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
      "descripcion": "Lote abierto hace 6 dias habiles posteriores a la fecha de la fila.",
      "evidencia": "Estado_Lote = \"Abierto\", OF_Lote = OF-4226, Fecha_Cierre_Lote = \"\" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores",
      "accion": "Cerrar el lote en el sistema o justificar por que sigue abierto."
    },
    {
      "id": "R11-EXT-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia de 17.5 puntos de OEE entre operarios en EXT-01 turno Noche.",
      "evidencia": "OP-102 = 83.9% vs OP-104 = 66.5% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 73.5% (3 turnos); OP-102: 83.9% (4 turnos); OP-103: 78.3% (4 turnos); OP-104: 66.5% (2 turnos); OP-105: 80.8% (4 turnos); OP-106: 81.5% (2 turnos)",
      "accion": "Comparar metodo de trabajo de OP-102 y OP-104 en EXT-01 turno Noche y verificar que las filas esten bien imputadas."
    },
    {
      "id": "R11-EXT-02-Mañana",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 26.3 puntos de OEE entre operarios en EXT-02 turno Mañana.",
      "evidencia": "OP-103 = 83.6% vs OP-104 = 57.3% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 74.6% (6 turnos); OP-103: 83.6% (2 turnos); OP-104: 57.3% (3 turnos); OP-105: 76.7% (4 turnos); OP-106: 70.8% (4 turnos)",
      "accion": "Comparar metodo de trabajo de OP-103 y OP-104 en EXT-02 turno Mañana y verificar que las filas esten bien imputadas."
    },
    {
      "id": "R11-EXT-02-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 12.3 puntos de OEE entre operarios en EXT-02 turno Tarde.",
      "evidencia": "OP-106 = 84.3% vs OP-102 = 72.0% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-102: 72.0% (4 turnos); OP-103: 79.0% (2 turnos); OP-104: 73.1% (4 turnos); OP-105: 72.1% (2 turnos); OP-106: 84.3% (6 turnos)",
      "accion": "Comparar metodo de trabajo de OP-106 y OP-102 en EXT-02 turno Tarde y verificar que las filas esten bien imputadas."
    },
    {
      "id": "R11-EXT-02-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 20.6 puntos de OEE entre operarios en EXT-02 turno Noche.",
      "evidencia": "OP-105 = 84.9% vs OP-106 = 64.3% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 72.3% (4 turnos); OP-102: 70.8% (4 turnos); OP-103: 70.1% (6 turnos); OP-104: 68.0% (2 turnos); OP-105: 84.9% (2 turnos); OP-106: 64.3% (2 turnos)",
      "accion": "Comparar metodo de trabajo de OP-105 y OP-106 en EXT-02 turno Noche y verificar que las filas esten bien imputadas."
    },
    {
      "id": "R11-TRZ-01-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de 16.3 puntos de OEE entre operarios en TRZ-01 turno Tarde.",
      "evidencia": "OP-103 = 85.8% vs OP-104 = 69.5% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 73.9% (3 turnos); OP-103: 85.8% (3 turnos); OP-104: 69.5% (4 turnos); OP-105: 76.6% (5 turnos); OP-106: 76.5% (2 turnos)",
      "accion": "Comparar metodo de trabajo de OP-103 y OP-104 en TRZ-01 turno Tarde y verificar que las filas esten bien imputadas."
    },
    {
      "id": "R11-TRZ-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado por periodo",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de 15.1 puntos de OEE entre operarios en TRZ-01 turno Noche.",
      "evidencia": "OP-106 = 83.7% vs OP-105 = 68.7% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 75.5% (5 turnos); OP-102: 76.2% (2 turnos); OP-103: 80.0% (3 turnos); OP-104: 72.0% (3 turnos); OP-105: 68.7% (3 turnos); OP-106: 83.7% (4 turnos)",
      "accion": "Comparar metodo de trabajo de OP-106 y OP-105 en TRZ-01 turno Noche y verificar que las filas esten bien imputadas."
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
      "descripcion": "Motivo_Parada fuera del catalogo cerrado.",
      "evidencia": "Motivo_Parada = \"aa\" (normalizado: \"aa\"), Tiempo_Parada_min = 60, OF_Lote = OF-4281",
      "accion": "Reemplazar por un valor del catalogo cerrado de motivos de parada."
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
      "descripcion": "Motivo_Parada fuera del catalogo cerrado.",
      "evidencia": "Motivo_Parada = \"x\" (normalizado: \"x\"), Tiempo_Parada_min = 60, OF_Lote = OF-4282",
      "accion": "Reemplazar por un valor del catalogo cerrado de motivos de parada."
    }
  ],
  "metricas": {
    "oee": {
      "umbral_pct": 60,
      "promedio_pct": 76.42,
      "turnos_bajo_umbral": 8,
      "peores_5": [
        {
          "fecha": "2026-08-28",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "oee_pct": 44.7
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-103",
          "oee_pct": 50.1
        },
        {
          "fecha": "2026-08-13",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "oee_pct": 53.6
        },
        {
          "fecha": "2026-08-27",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-101",
          "oee_pct": 54.2
        },
        {
          "fecha": "2026-08-26",
          "turno": "Tarde",
          "linea": "EXT-02",
          "operario": "OP-104",
          "oee_pct": 55.5
        }
      ]
    },
    "cumplimiento_meta": {
      "promedio_pct": 94.73,
      "turnos_no_cumplidos": 119,
      "turnos_criticos": 17,
      "criticos": [
        {
          "fecha": "2026-08-21",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "operario": "OP-105",
          "cumplimiento_pct": 0.0,
          "cant_producida": 0,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-28",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 55.4,
          "cant_producida": 3453,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-103",
          "cumplimiento_pct": 61.7,
          "cant_producida": 5668,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-13",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 66.2,
          "cant_producida": 5207,
          "meta_produccion": 7871
        },
        {
          "fecha": "2026-08-27",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-101",
          "cumplimiento_pct": 67.2,
          "cant_producida": 6175,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-26",
          "turno": "Tarde",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 68.6,
          "cant_producida": 5396,
          "meta_produccion": 7871
        },
        {
          "fecha": "2026-08-17",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 72.9,
          "cant_producida": 4544,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-06",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-106",
          "cumplimiento_pct": 73.3,
          "cant_producida": 6730,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-12",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-103",
          "cumplimiento_pct": 74.9,
          "cant_producida": 5899,
          "meta_produccion": 7871
        },
        {
          "fecha": "2026-08-19",
          "turno": "Noche",
          "linea": "EXT-01",
          "operario": "OP-101",
          "cumplimiento_pct": 76.2,
          "cant_producida": 4751,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-14",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-106",
          "cumplimiento_pct": 76.8,
          "cant_producida": 7050,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-14",
          "turno": "Tarde",
          "linea": "EXT-02",
          "operario": "OP-105",
          "cumplimiento_pct": 77.4,
          "cant_producida": 4821,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "TRZ-01",
          "operario": "OP-105",
          "cumplimiento_pct": 77.5,
          "cant_producida": 7116,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-26",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-102",
          "cumplimiento_pct": 77.6,
          "cant_producida": 4835,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-17",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "operario": "OP-104",
          "cumplimiento_pct": 78.7,
          "cant_producida": 7229,
          "meta_produccion": 9184
        },
        {
          "fecha": "2026-08-03",
          "turno": "Mañana",
          "linea": "EXT-01",
          "operario": "OP-106",
          "cumplimiento_pct": 79.3,
          "cant_producida": 4942,
          "meta_produccion": 6232
        },
        {
          "fecha": "2026-08-04",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-101",
          "cumplimiento_pct": 79.9,
          "cant_producida": 6290,
          "meta_produccion": 7871
        }
      ]
    },
    "calidad": {
      "umbral_pct": 95,
      "promedio_pct": 97.84,
      "por_debajo_umbral": [
        {
          "tipo": "operario",
          "clave": "OP-102",
          "calidad_promedio_pct": 94.5,
          "filas": 29
        }
      ],
      "proyeccion_semana": {
        "acumulado_pct": 97.96,
        "dias_transcurridos": 5,
        "dias_totales": 5,
        "proyectado_pct": 97.96,
        "cumple": true
      },
      "proyeccion_mes": {
        "acumulado_pct": 97.79,
        "dias_transcurridos": 20,
        "dias_totales": 21,
        "proyectado_pct": 97.79,
        "cumple": true
      }
    }
  },
  "reglas_no_evaluables": [
    {
      "regla": "R01",
      "motivo": "No se pudo evaluar la fila 2026-08-04 / Tarde / TRZ-01 (OF-4115): Hora_Fin esta vacia, no hay con que comparar Hora_Inicio. El resto de las filas se evaluo."
    },
    {
      "regla": "R02",
      "motivo": "No se pudo evaluar la fila 2026-08-04 / Tarde / TRZ-01 (OF-4115): Tiempo_Total_min esta vacio, no hay contra que comparar Tiempo_Setup_min + Tiempo_Parada_min. El resto de las filas se evaluo."
    },
    {
      "regla": "R11",
      "motivo": "En TRZ-02 turno Tarde no queda ningun par de operarios con 2 o mas turnos registrados en el periodo: OP-102 (1 turno/s). No hay desempeno sostenido que comparar."
    },
    {
      "regla": "R11",
      "motivo": "En TRZ-03 turno Noche no queda ningun par de operarios con 2 o mas turnos registrados en el periodo: OP-103 (1 turno/s). No hay desempeno sostenido que comparar."
    }
  ],
  "resumen": {
    "hallazgos_alta": 10,
    "hallazgos_media": 66,
    "hallazgos_baja": 8,
    "total_hallazgos": 84
  }
}
```

| ID | Regla | Severidad | Fecha | Turno | Línea | Descripción | Evidencia |
|---|---|---|---|---|---|---|---|
| R01-TRZ-02-2026-08-29-Tarde | R01 | Alta | 2026-08-29 | Tarde | TRZ-02 | Hora_Fin anterior o igual a Hora_Inicio en un turno que no es Noche. | Turno = "Tarde", Hora_Inicio = 22:01, Hora_Fin = 06:01, OF_Lote = OF-4281 |
| R04-TRZ-01-2026-08-04-Tarde | R04 | Alta | 2026-08-04 | Tarde | TRZ-01 | Campo obligatorio vacio: Hora_Fin. | Hora_Fin = "" (vacio); OF_Lote = OF-4115 |
| R04-EXT-02-2026-08-11-Tarde | R04 | Alta | 2026-08-11 | Tarde | EXT-02 | Campo obligatorio vacio: Operario. | Operario = "" (vacio); OF_Lote = OF-4159 |
| R09-EXT-02-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma linea. | 6 ocurrencias tras normalizar: 'Falla electrica' (3), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-03, 2026-08-04, 2026-08-05, 2026-08-06 |
| R09-TRZ-01-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | TRZ-01 | El motivo de parada 'falla mecanica' se repite 7 veces en la semana en la misma linea. | 7 ocurrencias tras normalizar: 'Falla mecanica' (7); fechas: 2026-08-03, 2026-08-04, 2026-08-06, 2026-08-07 |
| R09-EXT-01-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-01 | El motivo de parada 'falta de insumo' se repite 5 veces en la semana en la misma linea. | 5 ocurrencias tras normalizar: 'Falta de insumo' (5); fechas: 2026-08-10, 2026-08-12, 2026-08-13, 2026-08-14 |
| R09-EXT-02-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma linea. | 5 ocurrencias tras normalizar: 'Falla electrica' (2), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-12, 2026-08-13, 2026-08-14 |
| R09-EXT-02-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 4 veces en la semana en la misma linea. | 4 ocurrencias tras normalizar: 'Falla electrica' (1), 'Falla eléctrica' (1), 'falla electrica' (2); fechas: 2026-08-17, 2026-08-20, 2026-08-21 |
| R09-TRZ-01-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 | — | TRZ-01 | El motivo de parada 'mantenimiento programado' se repite 4 veces en la semana en la misma linea. | 4 ocurrencias tras normalizar: 'Mantenimiento programado' (4); fechas: 2026-08-17, 2026-08-18, 2026-08-19 |
| R09-EXT-02-2026-W35 | R09 | Alta | 2026-08-24..2026-08-28 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 7 veces en la semana en la misma linea. | 7 ocurrencias tras normalizar: 'Falla electrica' (3), 'Falla eléctrica' (1), 'falla electrica' (3); fechas: 2026-08-24, 2026-08-25, 2026-08-26, 2026-08-27, 2026-08-28 |
| R03-EXT-02-2026-08-07-Mañana | R03 | Media | 2026-08-07 | Mañana | EXT-02 | Parada registrada sin motivo cargado. | Tiempo_Parada_min = 20, Motivo_Parada = "" (vacio), OF_Lote = OF-4138 |
| R03-EXT-02-2026-08-19-Tarde | R03 | Media | 2026-08-19 | Tarde | EXT-02 | Parada con motivo "Otros" y sin observaciones que la expliquen. | Motivo_Parada = "Otros", Tiempo_Parada_min = 15, Observaciones = "" (vacio), OF_Lote = OF-4213 |
| R05-TRZ-01-2026-08-21-Tarde | R05 | Media | 2026-08-21 | Tarde | TRZ-01 | Produccion cero con tiempo productivo mayor a 60 minutos. | Cant_Producida = 0, Tiempo_Productivo_min = 480, Tiempo_Parada_min = 0, Observaciones = "Linea detenida por espera de material" |
| R08a-EXT-02-2026-08-05 | R08a | Media | 2026-08-05 | — | EXT-02 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Falla electrica (65 min); Tarde: Falta de insumo (120 min); Noche: Falla electrica (165 min) |
| R08a-EXT-01-2026-08-06 | R08a | Media | 2026-08-06 | — | EXT-01 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Ajuste de calidad (45 min); Tarde: Ajuste de calidad (45 min); Noche: Falla mecanica (45 min) |
| R08a-TRZ-01-2026-08-06 | R08a | Media | 2026-08-06 | — | TRZ-01 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Falla mecanica (35 min); Tarde: Falla mecanica (20 min); Noche: Falla mecanica (60 min) |
| R08a-TRZ-01-2026-08-07 | R08a | Media | 2026-08-07 | — | TRZ-01 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Falta de insumo (20 min); Tarde: Falta de insumo (20 min); Noche: Falla mecanica (45 min) |
| R08a-TRZ-01-2026-08-11 | R08a | Media | 2026-08-11 | — | TRZ-01 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Ajuste de calidad (45 min); Tarde: Falta de insumo (95 min); Noche: Ajuste de calidad (30 min) |
| R08a-EXT-02-2026-08-12 | R08a | Media | 2026-08-12 | — | EXT-02 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: falla electrica (50 min); Tarde: Ajuste de calidad (20 min); Noche: Falla electrica (100 min) |
| R08a-EXT-02-2026-08-13 | R08a | Media | 2026-08-13 | — | EXT-02 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Falla electrica (140 min); Tarde: Falla eléctrica (80 min); Noche: Falta de insumo (30 min) |
| R08a-EXT-02-2026-08-20 | R08a | Media | 2026-08-20 | — | EXT-02 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Ajuste de calidad (45 min); Tarde: Ajuste de calidad (15 min); Noche: Falla electrica (90 min) |
| R08a-EXT-02-2026-08-21 | R08a | Media | 2026-08-21 | — | EXT-02 | 3 paradas No Planificadas en la misma linea y fecha. | 3 filas con Tipo_Parada = "No Planificada" — Mañana: Ajuste de calidad (60 min); Tarde: Falla eléctrica (115 min); Noche: falla electrica (95 min) |
| R08b-EXT-01-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-01 | Tiempo de parada acumulado de 165 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 165 min — Mañana: 120 min (Mantenimiento programado); Noche: 45 min (Mantenimiento programado) |
| R08b-EXT-02-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-02 | Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 150 min — Mañana: 85 min (falla electrica); Noche: 65 min (Ajuste de calidad) |
| R08b-EXT-02-2026-08-04 | R08b | Media | 2026-08-04 | — | EXT-02 | Tiempo de parada acumulado de 175 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 175 min — Mañana: 80 min (Falla electrica); Tarde: 45 min (Mantenimiento programado); Noche: 50 min (Falla eléctrica) |
| R08b-EXT-02-2026-08-05 | R08b | Media | 2026-08-05 | — | EXT-02 | Tiempo de parada acumulado de 350 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 350 min — Mañana: 65 min (Falla electrica); Tarde: 120 min (Falta de insumo); Noche: 165 min (Falla electrica) |
| R08b-TRZ-01-2026-08-05 | R08b | Media | 2026-08-05 | — | TRZ-01 | Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 200 min — Tarde: 90 min (Cambio de formato); Noche: 110 min (Falta de insumo) |
| R08b-EXT-01-2026-08-06 | R08b | Media | 2026-08-06 | — | EXT-01 | Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 135 min — Mañana: 45 min (Ajuste de calidad); Tarde: 45 min (Ajuste de calidad); Noche: 45 min (Falla mecanica) |
| R08b-EXT-02-2026-08-11 | R08b | Media | 2026-08-11 | — | EXT-02 | Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 170 min — Mañana: 45 min (Mantenimiento programado); Tarde: 45 min (Mantenimiento programado); Noche: 80 min (Falta de insumo) |
| R08b-TRZ-01-2026-08-11 | R08b | Media | 2026-08-11 | — | TRZ-01 | Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 170 min — Mañana: 45 min (Ajuste de calidad); Tarde: 95 min (Falta de insumo); Noche: 30 min (Ajuste de calidad) |
| R08b-EXT-02-2026-08-12 | R08b | Media | 2026-08-12 | — | EXT-02 | Tiempo de parada acumulado de 170 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 170 min — Mañana: 50 min (falla electrica); Tarde: 20 min (Ajuste de calidad); Noche: 100 min (Falla electrica) |
| R08b-EXT-02-2026-08-13 | R08b | Media | 2026-08-13 | — | EXT-02 | Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 250 min — Mañana: 140 min (Falla electrica); Tarde: 80 min (Falla eléctrica); Noche: 30 min (Falta de insumo) |
| R08b-EXT-02-2026-08-14 | R08b | Media | 2026-08-14 | — | EXT-02 | Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 250 min — Mañana: 120 min (Falta de insumo); Tarde: 130 min (falla electrica) |
| R08b-TRZ-01-2026-08-14 | R08b | Media | 2026-08-14 | — | TRZ-01 | Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 200 min — Mañana: 60 min (Mantenimiento programado); Tarde: 95 min (Mantenimiento programado); Noche: 45 min (Falta de insumo) |
| R08b-EXT-02-2026-08-17 | R08b | Media | 2026-08-17 | — | EXT-02 | Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 150 min — Mañana: 50 min (Mantenimiento programado); Noche: 100 min (falla electrica) |
| R08b-EXT-01-2026-08-19 | R08b | Media | 2026-08-19 | — | EXT-01 | Tiempo de parada acumulado de 145 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 145 min — Tarde: 80 min (Falta de insumo); Noche: 65 min (Falta de insumo) |
| R08b-EXT-02-2026-08-20 | R08b | Media | 2026-08-20 | — | EXT-02 | Tiempo de parada acumulado de 150 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 150 min — Mañana: 45 min (Ajuste de calidad); Tarde: 15 min (Ajuste de calidad); Noche: 90 min (Falla electrica) |
| R08b-EXT-02-2026-08-21 | R08b | Media | 2026-08-21 | — | EXT-02 | Tiempo de parada acumulado de 270 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 270 min — Mañana: 60 min (Ajuste de calidad); Tarde: 115 min (Falla eléctrica); Noche: 95 min (falla electrica) |
| R08b-EXT-02-2026-08-25 | R08b | Media | 2026-08-25 | — | EXT-02 | Tiempo de parada acumulado de 175 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 175 min — Mañana: 20 min (Falla mecanica); Tarde: 70 min (Mantenimiento programado); Noche: 85 min (Falla eléctrica) |
| R08b-EXT-01-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-01 | Tiempo de parada acumulado de 165 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 165 min — Mañana: 50 min (Cambio de formato); Tarde: 60 min (Falta de insumo); Noche: 55 min (Mantenimiento programado) |
| R08b-EXT-02-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-02 | Tiempo de parada acumulado de 255 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 255 min — Tarde: 110 min (falla electrica); Noche: 145 min (falla electrica) |
| R08b-TRZ-01-2026-08-26 | R08b | Media | 2026-08-26 | — | TRZ-01 | Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 135 min — Mañana: 45 min (Cambio de formato); Tarde: 90 min (Cambio de formato) |
| R08b-EXT-02-2026-08-27 | R08b | Media | 2026-08-27 | — | EXT-02 | Tiempo de parada acumulado de 250 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 250 min — Mañana: 150 min (Falla electrica); Tarde: 15 min (Cambio de formato); Noche: 85 min (falla electrica) |
| R08b-EXT-02-2026-08-28 | R08b | Media | 2026-08-28 | — | EXT-02 | Tiempo de parada acumulado de 200 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 200 min — Mañana: 180 min (Falla electrica); Noche: 20 min (Falta de insumo) |
| R08b-TRZ-01-2026-08-28 | R08b | Media | 2026-08-28 | — | TRZ-01 | Tiempo de parada acumulado de 135 min en la linea en el dia, sobre un umbral de 120 min. | Suma Tiempo_Parada_min = 135 min — Tarde: 75 min (Cambio de formato); Noche: 60 min (Falta de insumo) |
| R12-EXT-01-2026-08-03-Tarde | R12 | Media | 2026-08-03 | Tarde | EXT-01 | Lote abierto hace 19 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4104, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-03, corte = 2026-08-30 -> 19 dias habiles posteriores |
| R12-EXT-02-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | EXT-02 | Lote abierto hace 18 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4114, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores |
| R12-EXT-02-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | EXT-02 | Lote abierto hace 18 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4117, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores |
| R12-TRZ-01-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | TRZ-01 | Lote abierto hace 18 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4115, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores |
| R12-TRZ-01-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | TRZ-01 | Lote abierto hace 18 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4118, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-04, corte = 2026-08-30 -> 18 dias habiles posteriores |
| R12-TRZ-01-2026-08-06-Mañana | R12 | Media | 2026-08-06 | Mañana | TRZ-01 | Lote abierto hace 16 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4130, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-06, corte = 2026-08-30 -> 16 dias habiles posteriores |
| R12-TRZ-01-2026-08-06-Tarde | R12 | Media | 2026-08-06 | Tarde | TRZ-01 | Lote abierto hace 16 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4133, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-06, corte = 2026-08-30 -> 16 dias habiles posteriores |
| R12-EXT-01-2026-08-07-Tarde | R12 | Media | 2026-08-07 | Tarde | EXT-01 | Lote abierto hace 15 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4140, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores |
| R12-EXT-01-2026-08-07-Noche | R12 | Media | 2026-08-07 | Noche | EXT-01 | Lote abierto hace 15 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4143, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores |
| R12-TRZ-01-2026-08-07-Mañana | R12 | Media | 2026-08-07 | Mañana | TRZ-01 | Lote abierto hace 15 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4139, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-07, corte = 2026-08-30 -> 15 dias habiles posteriores |
| R12-EXT-01-2026-08-10-Mañana | R12 | Media | 2026-08-10 | Mañana | EXT-01 | Lote abierto hace 14 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4146, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-10, corte = 2026-08-30 -> 14 dias habiles posteriores |
| R12-EXT-01-2026-08-11-Mañana | R12 | Media | 2026-08-11 | Mañana | EXT-01 | Lote abierto hace 13 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4155, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-11, corte = 2026-08-30 -> 13 dias habiles posteriores |
| R12-EXT-01-2026-08-12-Tarde | R12 | Media | 2026-08-12 | Tarde | EXT-01 | Lote abierto hace 12 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4167, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores |
| R12-EXT-02-2026-08-12-Noche | R12 | Media | 2026-08-12 | Noche | EXT-02 | Lote abierto hace 12 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4171, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores |
| R12-TRZ-01-2026-08-12-Mañana | R12 | Media | 2026-08-12 | Mañana | TRZ-01 | Lote abierto hace 12 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4166, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-12, corte = 2026-08-30 -> 12 dias habiles posteriores |
| R12-EXT-01-2026-08-13-Mañana | R12 | Media | 2026-08-13 | Mañana | EXT-01 | Lote abierto hace 11 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4173, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores |
| R12-EXT-01-2026-08-13-Noche | R12 | Media | 2026-08-13 | Noche | EXT-01 | Lote abierto hace 11 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4179, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores |
| R12-TRZ-01-2026-08-13-Tarde | R12 | Media | 2026-08-13 | Tarde | TRZ-01 | Lote abierto hace 11 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4178, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-13, corte = 2026-08-30 -> 11 dias habiles posteriores |
| R12-TRZ-01-2026-08-14-Noche | R12 | Media | 2026-08-14 | Noche | TRZ-01 | Lote abierto hace 10 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4190, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-14, corte = 2026-08-30 -> 10 dias habiles posteriores |
| R12-EXT-02-2026-08-17-Noche | R12 | Media | 2026-08-17 | Noche | EXT-02 | Lote abierto hace 9 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4198, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-17, corte = 2026-08-30 -> 9 dias habiles posteriores |
| R12-EXT-02-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | EXT-02 | Lote abierto hace 8 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4201, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores |
| R12-EXT-02-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | EXT-02 | Lote abierto hace 8 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4204, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores |
| R12-TRZ-01-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | TRZ-01 | Lote abierto hace 8 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4202, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores |
| R12-TRZ-01-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | TRZ-01 | Lote abierto hace 8 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4205, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores |
| R12-TRZ-01-2026-08-18-Noche | R12 | Media | 2026-08-18 | Noche | TRZ-01 | Lote abierto hace 8 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4208, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-18, corte = 2026-08-30 -> 8 dias habiles posteriores |
| R12-EXT-02-2026-08-19-Tarde | R12 | Media | 2026-08-19 | Tarde | EXT-02 | Lote abierto hace 7 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4213, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores |
| R12-TRZ-01-2026-08-19-Mañana | R12 | Media | 2026-08-19 | Mañana | TRZ-01 | Lote abierto hace 7 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4211, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores |
| R12-TRZ-01-2026-08-19-Noche | R12 | Media | 2026-08-19 | Noche | TRZ-01 | Lote abierto hace 7 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4217, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-19, corte = 2026-08-30 -> 7 dias habiles posteriores |
| R12-EXT-01-2026-08-20-Mañana | R12 | Media | 2026-08-20 | Mañana | EXT-01 | Lote abierto hace 6 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4218, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores |
| R12-EXT-02-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | EXT-02 | Lote abierto hace 6 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4225, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores |
| R12-TRZ-01-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | TRZ-01 | Lote abierto hace 6 dias habiles posteriores a la fecha de la fila. | Estado_Lote = "Abierto", OF_Lote = OF-4226, Fecha_Cierre_Lote = "" (vacio), Fecha = 2026-08-20, corte = 2026-08-30 -> 6 dias habiles posteriores |
| R11-EXT-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-01 | Diferencia de 17.5 puntos de OEE entre operarios en EXT-01 turno Noche. | OP-102 = 83.9% vs OP-104 = 66.5% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 73.5% (3 turnos); OP-102: 83.9% (4 turnos); OP-103: 78.3% (4 turnos); OP-104: 66.5% (2 turnos); OP-105: 80.8% (4 turnos); OP-106: 81.5% (2 turnos) |
| R11-EXT-02-Mañana | R11 | Baja | 2026-08-03..2026-08-30 | Mañana | EXT-02 | Diferencia de 26.3 puntos de OEE entre operarios en EXT-02 turno Mañana. | OP-103 = 83.6% vs OP-104 = 57.3% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 74.6% (6 turnos); OP-103: 83.6% (2 turnos); OP-104: 57.3% (3 turnos); OP-105: 76.7% (4 turnos); OP-106: 70.8% (4 turnos) |
| R11-EXT-02-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | EXT-02 | Diferencia de 12.3 puntos de OEE entre operarios en EXT-02 turno Tarde. | OP-106 = 84.3% vs OP-102 = 72.0% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-102: 72.0% (4 turnos); OP-103: 79.0% (2 turnos); OP-104: 73.1% (4 turnos); OP-105: 72.1% (2 turnos); OP-106: 84.3% (6 turnos) |
| R11-EXT-02-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-02 | Diferencia de 20.6 puntos de OEE entre operarios en EXT-02 turno Noche. | OP-105 = 84.9% vs OP-106 = 64.3% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 72.3% (4 turnos); OP-102: 70.8% (4 turnos); OP-103: 70.1% (6 turnos); OP-104: 68.0% (2 turnos); OP-105: 84.9% (2 turnos); OP-106: 64.3% (2 turnos) |
| R11-TRZ-01-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | TRZ-01 | Diferencia de 16.3 puntos de OEE entre operarios en TRZ-01 turno Tarde. | OP-103 = 85.8% vs OP-104 = 69.5% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 73.9% (3 turnos); OP-103: 85.8% (3 turnos); OP-104: 69.5% (4 turnos); OP-105: 76.6% (5 turnos); OP-106: 76.5% (2 turnos) |
| R11-TRZ-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | TRZ-01 | Diferencia de 15.1 puntos de OEE entre operarios en TRZ-01 turno Noche. | OP-106 = 83.7% vs OP-105 = 68.7% (promedio simple de sus filas); operarios elegibles con 2+ turnos — OP-101: 75.5% (5 turnos); OP-102: 76.2% (2 turnos); OP-103: 80.0% (3 turnos); OP-104: 72.0% (3 turnos); OP-105: 68.7% (3 turnos); OP-106: 83.7% (4 turnos) |
| R13-TRZ-02-2026-08-29-Tarde | R13 | Baja | 2026-08-29 | Tarde | TRZ-02 | Motivo_Parada fuera del catalogo cerrado. | Motivo_Parada = "aa" (normalizado: "aa"), Tiempo_Parada_min = 60, OF_Lote = OF-4281 |
| R13-TRZ-03-2026-08-30-Noche | R13 | Baja | 2026-08-30 | Noche | TRZ-03 | Motivo_Parada fuera del catalogo cerrado. | Motivo_Parada = "x" (normalizado: "x"), Tiempo_Parada_min = 60, OF_Lote = OF-4282 |
