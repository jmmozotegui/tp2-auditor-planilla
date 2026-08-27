# Corrida de auditoría — planilla de producción

- **Fecha y hora de la corrida:** 2026-08-27 17:43 UTC
- **Fecha de corte usada:** 2026-08-19
- **Filas analizadas:** 117 (OF-4101 a OF-4217, `Fecha` del 2026-08-03 al 2026-08-19)
- **Filas ignoradas por corte:** 63 (OF-4218 a OF-4280, `Fecha` del 2026-08-20 al 2026-08-28)

```json
{
  "meta": {
    "periodo_desde": "2026-08-03",
    "periodo_hasta": "2026-08-19",
    "fecha_corte": "2026-08-19",
    "filas_analizadas": 117,
    "filas_ignoradas_por_corte": 63
  },
  "hallazgos": [
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
      "evidencia": "OF-4115: Hora_Inicio = \"14:00\", Hora_Fin = \"\" (vacío).",
      "accion": "Solicitar al supervisor del turno que complete la Hora_Fin de OF-4115."
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
      "evidencia": "OF-4159: Operario = \"\" (vacío), Supervisor = \"SUP-02\".",
      "accion": "Solicitar al supervisor SUP-02 que identifique el legajo del operario de OF-4159."
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
      "evidencia": "6 ocurrencias tras normalizar: 2026-08-03 Mañana 'falla electrica' (85 min), 2026-08-04 Mañana 'Falla electrica' (80 min), 2026-08-04 Noche 'Falla eléctrica' (50 min), 2026-08-05 Mañana 'Falla electrica' (65 min), 2026-08-05 Noche 'Falla electrica' (165 min), 2026-08-06 Noche 'falla electrica' (100 min).",
      "accion": "Investigar causa raíz del problema eléctrico recurrente en EXT-02 en la semana del 03 al 07/08."
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
      "evidencia": "7 ocurrencias tras normalizar, todas cargadas como 'Falla mecanica': 2026-08-03 Mañana (50 min), 2026-08-03 Noche (45 min), 2026-08-04 Mañana (45 min), 2026-08-06 Mañana (35 min), 2026-08-06 Tarde (20 min), 2026-08-06 Noche (60 min), 2026-08-07 Noche (45 min).",
      "accion": "Investigar causa raíz de la falla mecánica recurrente en TRZ-01 en la semana del 03 al 07/08."
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
      "evidencia": "5 ocurrencias tras normalizar, todas cargadas como 'Falta de insumo': 2026-08-10 Noche (45 min), 2026-08-12 Tarde (60 min), 2026-08-13 Mañana (80 min), 2026-08-14 Mañana (15 min), 2026-08-14 Tarde (45 min).",
      "accion": "Investigar causa raíz del faltante de insumo recurrente en EXT-01 en la semana del 10 al 14/08."
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
      "evidencia": "5 ocurrencias tras normalizar: 2026-08-12 Mañana 'falla electrica' (50 min), 2026-08-12 Noche 'Falla electrica' (100 min), 2026-08-13 Mañana 'Falla electrica' (140 min), 2026-08-13 Tarde 'Falla eléctrica' (80 min), 2026-08-14 Tarde 'falla electrica' (130 min).",
      "accion": "Investigar causa raíz del problema eléctrico recurrente en EXT-02 en la semana del 10 al 14/08."
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
      "evidencia": "OF-4138: Tiempo_Parada_min = 20, Motivo_Parada = \"\" (vacío), Tipo_Parada = \"\" (vacío).",
      "accion": "Solicitar al supervisor del turno que complete el motivo de parada de OF-4138."
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
      "descripcion": "Parada con motivo 'Otros' sin Observaciones que la expliquen.",
      "evidencia": "OF-4213: Tiempo_Parada_min = 15, Motivo_Parada = \"Otros\", Observaciones = \"\" (vacío).",
      "accion": "Solicitar al supervisor del turno que detalle en Observaciones el motivo 'Otros' de OF-4213."
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla electrica' (65 min), Tarde 'Falta de insumo' (120 min), Noche 'Falla electrica' (165 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (45 min), Tarde 'Ajuste de calidad' (45 min), Noche 'Falla mecanica' (45 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla mecanica' (35 min), Tarde 'Falla mecanica' (20 min), Noche 'Falla mecanica' (60 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Falta de insumo' (20 min), Tarde 'Falta de insumo' (20 min), Noche 'Falla mecanica' (45 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Ajuste de calidad' (45 min), Tarde 'Falta de insumo' (95 min), Noche 'Ajuste de calidad' (30 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'falla electrica' (50 min), Tarde 'Ajuste de calidad' (20 min), Noche 'Falla electrica' (100 min); las tres con Tipo_Parada = 'No Planificada'.",
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
      "descripcion": "3 paradas No Planificadas en la misma línea y fecha.",
      "evidencia": "Mañana 'Falla electrica' (140 min), Tarde 'Falla eléctrica' (80 min), Noche 'Falta de insumo' (30 min); las tres con Tipo_Parada = 'No Planificada'.",
      "accion": "Revisar con el jefe de línea las tres paradas no planificadas de EXT-02 del 13/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 120 + Tarde 0 + Noche 45 = 165 min.",
      "accion": "Validar con el jefe de línea la carga de los 165 minutos de parada de EXT-01 del 03/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 85 + Tarde 0 + Noche 65 = 150 min.",
      "accion": "Validar con el jefe de línea la carga de los 150 minutos de parada de EXT-02 del 03/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 80 + Tarde 45 + Noche 50 = 175 min.",
      "accion": "Validar con el jefe de línea la carga de los 175 minutos de parada de EXT-02 del 04/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 65 + Tarde 120 + Noche 165 = 350 min.",
      "accion": "Validar con el jefe de línea la carga de los 350 minutos de parada de EXT-02 del 05/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 90 + Noche 110 = 200 min.",
      "accion": "Validar con el jefe de línea la carga de los 200 minutos de parada de TRZ-01 del 05/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 45 + Noche 45 = 135 min.",
      "accion": "Validar con el jefe de línea la carga de los 135 minutos de parada de EXT-01 del 06/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 45 + Noche 80 = 170 min.",
      "accion": "Validar con el jefe de línea la carga de los 170 minutos de parada de EXT-02 del 11/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 45 + Tarde 95 + Noche 30 = 170 min.",
      "accion": "Validar con el jefe de línea la carga de los 170 minutos de parada de TRZ-01 del 11/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 50 + Tarde 20 + Noche 100 = 170 min.",
      "accion": "Validar con el jefe de línea la carga de los 170 minutos de parada de EXT-02 del 12/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 140 + Tarde 80 + Noche 30 = 250 min.",
      "accion": "Validar con el jefe de línea la carga de los 250 minutos de parada de EXT-02 del 13/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 120 + Tarde 130 + Noche 0 = 250 min.",
      "accion": "Validar con el jefe de línea la carga de los 250 minutos de parada de EXT-02 del 14/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 60 + Tarde 95 + Noche 45 = 200 min.",
      "accion": "Validar con el jefe de línea la carga de los 200 minutos de parada de TRZ-01 del 14/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 50 + Tarde 0 + Noche 100 = 150 min.",
      "accion": "Validar con el jefe de línea la carga de los 150 minutos de parada de EXT-02 del 17/08."
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
      "descripcion": "Tiempo de parada acumulado del día por encima de 120 minutos.",
      "evidencia": "Tiempo_Parada_min: Mañana 0 + Tarde 80 + Noche 65 = 145 min.",
      "accion": "Validar con el jefe de línea la carga de los 145 minutos de parada de EXT-01 del 19/08."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4104: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 12 días hábiles entre 2026-08-03 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4104 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4114: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4114 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4117: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4117 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4115: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4115 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4118: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 11 días hábiles entre 2026-08-04 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4118 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4130: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 9 días hábiles entre 2026-08-06 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4130 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4133: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 9 días hábiles entre 2026-08-06 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4133 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4140: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4140 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4143: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4143 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4139: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 8 días hábiles entre 2026-08-07 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4139 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4146: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 7 días hábiles entre 2026-08-10 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4146 que lo cierre o justifique por qué sigue abierto."
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
      "descripcion": "Lote abierto hace más de 5 días hábiles respecto de la fecha de corte.",
      "evidencia": "OF-4155: Estado_Lote = \"Abierto\", Fecha_Cierre_Lote = \"\" (vacío); 6 días hábiles entre 2026-08-11 y la fecha de corte 2026-08-19.",
      "accion": "Pedir al supervisor del lote OF-4155 que lo cierre o justifique por qué sigue abierto."
    }
  ],
  "metricas": {
    "oee": {
      "umbral_pct": 60,
      "promedio_pct": 76.5,
      "turnos_bajo_umbral": 4,
      "peores_5": [
        { "fecha": "2026-08-05", "turno": "Noche", "linea": "EXT-02", "operario": "OP-103", "oee_pct": 50.1 },
        { "fecha": "2026-08-13", "turno": "Mañana", "linea": "EXT-02", "operario": "OP-104", "oee_pct": 53.6 },
        { "fecha": "2026-08-17", "turno": "Noche", "linea": "EXT-02", "operario": "OP-104", "oee_pct": 59.1 },
        { "fecha": "2026-08-06", "turno": "Noche", "linea": "EXT-02", "operario": "OP-106", "oee_pct": 59.8 },
        { "fecha": "2026-08-12", "turno": "Noche", "linea": "EXT-02", "operario": "OP-103", "oee_pct": 60.1 }
      ]
    },
    "cumplimiento_meta": {
      "promedio_pct": 95.4,
      "turnos_no_cumplidos": 77,
      "turnos_criticos": 12,
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
        { "fecha": "2026-08-19", "turno": "Noche", "linea": "EXT-01", "operario": "OP-101", "cumplimiento_pct": 76.2 }
      ]
    },
    "calidad": {
      "umbral_pct": 95,
      "promedio_pct": 97.8,
      "por_debajo_umbral": [
        { "tipo": "operario", "clave": "OP-102", "calidad_pct": 94.4, "filas": 20 }
      ],
      "proyeccion_semana": {
        "acumulado_pct": 97.6,
        "dias_transcurridos": 3,
        "dias_totales": 5,
        "proyectado_pct": 97.6,
        "cumple": true
      },
      "proyeccion_mes": {
        "acumulado_pct": 97.7,
        "dias_transcurridos": 13,
        "dias_totales": 21,
        "proyectado_pct": 97.7,
        "cumple": true
      }
    }
  },
  "reglas_no_evaluables": [
    {
      "regla": "R11",
      "motivo": "El contrato no define cómo se obtiene el OEE_pct de un operario cuando tiene más de una fila en la misma Maquina_Linea y Turno dentro del período, y el resultado cambia según el criterio que se use. Ejemplo verificable en TRZ-01 turno Mañana: comparando filas individuales la diferencia es 20,5 puntos (2026-08-06 OP-101 OEE_pct = 69,5 contra 2026-08-17 OP-103 OEE_pct = 90,0), lo que superaría el umbral de 10 puntos; promediando por operario la diferencia es 6,6 puntos (OP-101 = 82,2 sobre 3 filas contra OP-105 = 75,6 sobre 1 fila), lo que no lo superaría. Tampoco existe en el contrato un formato de identificador para un alcance agregado por línea y turno sobre todo el período. No se evalúa para no inventar un criterio."
    },
    {
      "regla": "R06",
      "motivo": "Parcialmente no evaluable: la fila 2026-08-17 Noche EXT-01 (OF-4197) tiene OEE_pct y Rendimiento_pct vacíos y Velocidad_Estandar_uh vacío, por lo que no puede compararse contra el umbral de 60%. El promedio y el conteo de turnos bajo umbral se calcularon sobre 116 de las 117 filas analizadas; esa fila no se estimó."
    }
  ],
  "resumen": {
    "hallazgos_alta": 6,
    "hallazgos_media": 35,
    "hallazgos_baja": 0,
    "total_hallazgos": 41
  }
}
```

