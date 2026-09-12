# Auditoría de Planilla de Producción — Corrida v3 Haiku

**Fecha y hora de corrida:** 2026-09-12 18:21:24 UTC

**Fecha de corte:** 2026-08-30

**Filas analizadas:** 182

---

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
      "regla": "R01",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-29",
      "turno": "Tarde",
      "linea": "TRZ-02",
      "operario": "OP-102",
      "descripcion": "Hora de fin menor o igual a hora de inicio (turno no noche).",
      "evidencia": "Hora_Inicio = '22:01', Hora_Fin = '06:01'",
      "accion": "Revisar y corregir los horarios registrados.",
      "id": "R01-TRZ-02-2026-08-29-Tarde"
    },
    {
      "regla": "R04",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Campos obligatorios vacíos.",
      "evidencia": "Campos vacíos: Hora_Fin",
      "accion": "Completar los campos obligatorios faltantes.",
      "id": "R04-TRZ-01-2026-08-04-Tarde"
    },
    {
      "regla": "R04",
      "severidad": "Alta",
      "alcance": "fila",
      "fecha": "2026-08-11",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": NaN,
      "descripcion": "Campos obligatorios vacíos.",
      "evidencia": "Campos vacíos: Operario",
      "accion": "Completar los campos obligatorios faltantes.",
      "id": "R04-EXT-02-2026-08-11-Tarde"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-06",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Motivo de parada 'falla electrica' aparece 6 veces en la semana 32 en EXT-02.",
      "evidencia": "'falla electrica' se repite 6 veces la semana W32 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-EXT-02-2026-W32"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-07",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Motivo de parada 'falla mecanica' aparece 7 veces en la semana 32 en TRZ-01.",
      "evidencia": "'falla mecanica' se repite 7 veces la semana W32 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-TRZ-01-2026-W32"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-10..2026-08-14",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Motivo de parada 'falta de insumo' aparece 5 veces en la semana 33 en EXT-01.",
      "evidencia": "'falta de insumo' se repite 5 veces la semana W33 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-EXT-01-2026-W33"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-12..2026-08-14",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Motivo de parada 'falla electrica' aparece 5 veces en la semana 33 en EXT-02.",
      "evidencia": "'falla electrica' se repite 5 veces la semana W33 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-EXT-02-2026-W33"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-17..2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Motivo de parada 'falla electrica' aparece 4 veces en la semana 34 en EXT-02.",
      "evidencia": "'falla electrica' se repite 4 veces la semana W34 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-EXT-02-2026-W34"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-17..2026-08-19",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Motivo de parada 'mantenimiento programado' aparece 4 veces en la semana 34 en TRZ-01.",
      "evidencia": "'mantenimiento programado' se repite 4 veces la semana W34 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-TRZ-01-2026-W34"
    },
    {
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-24..2026-08-28",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Motivo de parada 'falla electrica' aparece 7 veces en la semana 35 en EXT-02.",
      "evidencia": "'falla electrica' se repite 7 veces la semana W35 de 2026",
      "accion": "Investigar causa raíz del problema recurrente.",
      "id": "R09-EXT-02-2026-W35"
    },
    {
      "regla": "R03",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": "OP-106",
      "descripcion": "Parada registrada sin motivo cargado.",
      "evidencia": "Tiempo_Parada_min = 20, Motivo_Parada = '' (vacío)",
      "accion": "Solicitar al supervisor que complete el motivo de parada.",
      "id": "R03-EXT-02-2026-08-07-Mañana"
    },
    {
      "regla": "R03",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Parada con motivo 'Otros' sin observación explicativa.",
      "evidencia": "Motivo_Parada = 'Otros', Observaciones = '' (vacío)",
      "accion": "Solicitar al supervisor que explique el motivo de parada en observaciones.",
      "id": "R03-EXT-02-2026-08-19-Tarde"
    },
    {
      "regla": "R05",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-21",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Producción nula pero con tiempo productivo significativo.",
      "evidencia": "Cant_Producida = 0, Tiempo_Productivo_min = 480.0",
      "accion": "Investigar por qué no se registró producción durante este turno.",
      "id": "R05-TRZ-01-2026-08-21-Tarde"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-02 el 2026-08-05",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-02-2026-08-05"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-01 el 2026-08-06",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-01-2026-08-06"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en TRZ-01 el 2026-08-06",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-TRZ-01-2026-08-06"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-07",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en TRZ-01 el 2026-08-07",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-TRZ-01-2026-08-07"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en TRZ-01 el 2026-08-11",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-TRZ-01-2026-08-11"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-12",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-02 el 2026-08-12",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-02-2026-08-12"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-13",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-02 el 2026-08-13",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-02-2026-08-13"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-20",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-02 el 2026-08-20",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-02-2026-08-20"
    },
    {
      "regla": "R08a",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "3 paradas no planificadas en la misma línea y fecha.",
      "evidencia": "Más de 2 paradas no planificadas en EXT-02 el 2026-08-21",
      "accion": "Analizar las causas recurrentes de paradas no planificadas.",
      "id": "R08a-EXT-02-2026-08-21"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-03",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 165 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 165 > 120 en EXT-01 el 2026-08-03",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-01-2026-08-03"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-03",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 150 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-03",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-03"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-04",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 175 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 175 > 120 en EXT-02 el 2026-08-04",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-04"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 350 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 350 > 120 en EXT-02 el 2026-08-05",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-05"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-05",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 200 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 200 > 120 en TRZ-01 el 2026-08-05",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-TRZ-01-2026-08-05"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-06",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 135 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 135 > 120 en EXT-01 el 2026-08-06",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-01-2026-08-06"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 170 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 170 > 120 en EXT-02 el 2026-08-11",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-11"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-11",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 170 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 170 > 120 en TRZ-01 el 2026-08-11",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-TRZ-01-2026-08-11"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-12",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 170 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 170 > 120 en EXT-02 el 2026-08-12",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-12"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-13",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 250 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-13",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-13"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-14",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 250 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-14",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-14"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-14",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 200 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 200 > 120 en TRZ-01 el 2026-08-14",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-TRZ-01-2026-08-14"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-17",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 150 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-17",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-17"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-19",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 145 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 145 > 120 en EXT-01 el 2026-08-19",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-01-2026-08-19"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-20",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 150 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-20",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-20"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-21",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 270 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 270 > 120 en EXT-02 el 2026-08-21",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-21"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-25",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 175 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 175 > 120 en EXT-02 el 2026-08-25",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-25"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 165 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 165 > 120 en EXT-01 el 2026-08-26",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-01-2026-08-26"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 255 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 255 > 120 en EXT-02 el 2026-08-26",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-26"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-26",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 135 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 135 > 120 en TRZ-01 el 2026-08-26",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-TRZ-01-2026-08-26"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-27",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 250 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-27",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-27"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-28",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 200 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 200 > 120 en EXT-02 el 2026-08-28",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-EXT-02-2026-08-28"
    },
    {
      "regla": "R08b",
      "severidad": "Media",
      "alcance": "agregado",
      "fecha": "2026-08-28",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Tiempo de parada acumulado 135 minutos en la misma línea y fecha.",
      "evidencia": "Tiempo_Parada_min acumulado = 135 > 120 en TRZ-01 el 2026-08-28",
      "accion": "Investigar la causa raíz del alto tiempo de parada acumulado.",
      "id": "R08b-TRZ-01-2026-08-28"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-03",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto por 19 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 19",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-03-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 18 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-04-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 18 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-04-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto por 18 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-04-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-04",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 18 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-04-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-06",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 16 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 16",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-06-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-06",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-104",
      "descripcion": "Lote abierto por 16 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 16",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-06-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto por 15 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-07-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto por 15 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-07-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-07",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 15 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-07-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-10",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-103",
      "descripcion": "Lote abierto por 14 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 14",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-10-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-11",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-103",
      "descripcion": "Lote abierto por 13 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 13",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-11-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Tarde",
      "linea": "EXT-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 12 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-12-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-103",
      "descripcion": "Lote abierto por 12 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-12-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-12",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 12 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-12-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 11 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-13-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 11 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-13-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-13",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 11 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-13-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-14",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto por 10 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 10",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-14-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-17",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-104",
      "descripcion": "Lote abierto por 9 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 9",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-17-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": "OP-103",
      "descripcion": "Lote abierto por 8 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-18-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-104",
      "descripcion": "Lote abierto por 8 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-18-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-106",
      "descripcion": "Lote abierto por 8 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-18-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 8 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-18-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-18",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 8 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-18-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 7 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-19-Tarde"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Mañana",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 7 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-19-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-19",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-102",
      "descripcion": "Lote abierto por 7 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-19-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Mañana",
      "linea": "EXT-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 6 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-01-2026-08-20-Mañana"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": "OP-101",
      "descripcion": "Lote abierto por 6 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-EXT-02-2026-08-20-Noche"
    },
    {
      "regla": "R12",
      "severidad": "Media",
      "alcance": "fila",
      "fecha": "2026-08-20",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": "OP-105",
      "descripcion": "Lote abierto por 6 días hábiles sin cerrar.",
      "evidencia": "Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6",
      "accion": "Investigar el motivo del retraso en el cierre del lote.",
      "id": "R12-TRZ-01-2026-08-20-Noche"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia de 17.5 puntos en OEE entre operarios en turno Noche.",
      "evidencia": "Máximo OEE = 83.9%, Mínimo OEE = 66.5%, Diferencia = 17.5",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-EXT-01-Noche"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 26.3 puntos en OEE entre operarios en turno Mañana.",
      "evidencia": "Máximo OEE = 83.6%, Mínimo OEE = 57.3%, Diferencia = 26.3",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-EXT-02-Mañana"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 12.3 puntos en OEE entre operarios en turno Tarde.",
      "evidencia": "Máximo OEE = 84.3%, Mínimo OEE = 72.0%, Diferencia = 12.3",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-EXT-02-Tarde"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia de 20.6 puntos en OEE entre operarios en turno Noche.",
      "evidencia": "Máximo OEE = 84.9%, Mínimo OEE = 64.3%, Diferencia = 20.6",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-EXT-02-Noche"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de 16.3 puntos en OEE entre operarios en turno Tarde.",
      "evidencia": "Máximo OEE = 85.8%, Mínimo OEE = 69.5%, Diferencia = 16.3",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-TRZ-01-Tarde"
    },
    {
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-30",
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia de 15.1 puntos en OEE entre operarios en turno Noche.",
      "evidencia": "Máximo OEE = 83.7%, Mínimo OEE = 68.7%, Diferencia = 15.1",
      "accion": "Revisar desempeño de operarios y analizar variabilidad.",
      "id": "R11-TRZ-01-Noche"
    },
    {
      "regla": "R13",
      "severidad": "Baja",
      "alcance": "fila",
      "fecha": "2026-08-29",
      "turno": "Tarde",
      "linea": "TRZ-02",
      "operario": "OP-102",
      "descripcion": "Motivo de parada 'aa' no está en catálogo cerrado.",
      "evidencia": "Motivo_Parada = 'aa'",
      "accion": "Estandarizar el motivo de parada según catálogo.",
      "id": "R13-TRZ-02-2026-08-29-Tarde"
    },
    {
      "regla": "R13",
      "severidad": "Baja",
      "alcance": "fila",
      "fecha": "2026-08-30",
      "turno": "Noche",
      "linea": "TRZ-03",
      "operario": "OP-103",
      "descripcion": "Motivo de parada 'x' no está en catálogo cerrado.",
      "evidencia": "Motivo_Parada = 'x'",
      "accion": "Estandarizar el motivo de parada según catálogo.",
      "id": "R13-TRZ-03-2026-08-30-Noche"
    }
  ],
  "metricas": {
    "oee": {
      "umbral_pct": 60,
      "promedio_pct": 76.4,
      "turnos_bajo_umbral": 8,
      "peores_5": [
        {
          "fecha": "2026-08-28",
          "turno": "Mañana",
          "linea": "EXT-02",
          "oee_pct": 44.7
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "EXT-02",
          "oee_pct": 50.1
        },
        {
          "fecha": "2026-08-13",
          "turno": "Mañana",
          "linea": "EXT-02",
          "oee_pct": 53.6
        },
        {
          "fecha": "2026-08-27",
          "turno": "Mañana",
          "linea": "EXT-02",
          "oee_pct": 54.2
        },
        {
          "fecha": "2026-08-26",
          "turno": "Tarde",
          "linea": "EXT-02",
          "oee_pct": 55.5
        }
      ]
    },
    "cumplimiento_meta": {
      "promedio_pct": 94.7,
      "turnos_no_cumplidos": 119,
      "turnos_criticos": 17,
      "criticos": [
        {
          "fecha": "2026-08-03",
          "turno": "Mañana",
          "linea": "EXT-01",
          "cumplimiento_pct": 79.3
        },
        {
          "fecha": "2026-08-04",
          "turno": "Mañana",
          "linea": "EXT-02",
          "cumplimiento_pct": 79.9
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "EXT-02",
          "cumplimiento_pct": 61.7
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "TRZ-01",
          "cumplimiento_pct": 77.5
        },
        {
          "fecha": "2026-08-06",
          "turno": "Noche",
          "linea": "EXT-02",
          "cumplimiento_pct": 73.3
        },
        {
          "fecha": "2026-08-12",
          "turno": "Noche",
          "linea": "EXT-02",
          "cumplimiento_pct": 74.9
        },
        {
          "fecha": "2026-08-13",
          "turno": "Mañana",
          "linea": "EXT-02",
          "cumplimiento_pct": 66.2
        },
        {
          "fecha": "2026-08-14",
          "turno": "Mañana",
          "linea": "EXT-02",
          "cumplimiento_pct": 76.8
        },
        {
          "fecha": "2026-08-14",
          "turno": "Tarde",
          "linea": "EXT-02",
          "cumplimiento_pct": 77.4
        },
        {
          "fecha": "2026-08-17",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "cumplimiento_pct": 78.7
        },
        {
          "fecha": "2026-08-17",
          "turno": "Noche",
          "linea": "EXT-02",
          "cumplimiento_pct": 72.9
        },
        {
          "fecha": "2026-08-19",
          "turno": "Noche",
          "linea": "EXT-01",
          "cumplimiento_pct": 76.2
        },
        {
          "fecha": "2026-08-21",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "cumplimiento_pct": 0.0
        },
        {
          "fecha": "2026-08-26",
          "turno": "Tarde",
          "linea": "EXT-02",
          "cumplimiento_pct": 68.6
        },
        {
          "fecha": "2026-08-26",
          "turno": "Noche",
          "linea": "EXT-02",
          "cumplimiento_pct": 77.6
        },
        {
          "fecha": "2026-08-27",
          "turno": "Mañana",
          "linea": "EXT-02",
          "cumplimiento_pct": 67.2
        },
        {
          "fecha": "2026-08-28",
          "turno": "Mañana",
          "linea": "EXT-02",
          "cumplimiento_pct": 55.4
        }
      ]
    },
    "calidad": {
      "umbral_pct": 95,
      "promedio_pct": 97.8,
      "por_debajo_umbral": [
        {
          "operario": "OP-102",
          "calidad_pct": 94.5
        }
      ],
      "proyeccion_semana": {
        "acumulado_pct": 98.0,
        "dias_transcurridos": 5,
        "dias_totales": 5,
        "proyectado_pct": 98.0,
        "cumple": true
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
  "reglas_no_evaluables": [],
  "resumen": {
    "hallazgos_alta": 10,
    "hallazgos_media": 66,
    "hallazgos_baja": 8,
    "total_hallazgos": 84
  }
}

| ID | Regla | Severidad | Fecha | Turno | Línea | Descripción | Evidencia |
|---|---|---|---|---|---|---|---|
| R01-TRZ-02-2026-08-29-Tarde | R01 | Alta | 2026-08-29 | Tarde | TRZ-02 | Hora de fin menor o igual a hora de inicio (turno no noche). | Hora_Inicio = '22:01', Hora_Fin = '06:01' |
| R04-TRZ-01-2026-08-04-Tarde | R04 | Alta | 2026-08-04 | Tarde | TRZ-01 | Campos obligatorios vacíos. | Campos vacíos: Hora_Fin |
| R04-EXT-02-2026-08-11-Tarde | R04 | Alta | 2026-08-11 | Tarde | EXT-02 | Campos obligatorios vacíos. | Campos vacíos: Operario |
| R09-EXT-02-2026-W32 | R09 | Alta | 2026-08-03..2026-08-06 | — | EXT-02 | Motivo de parada 'falla electrica' aparece 6 veces en la semana 32 en EXT-02. | 'falla electrica' se repite 6 veces la semana W32 de 2026 |
| R09-TRZ-01-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 | — | TRZ-01 | Motivo de parada 'falla mecanica' aparece 7 veces en la semana 32 en TRZ-01. | 'falla mecanica' se repite 7 veces la semana W32 de 2026 |
| R09-EXT-01-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 | — | EXT-01 | Motivo de parada 'falta de insumo' aparece 5 veces en la semana 33 en EXT-01. | 'falta de insumo' se repite 5 veces la semana W33 de 2026 |
| R09-EXT-02-2026-W33 | R09 | Alta | 2026-08-12..2026-08-14 | — | EXT-02 | Motivo de parada 'falla electrica' aparece 5 veces en la semana 33 en EXT-02. | 'falla electrica' se repite 5 veces la semana W33 de 2026 |
| R09-EXT-02-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 | — | EXT-02 | Motivo de parada 'falla electrica' aparece 4 veces en la semana 34 en EXT-02. | 'falla electrica' se repite 4 veces la semana W34 de 2026 |
| R09-TRZ-01-2026-W34 | R09 | Alta | 2026-08-17..2026-08-19 | — | TRZ-01 | Motivo de parada 'mantenimiento programado' aparece 4 veces en la semana 34 en TRZ-01. | 'mantenimiento programado' se repite 4 veces la semana W34 de 2026 |
| R09-EXT-02-2026-W35 | R09 | Alta | 2026-08-24..2026-08-28 | — | EXT-02 | Motivo de parada 'falla electrica' aparece 7 veces en la semana 35 en EXT-02. | 'falla electrica' se repite 7 veces la semana W35 de 2026 |
| R03-EXT-02-2026-08-07-Mañana | R03 | Media | 2026-08-07 | Mañana | EXT-02 | Parada registrada sin motivo cargado. | Tiempo_Parada_min = 20, Motivo_Parada = '' (vacío) |
| R03-EXT-02-2026-08-19-Tarde | R03 | Media | 2026-08-19 | Tarde | EXT-02 | Parada con motivo 'Otros' sin observación explicativa. | Motivo_Parada = 'Otros', Observaciones = '' (vacío) |
| R05-TRZ-01-2026-08-21-Tarde | R05 | Media | 2026-08-21 | Tarde | TRZ-01 | Producción nula pero con tiempo productivo significativo. | Cant_Producida = 0, Tiempo_Productivo_min = 480.0 |
| R08a-EXT-02-2026-08-05 | R08a | Media | 2026-08-05 | — | EXT-02 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-02 el 2026-08-05 |
| R08a-EXT-01-2026-08-06 | R08a | Media | 2026-08-06 | — | EXT-01 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-01 el 2026-08-06 |
| R08a-TRZ-01-2026-08-06 | R08a | Media | 2026-08-06 | — | TRZ-01 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en TRZ-01 el 2026-08-06 |
| R08a-TRZ-01-2026-08-07 | R08a | Media | 2026-08-07 | — | TRZ-01 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en TRZ-01 el 2026-08-07 |
| R08a-TRZ-01-2026-08-11 | R08a | Media | 2026-08-11 | — | TRZ-01 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en TRZ-01 el 2026-08-11 |
| R08a-EXT-02-2026-08-12 | R08a | Media | 2026-08-12 | — | EXT-02 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-02 el 2026-08-12 |
| R08a-EXT-02-2026-08-13 | R08a | Media | 2026-08-13 | — | EXT-02 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-02 el 2026-08-13 |
| R08a-EXT-02-2026-08-20 | R08a | Media | 2026-08-20 | — | EXT-02 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-02 el 2026-08-20 |
| R08a-EXT-02-2026-08-21 | R08a | Media | 2026-08-21 | — | EXT-02 | 3 paradas no planificadas en la misma línea y fecha. | Más de 2 paradas no planificadas en EXT-02 el 2026-08-21 |
| R08b-EXT-01-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-01 | Tiempo de parada acumulado 165 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 165 > 120 en EXT-01 el 2026-08-03 |
| R08b-EXT-02-2026-08-03 | R08b | Media | 2026-08-03 | — | EXT-02 | Tiempo de parada acumulado 150 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-03 |
| R08b-EXT-02-2026-08-04 | R08b | Media | 2026-08-04 | — | EXT-02 | Tiempo de parada acumulado 175 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 175 > 120 en EXT-02 el 2026-08-04 |
| R08b-EXT-02-2026-08-05 | R08b | Media | 2026-08-05 | — | EXT-02 | Tiempo de parada acumulado 350 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 350 > 120 en EXT-02 el 2026-08-05 |
| R08b-TRZ-01-2026-08-05 | R08b | Media | 2026-08-05 | — | TRZ-01 | Tiempo de parada acumulado 200 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 200 > 120 en TRZ-01 el 2026-08-05 |
| R08b-EXT-01-2026-08-06 | R08b | Media | 2026-08-06 | — | EXT-01 | Tiempo de parada acumulado 135 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 135 > 120 en EXT-01 el 2026-08-06 |
| R08b-EXT-02-2026-08-11 | R08b | Media | 2026-08-11 | — | EXT-02 | Tiempo de parada acumulado 170 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 170 > 120 en EXT-02 el 2026-08-11 |
| R08b-TRZ-01-2026-08-11 | R08b | Media | 2026-08-11 | — | TRZ-01 | Tiempo de parada acumulado 170 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 170 > 120 en TRZ-01 el 2026-08-11 |
| R08b-EXT-02-2026-08-12 | R08b | Media | 2026-08-12 | — | EXT-02 | Tiempo de parada acumulado 170 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 170 > 120 en EXT-02 el 2026-08-12 |
| R08b-EXT-02-2026-08-13 | R08b | Media | 2026-08-13 | — | EXT-02 | Tiempo de parada acumulado 250 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-13 |
| R08b-EXT-02-2026-08-14 | R08b | Media | 2026-08-14 | — | EXT-02 | Tiempo de parada acumulado 250 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-14 |
| R08b-TRZ-01-2026-08-14 | R08b | Media | 2026-08-14 | — | TRZ-01 | Tiempo de parada acumulado 200 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 200 > 120 en TRZ-01 el 2026-08-14 |
| R08b-EXT-02-2026-08-17 | R08b | Media | 2026-08-17 | — | EXT-02 | Tiempo de parada acumulado 150 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-17 |
| R08b-EXT-01-2026-08-19 | R08b | Media | 2026-08-19 | — | EXT-01 | Tiempo de parada acumulado 145 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 145 > 120 en EXT-01 el 2026-08-19 |
| R08b-EXT-02-2026-08-20 | R08b | Media | 2026-08-20 | — | EXT-02 | Tiempo de parada acumulado 150 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 150 > 120 en EXT-02 el 2026-08-20 |
| R08b-EXT-02-2026-08-21 | R08b | Media | 2026-08-21 | — | EXT-02 | Tiempo de parada acumulado 270 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 270 > 120 en EXT-02 el 2026-08-21 |
| R08b-EXT-02-2026-08-25 | R08b | Media | 2026-08-25 | — | EXT-02 | Tiempo de parada acumulado 175 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 175 > 120 en EXT-02 el 2026-08-25 |
| R08b-EXT-01-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-01 | Tiempo de parada acumulado 165 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 165 > 120 en EXT-01 el 2026-08-26 |
| R08b-EXT-02-2026-08-26 | R08b | Media | 2026-08-26 | — | EXT-02 | Tiempo de parada acumulado 255 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 255 > 120 en EXT-02 el 2026-08-26 |
| R08b-TRZ-01-2026-08-26 | R08b | Media | 2026-08-26 | — | TRZ-01 | Tiempo de parada acumulado 135 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 135 > 120 en TRZ-01 el 2026-08-26 |
| R08b-EXT-02-2026-08-27 | R08b | Media | 2026-08-27 | — | EXT-02 | Tiempo de parada acumulado 250 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 250 > 120 en EXT-02 el 2026-08-27 |
| R08b-EXT-02-2026-08-28 | R08b | Media | 2026-08-28 | — | EXT-02 | Tiempo de parada acumulado 200 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 200 > 120 en EXT-02 el 2026-08-28 |
| R08b-TRZ-01-2026-08-28 | R08b | Media | 2026-08-28 | — | TRZ-01 | Tiempo de parada acumulado 135 minutos en la misma línea y fecha. | Tiempo_Parada_min acumulado = 135 > 120 en TRZ-01 el 2026-08-28 |
| R12-EXT-01-2026-08-03-Tarde | R12 | Media | 2026-08-03 | Tarde | EXT-01 | Lote abierto por 19 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 19 |
| R12-EXT-02-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | EXT-02 | Lote abierto por 18 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18 |
| R12-EXT-02-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | EXT-02 | Lote abierto por 18 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18 |
| R12-TRZ-01-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | TRZ-01 | Lote abierto por 18 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18 |
| R12-TRZ-01-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | TRZ-01 | Lote abierto por 18 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 18 |
| R12-TRZ-01-2026-08-06-Mañana | R12 | Media | 2026-08-06 | Mañana | TRZ-01 | Lote abierto por 16 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 16 |
| R12-TRZ-01-2026-08-06-Tarde | R12 | Media | 2026-08-06 | Tarde | TRZ-01 | Lote abierto por 16 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 16 |
| R12-EXT-01-2026-08-07-Tarde | R12 | Media | 2026-08-07 | Tarde | EXT-01 | Lote abierto por 15 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15 |
| R12-EXT-01-2026-08-07-Noche | R12 | Media | 2026-08-07 | Noche | EXT-01 | Lote abierto por 15 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15 |
| R12-TRZ-01-2026-08-07-Mañana | R12 | Media | 2026-08-07 | Mañana | TRZ-01 | Lote abierto por 15 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 15 |
| R12-EXT-01-2026-08-10-Mañana | R12 | Media | 2026-08-10 | Mañana | EXT-01 | Lote abierto por 14 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 14 |
| R12-EXT-01-2026-08-11-Mañana | R12 | Media | 2026-08-11 | Mañana | EXT-01 | Lote abierto por 13 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 13 |
| R12-EXT-01-2026-08-12-Tarde | R12 | Media | 2026-08-12 | Tarde | EXT-01 | Lote abierto por 12 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12 |
| R12-EXT-02-2026-08-12-Noche | R12 | Media | 2026-08-12 | Noche | EXT-02 | Lote abierto por 12 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12 |
| R12-TRZ-01-2026-08-12-Mañana | R12 | Media | 2026-08-12 | Mañana | TRZ-01 | Lote abierto por 12 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 12 |
| R12-EXT-01-2026-08-13-Mañana | R12 | Media | 2026-08-13 | Mañana | EXT-01 | Lote abierto por 11 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11 |
| R12-EXT-01-2026-08-13-Noche | R12 | Media | 2026-08-13 | Noche | EXT-01 | Lote abierto por 11 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11 |
| R12-TRZ-01-2026-08-13-Tarde | R12 | Media | 2026-08-13 | Tarde | TRZ-01 | Lote abierto por 11 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 11 |
| R12-TRZ-01-2026-08-14-Noche | R12 | Media | 2026-08-14 | Noche | TRZ-01 | Lote abierto por 10 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 10 |
| R12-EXT-02-2026-08-17-Noche | R12 | Media | 2026-08-17 | Noche | EXT-02 | Lote abierto por 9 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 9 |
| R12-EXT-02-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | EXT-02 | Lote abierto por 8 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8 |
| R12-EXT-02-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | EXT-02 | Lote abierto por 8 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8 |
| R12-TRZ-01-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | TRZ-01 | Lote abierto por 8 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8 |
| R12-TRZ-01-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | TRZ-01 | Lote abierto por 8 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8 |
| R12-TRZ-01-2026-08-18-Noche | R12 | Media | 2026-08-18 | Noche | TRZ-01 | Lote abierto por 8 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 8 |
| R12-EXT-02-2026-08-19-Tarde | R12 | Media | 2026-08-19 | Tarde | EXT-02 | Lote abierto por 7 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7 |
| R12-TRZ-01-2026-08-19-Mañana | R12 | Media | 2026-08-19 | Mañana | TRZ-01 | Lote abierto por 7 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7 |
| R12-TRZ-01-2026-08-19-Noche | R12 | Media | 2026-08-19 | Noche | TRZ-01 | Lote abierto por 7 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 7 |
| R12-EXT-01-2026-08-20-Mañana | R12 | Media | 2026-08-20 | Mañana | EXT-01 | Lote abierto por 6 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6 |
| R12-EXT-02-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | EXT-02 | Lote abierto por 6 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6 |
| R12-TRZ-01-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | TRZ-01 | Lote abierto por 6 días hábiles sin cerrar. | Estado_Lote = 'Abierto', días hábiles posteriores sin cierre = 6 |
| R11-EXT-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-01 | Diferencia de 17.5 puntos en OEE entre operarios en turno Noche. | Máximo OEE = 83.9%, Mínimo OEE = 66.5%, Diferencia = 17.5 |
| R11-EXT-02-Mañana | R11 | Baja | 2026-08-03..2026-08-30 | Mañana | EXT-02 | Diferencia de 26.3 puntos en OEE entre operarios en turno Mañana. | Máximo OEE = 83.6%, Mínimo OEE = 57.3%, Diferencia = 26.3 |
| R11-EXT-02-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | EXT-02 | Diferencia de 12.3 puntos en OEE entre operarios en turno Tarde. | Máximo OEE = 84.3%, Mínimo OEE = 72.0%, Diferencia = 12.3 |
| R11-EXT-02-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | EXT-02 | Diferencia de 20.6 puntos en OEE entre operarios en turno Noche. | Máximo OEE = 84.9%, Mínimo OEE = 64.3%, Diferencia = 20.6 |
| R11-TRZ-01-Tarde | R11 | Baja | 2026-08-03..2026-08-30 | Tarde | TRZ-01 | Diferencia de 16.3 puntos en OEE entre operarios en turno Tarde. | Máximo OEE = 85.8%, Mínimo OEE = 69.5%, Diferencia = 16.3 |
| R11-TRZ-01-Noche | R11 | Baja | 2026-08-03..2026-08-30 | Noche | TRZ-01 | Diferencia de 15.1 puntos en OEE entre operarios en turno Noche. | Máximo OEE = 83.7%, Mínimo OEE = 68.7%, Diferencia = 15.1 |
| R13-TRZ-02-2026-08-29-Tarde | R13 | Baja | 2026-08-29 | Tarde | TRZ-02 | Motivo de parada 'aa' no está en catálogo cerrado. | Motivo_Parada = 'aa' |
| R13-TRZ-03-2026-08-30-Noche | R13 | Baja | 2026-08-30 | Noche | TRZ-03 | Motivo de parada 'x' no está en catálogo cerrado. | Motivo_Parada = 'x' |