| ID | Regla | Severidad | Fecha | Turno | Línea | Descripción | Evidencia |
|---|---|---|---|---|---|---|---|
| R04-TRZ-01-2026-08-04-Tarde | R04 | Alta | 2026-08-04 | Tarde | TRZ-01 | Campo obligatorio Hora_Fin vacío. | OF-4115: Hora_Inicio = "14:00", Hora_Fin = "" (vacío). |
| R04-EXT-02-2026-08-11-Tarde | R04 | Alta | 2026-08-11 | Tarde | EXT-02 | Campo obligatorio Operario vacío. | OF-4159: Operario = "" (vacío), Supervisor = "SUP-02". |
| R09-EXT-02-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma línea. | 6 ocurrencias tras normalizar: 03/08 Mañana 'falla electrica' (85 min), 04/08 Mañana 'Falla electrica' (80 min), 04/08 Noche 'Falla eléctrica' (50 min), 05/08 Mañana 'Falla electrica' (65 min), 05/08 Noche 'Falla electrica' (165 min), 06/08 Noche 'falla electrica' (100 min). |
| R09-TRZ-01-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | TRZ-01 | El motivo de parada 'falla mecanica' se repite 7 veces en la semana en la misma línea. | 7 ocurrencias tras normalizar, todas 'Falla mecanica': 03/08 Mañana (50), 03/08 Noche (45), 04/08 Mañana (45), 06/08 Mañana (35), 06/08 Tarde (20), 06/08 Noche (60), 07/08 Noche (45). |
| R09-EXT-01-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-01 | El motivo de parada 'falta de insumo' se repite 5 veces en la semana en la misma línea. | 5 ocurrencias tras normalizar, todas 'Falta de insumo': 10/08 Noche (45), 12/08 Tarde (60), 13/08 Mañana (80), 14/08 Mañana (15), 14/08 Tarde (45). |
| R09-EXT-02-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-02 | El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma línea. | 5 ocurrencias tras normalizar: 12/08 Mañana 'falla electrica' (50), 12/08 Noche 'Falla electrica' (100), 13/08 Mañana 'Falla electrica' (140), 13/08 Tarde 'Falla eléctrica' (80), 14/08 Tarde 'falla electrica' (130). |
| R03-EXT-02-2026-08-07-Mañana | R03 | Media | 2026-08-07 | Mañana | EXT-02 | Parada registrada sin motivo cargado. | OF-4138: Tiempo_Parada_min = 20, Motivo_Parada = "" (vacío), Tipo_Parada = "" (vacío). |
| R03-EXT-02-2026-08-19-Tarde | R03 | Media | 2026-08-19 | Tarde | EXT-02 | Parada con motivo 'Otros' sin Observaciones que la expliquen. | OF-4213: Tiempo_Parada_min = 15, Motivo_Parada = "Otros", Observaciones = "" (vacío). |
| R08a-EXT-02-2026-08-05 | R08a | Media | 2026-08-05 | — | EXT-02 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Falla electrica' (65), Tarde 'Falta de insumo' (120), Noche 'Falla electrica' (165); las tres No Planificada. |
| R08a-EXT-01-2026-08-06 | R08a | Media | 2026-08-06 | — | EXT-01 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Ajuste de calidad' (45), Tarde 'Ajuste de calidad' (45), Noche 'Falla mecanica' (45); las tres No Planificada. |
| R08a-TRZ-01-2026-08-06 | R08a | Media | 2026-08-06 | — | TRZ-01 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Falla mecanica' (35), Tarde 'Falla mecanica' (20), Noche 'Falla mecanica' (60); las tres No Planificada. |
| R08a-TRZ-01-2026-08-07 | R08a | Media | 2026-08-07 | — | TRZ-01 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Falta de insumo' (20), Tarde 'Falta de insumo' (20), Noche 'Falla mecanica' (45); las tres No Planificada. |
| R08a-TRZ-01-2026-08-11 | R08a | Media | 2026-08-11 | — | TRZ-01 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Ajuste de calidad' (45), Tarde 'Falta de insumo' (95), Noche 'Ajuste de calidad' (30); las tres No Planificada. |
| R08a-EXT-02-2026-08-12 | R08a | Media | 2026-08-12 | — | EXT-02 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'falla electrica' (50), Tarde 'Ajuste de calidad' (20), Noche 'Falla electrica' (100); las tres No Planificada. |
| R08a-EXT-02-2026-08-13 | R08a | Media | 2026-08-13 | — | EXT-02 | 3 paradas No Planificadas en la misma línea y fecha. | Mañana 'Falla electrica' (140), Tarde 'Falla eléctrica' (80), Noche 'Falta de insumo' (30); las tres No Planificada. |
| R08b-EXT-01-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 120 + 0 + 45 = 165 min. |
| R08b-EXT-02-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 85 + 0 + 65 = 150 min. |
| R08b-EXT-02-2026-08-04 | R08b | Media | 2026-08-04 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 80 + 45 + 50 = 175 min. |
| R08b-EXT-02-2026-08-05 | R08b | Media | 2026-08-05 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 65 + 120 + 165 = 350 min. |
| R08b-TRZ-01-2026-08-05 | R08b | Media | 2026-08-05 | — | TRZ-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 0 + 90 + 110 = 200 min. |
| R08b-EXT-01-2026-08-06 | R08b | Media | 2026-08-06 | — | EXT-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 45 + 45 + 45 = 135 min. |
| R08b-EXT-02-2026-08-11 | R08b | Media | 2026-08-11 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 45 + 45 + 80 = 170 min. |
| R08b-TRZ-01-2026-08-11 | R08b | Media | 2026-08-11 | — | TRZ-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 45 + 95 + 30 = 170 min. |
| R08b-EXT-02-2026-08-12 | R08b | Media | 2026-08-12 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 50 + 20 + 100 = 170 min. |
| R08b-EXT-02-2026-08-13 | R08b | Media | 2026-08-13 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 140 + 80 + 30 = 250 min. |
| R08b-EXT-02-2026-08-14 | R08b | Media | 2026-08-14 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 120 + 130 + 0 = 250 min. |
| R08b-TRZ-01-2026-08-14 | R08b | Media | 2026-08-14 | — | TRZ-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 60 + 95 + 45 = 200 min. |
| R08b-EXT-02-2026-08-17 | R08b | Media | 2026-08-17 | — | EXT-02 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 50 + 0 + 100 = 150 min. |
| R08b-EXT-01-2026-08-19 | R08b | Media | 2026-08-19 | — | EXT-01 | Tiempo de parada acumulado del día por encima de 120 minutos. | Tiempo_Parada_min: 0 + 80 + 65 = 145 min. |
| R12-EXT-01-2026-08-03-Tarde | R12 | Media | 2026-08-03 | Tarde | EXT-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4104: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 12 días hábiles hasta 2026-08-19. |
| R12-EXT-02-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | EXT-02 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4114: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 11 días hábiles hasta 2026-08-19. |
| R12-EXT-02-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | EXT-02 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4117: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 11 días hábiles hasta 2026-08-19. |
| R12-TRZ-01-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | TRZ-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4115: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 11 días hábiles hasta 2026-08-19. |
| R12-TRZ-01-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | TRZ-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4118: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 11 días hábiles hasta 2026-08-19. |
| R12-TRZ-01-2026-08-06-Mañana | R12 | Media | 2026-08-06 | Mañana | TRZ-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4130: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 9 días hábiles hasta 2026-08-19. |
| R12-TRZ-01-2026-08-06-Tarde | R12 | Media | 2026-08-06 | Tarde | TRZ-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4133: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 9 días hábiles hasta 2026-08-19. |
| R12-EXT-01-2026-08-07-Tarde | R12 | Media | 2026-08-07 | Tarde | EXT-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4140: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 8 días hábiles hasta 2026-08-19. |
| R12-EXT-01-2026-08-07-Noche | R12 | Media | 2026-08-07 | Noche | EXT-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4143: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 8 días hábiles hasta 2026-08-19. |
| R12-TRZ-01-2026-08-07-Mañana | R12 | Media | 2026-08-07 | Mañana | TRZ-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4139: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 8 días hábiles hasta 2026-08-19. |
| R12-EXT-01-2026-08-10-Mañana | R12 | Media | 2026-08-10 | Mañana | EXT-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4146: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 7 días hábiles hasta 2026-08-19. |
| R12-EXT-01-2026-08-11-Mañana | R12 | Media | 2026-08-11 | Mañana | EXT-01 | Lote abierto hace más de 5 días hábiles respecto de la fecha de corte. | OF-4155: Estado_Lote = "Abierto", Fecha_Cierre_Lote vacío; 6 días hábiles hasta 2026-08-19. |
