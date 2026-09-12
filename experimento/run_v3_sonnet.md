# Corrida de auditoria — planilla de produccion (system_prompt_v3 / user_prompt_v2)

- **Corrida (UTC):** 2026-09-12 18:22:29 UTC
- **Fecha de corte usada:** 2026-08-30 (fecha mas reciente presente en la columna Fecha de la planilla, segun user_prompt_v2.md)
- **Periodo cubierto:** 2026-08-03 a 2026-08-30
- **Filas analizadas:** 182 (de 182 filas de datos totales en la planilla)
- **Filas ignoradas por corte:** 0

---

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
      "descripcion": "Hora_Fin es menor o igual a Hora_Inicio en un turno que no es Noche.",
      "evidencia": "Hora_Inicio = 22:01, Hora_Fin = 06:01, Turno = Tarde",
      "accion": "Corregir el horario cargado por el supervisor de turno."
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
      "descripcion": "Faltan campos obligatorios: Hora_Fin.",
      "evidencia": "Campos vacíos: Hora_Fin",
      "accion": "Solicitar al supervisor que complete los campos faltantes."
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
      "descripcion": "Faltan campos obligatorios: Operario.",
      "evidencia": "Campos vacíos: Operario",
      "accion": "Solicitar al supervisor que complete los campos faltantes."
    },
    {
      "id": "R09-EXT-02-2026-W32",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-03..2026-08-06",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma línea.",
      "evidencia": "6 ocurrencias tras normalizar: 'Falla electrica' (3), 'falla electrica' (2), 'Falla eléctrica' (1), fechas: 2026-08-03, 2026-08-04, 2026-08-04, 2026-08-05, 2026-08-05, 2026-08-06",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
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
      "evidencia": "7 ocurrencias tras normalizar: 'Falla mecanica' (7), fechas: 2026-08-03, 2026-08-03, 2026-08-04, 2026-08-06, 2026-08-06, 2026-08-06, 2026-08-07",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
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
      "evidencia": "5 ocurrencias tras normalizar: 'Falta de insumo' (5), fechas: 2026-08-10, 2026-08-12, 2026-08-13, 2026-08-14, 2026-08-14",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
    },
    {
      "id": "R09-EXT-02-2026-W33",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-12..2026-08-14",
      "turno": null,
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma línea.",
      "evidencia": "5 ocurrencias tras normalizar: 'falla electrica' (2), 'Falla electrica' (2), 'Falla eléctrica' (1), fechas: 2026-08-12, 2026-08-12, 2026-08-13, 2026-08-13, 2026-08-14",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
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
      "evidencia": "4 ocurrencias tras normalizar: 'falla electrica' (2), 'Falla electrica' (1), 'Falla eléctrica' (1), fechas: 2026-08-17, 2026-08-20, 2026-08-21, 2026-08-21",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
    },
    {
      "id": "R09-TRZ-01-2026-W34",
      "regla": "R09",
      "severidad": "Alta",
      "alcance": "agregado",
      "fecha": "2026-08-17..2026-08-19",
      "turno": null,
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "El motivo de parada 'mantenimiento programado' se repite 4 veces en la semana en la misma línea.",
      "evidencia": "4 ocurrencias tras normalizar: 'Mantenimiento programado' (4), fechas: 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-19",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
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
      "evidencia": "7 ocurrencias tras normalizar: 'Falla electrica' (3), 'falla electrica' (3), 'Falla eléctrica' (1), fechas: 2026-08-24, 2026-08-25, 2026-08-26, 2026-08-26, 2026-08-27, 2026-08-27, 2026-08-28",
      "accion": "Investigar causa raíz del problema recurrente en la línea."
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
      "evidencia": "Tiempo_Parada_min = 20, Motivo_Parada = \"\" (vacío)",
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
      "descripcion": "Motivo de parada 'Otros' sin observaciones que lo expliquen.",
      "evidencia": "Motivo_Parada = \"Otros\", Observaciones = \"\" (vacío)",
      "accion": "Solicitar al supervisor del turno que complete el motivo de parada."
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
      "descripcion": "Producción cero con tiempo productivo mayor a 60 minutos.",
      "evidencia": "Cant_Producida = 0, Tiempo_Productivo_min = 480",
      "accion": "Verificar con el supervisor por qué no hubo producción en ese turno."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-05 en EXT-02, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-06 en EXT-01, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-06 en TRZ-01, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-07 en TRZ-01, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-11 en TRZ-01, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-12 en EXT-02, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-13 en EXT-02, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-20 en EXT-02, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2).",
      "evidencia": "3 paradas No Planificadas el 2026-08-21 en EXT-02, turnos: Mañana, Noche, Tarde",
      "accion": "Investigar la causa de las paradas no planificadas repetidas en la línea ese día."
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
      "descripcion": "Tiempo de parada acumulado de 165 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 165 (Mañana=120, Tarde=0, Noche=45)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 150 (Mañana=85, Tarde=0, Noche=65)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 175 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 175 (Mañana=80, Tarde=45, Noche=50)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 350 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 350 (Mañana=65, Tarde=120, Noche=165)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 200 (Mañana=0, Tarde=90, Noche=110)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 135 (Mañana=45, Tarde=45, Noche=45)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 170 (Mañana=45, Tarde=45, Noche=80)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 170 (Mañana=45, Tarde=95, Noche=30)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 170 (Mañana=50, Tarde=20, Noche=100)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 250 (Mañana=140, Tarde=80, Noche=30)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 250 (Mañana=120, Tarde=130, Noche=0)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 200 (Mañana=60, Tarde=95, Noche=45)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 150 (Mañana=50, Tarde=0, Noche=100)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 145 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 145 (Mañana=0, Tarde=80, Noche=65)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 150 (Mañana=45, Tarde=15, Noche=90)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 270 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 270 (Mañana=60, Tarde=115, Noche=95)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 175 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 175 (Mañana=20, Tarde=70, Noche=85)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 165 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 165 (Mañana=50, Tarde=60, Noche=55)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 255 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 255 (Mañana=0, Tarde=110, Noche=145)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 135 (Mañana=45, Tarde=90, Noche=0)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 250 (Mañana=150, Tarde=15, Noche=85)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 200 (Mañana=180, Tarde=0, Noche=20)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120).",
      "evidencia": "Suma Tiempo_Parada_min = 135 (Mañana=0, Tarde=75, Noche=60)",
      "accion": "Revisar con el supervisor las paradas acumuladas de esa línea en la fecha."
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
      "descripcion": "Lote abierto con 19 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-03, OF_Lote = OF-4104, días hábiles posteriores hasta el corte = 19",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4114, días hábiles posteriores hasta el corte = 18",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4117, días hábiles posteriores hasta el corte = 18",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4115, días hábiles posteriores hasta el corte = 18",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4118, días hábiles posteriores hasta el corte = 18",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 16 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-06, OF_Lote = OF-4130, días hábiles posteriores hasta el corte = 16",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 16 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-06, OF_Lote = OF-4133, días hábiles posteriores hasta el corte = 16",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4140, días hábiles posteriores hasta el corte = 15",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4143, días hábiles posteriores hasta el corte = 15",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4139, días hábiles posteriores hasta el corte = 15",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 14 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-10, OF_Lote = OF-4146, días hábiles posteriores hasta el corte = 14",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 13 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-11, OF_Lote = OF-4155, días hábiles posteriores hasta el corte = 13",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4167, días hábiles posteriores hasta el corte = 12",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4171, días hábiles posteriores hasta el corte = 12",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4166, días hábiles posteriores hasta el corte = 12",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4173, días hábiles posteriores hasta el corte = 11",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4179, días hábiles posteriores hasta el corte = 11",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4178, días hábiles posteriores hasta el corte = 11",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 10 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-14, OF_Lote = OF-4190, días hábiles posteriores hasta el corte = 10",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 9 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-17, OF_Lote = OF-4198, días hábiles posteriores hasta el corte = 9",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4201, días hábiles posteriores hasta el corte = 8",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4204, días hábiles posteriores hasta el corte = 8",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4202, días hábiles posteriores hasta el corte = 8",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4205, días hábiles posteriores hasta el corte = 8",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4208, días hábiles posteriores hasta el corte = 8",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4213, días hábiles posteriores hasta el corte = 7",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4211, días hábiles posteriores hasta el corte = 7",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4217, días hábiles posteriores hasta el corte = 7",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4218, días hábiles posteriores hasta el corte = 6",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4225, días hábiles posteriores hasta el corte = 6",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
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
      "descripcion": "Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30).",
      "evidencia": "Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4226, días hábiles posteriores hasta el corte = 6",
      "accion": "Verificar con el supervisor el estado real del lote y cerrarlo si corresponde."
    },
    {
      "id": "R11-EXT-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Noche",
      "linea": "EXT-01",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-101 (OEE=73.5%) vs OP-102 (OEE=83.9%) dif=10.4pts; OP-102 (OEE=83.9%) vs OP-104 (OEE=66.4%) dif=17.5pts; OP-103 (OEE=78.4%) vs OP-104 (OEE=66.4%) dif=11.9pts; OP-104 (OEE=66.4%) vs OP-105 (OEE=80.8%) dif=14.4pts; OP-104 (OEE=66.4%) vs OP-106 (OEE=81.5%) dif=15.0pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
    },
    {
      "id": "R11-EXT-02-Mañana",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Mañana",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-101 (OEE=74.6%) vs OP-104 (OEE=57.3%) dif=17.3pts; OP-103 (OEE=83.6%) vs OP-104 (OEE=57.3%) dif=26.3pts; OP-103 (OEE=83.6%) vs OP-106 (OEE=70.8%) dif=12.8pts; OP-104 (OEE=57.3%) vs OP-105 (OEE=76.7%) dif=19.4pts; OP-104 (OEE=57.3%) vs OP-106 (OEE=70.8%) dif=13.6pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
    },
    {
      "id": "R11-EXT-02-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Tarde",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-102 (OEE=72.0%) vs OP-106 (OEE=84.3%) dif=12.3pts; OP-104 (OEE=73.1%) vs OP-106 (OEE=84.3%) dif=11.2pts; OP-105 (OEE=72.1%) vs OP-106 (OEE=84.3%) dif=12.3pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
    },
    {
      "id": "R11-EXT-02-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Noche",
      "linea": "EXT-02",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-101 (OEE=72.3%) vs OP-105 (OEE=84.9%) dif=12.6pts; OP-102 (OEE=70.8%) vs OP-105 (OEE=84.9%) dif=14.1pts; OP-103 (OEE=70.1%) vs OP-105 (OEE=84.9%) dif=14.8pts; OP-104 (OEE=68.0%) vs OP-105 (OEE=84.9%) dif=16.9pts; OP-105 (OEE=84.9%) vs OP-106 (OEE=64.4%) dif=20.6pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
    },
    {
      "id": "R11-TRZ-01-Tarde",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Tarde",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-101 (OEE=73.9%) vs OP-103 (OEE=85.8%) dif=11.9pts; OP-103 (OEE=85.8%) vs OP-104 (OEE=69.5%) dif=16.3pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
    },
    {
      "id": "R11-TRZ-01-Noche",
      "regla": "R11",
      "severidad": "Baja",
      "alcance": "agregado",
      "fecha": null,
      "turno": "Noche",
      "linea": "TRZ-01",
      "operario": null,
      "descripcion": "Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno.",
      "evidencia": "OP-103 (OEE=80.0%) vs OP-105 (OEE=68.7%) dif=11.4pts; OP-104 (OEE=72.0%) vs OP-106 (OEE=83.7%) dif=11.8pts; OP-105 (OEE=68.7%) vs OP-106 (OEE=83.7%) dif=15.1pts",
      "accion": "Revisar diferencias de desempeño entre operarios en esa línea y turno."
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
      "descripcion": "Motivo_Parada fuera del catálogo cerrado de motivos.",
      "evidencia": "Motivo_Parada = \"aa\"",
      "accion": "Corregir el motivo de parada para que corresponda al catálogo cerrado."
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
      "descripcion": "Motivo_Parada fuera del catálogo cerrado de motivos.",
      "evidencia": "Motivo_Parada = \"x\"",
      "accion": "Corregir el motivo de parada para que corresponda al catálogo cerrado."
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
      "promedio_pct": 94.7,
      "turnos_no_cumplidos": 119,
      "turnos_criticos": 17,
      "criticos": [
        {
          "fecha": "2026-08-21",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "operario": "OP-105",
          "cumplimiento_pct": 0.0
        },
        {
          "fecha": "2026-08-28",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 55.4
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-103",
          "cumplimiento_pct": 61.7
        },
        {
          "fecha": "2026-08-13",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 66.2
        },
        {
          "fecha": "2026-08-27",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-101",
          "cumplimiento_pct": 67.2
        },
        {
          "fecha": "2026-08-26",
          "turno": "Tarde",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 68.6
        },
        {
          "fecha": "2026-08-17",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-104",
          "cumplimiento_pct": 72.9
        },
        {
          "fecha": "2026-08-06",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-106",
          "cumplimiento_pct": 73.3
        },
        {
          "fecha": "2026-08-12",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-103",
          "cumplimiento_pct": 74.9
        },
        {
          "fecha": "2026-08-19",
          "turno": "Noche",
          "linea": "EXT-01",
          "operario": "OP-101",
          "cumplimiento_pct": 76.2
        },
        {
          "fecha": "2026-08-14",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-106",
          "cumplimiento_pct": 76.8
        },
        {
          "fecha": "2026-08-14",
          "turno": "Tarde",
          "linea": "EXT-02",
          "operario": "OP-105",
          "cumplimiento_pct": 77.4
        },
        {
          "fecha": "2026-08-05",
          "turno": "Noche",
          "linea": "TRZ-01",
          "operario": "OP-105",
          "cumplimiento_pct": 77.5
        },
        {
          "fecha": "2026-08-26",
          "turno": "Noche",
          "linea": "EXT-02",
          "operario": "OP-102",
          "cumplimiento_pct": 77.6
        },
        {
          "fecha": "2026-08-17",
          "turno": "Tarde",
          "linea": "TRZ-01",
          "operario": "OP-104",
          "cumplimiento_pct": 78.7
        },
        {
          "fecha": "2026-08-03",
          "turno": "Mañana",
          "linea": "EXT-01",
          "operario": "OP-106",
          "cumplimiento_pct": 79.3
        },
        {
          "fecha": "2026-08-04",
          "turno": "Mañana",
          "linea": "EXT-02",
          "operario": "OP-101",
          "cumplimiento_pct": 79.9
        }
      ]
    },
    "calidad": {
      "umbral_pct": 95,
      "promedio_pct": 97.8,
      "por_debajo_umbral": [
        {
          "tipo": "operario",
          "id": "OP-102",
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
  "reglas_no_evaluables": [
    {
      "regla": "R11",
      "motivo": "En TRZ-02 turno Tarde no hay al menos dos operarios con 2 o más turnos registrados en el período; no hay un par comparable (operarios con >=2 turnos: 0 de 1 operarios distintos)."
    },
    {
      "regla": "R11",
      "motivo": "En TRZ-03 turno Noche no hay al menos dos operarios con 2 o más turnos registrados en el período; no hay un par comparable (operarios con >=2 turnos: 0 de 1 operarios distintos)."
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
| R01-TRZ-02-2026-08-29-Tarde | R01 | Alta | 2026-08-29 | Tarde | TRZ-02 | Hora_Fin es menor o igual a Hora_Inicio en un turno que no es Noche. | Hora_Inicio = 22:01, Hora_Fin = 06:01, Turno = Tarde |
| R04-TRZ-01-2026-08-04-Tarde | R04 | Alta | 2026-08-04 | Tarde | TRZ-01 | Faltan campos obligatorios: Hora_Fin. | Campos vacíos: Hora_Fin |
| R04-EXT-02-2026-08-11-Tarde | R04 | Alta | 2026-08-11 | Tarde | EXT-02 | Faltan campos obligatorios: Operario. | Campos vacíos: Operario |
| R09-EXT-02-2026-W32 | R09 | Alta | 2026-08-03..2026-08-06 |  | EXT-02 | El motivo de parada 'falla electrica' se repite 6 veces en la semana en la misma línea. | 6 ocurrencias tras normalizar: 'Falla electrica' (3), 'falla electrica' (2), 'Falla eléctrica' (1), fechas: 2026-08-03, 2026-08-04, 2026-08-04, 2026-08-05, 2026-08-05, 2026-08-06 |
| R09-TRZ-01-2026-W32 | R09 | Alta | 2026-08-03..2026-08-07 |  | TRZ-01 | El motivo de parada 'falla mecanica' se repite 7 veces en la semana en la misma línea. | 7 ocurrencias tras normalizar: 'Falla mecanica' (7), fechas: 2026-08-03, 2026-08-03, 2026-08-04, 2026-08-06, 2026-08-06, 2026-08-06, 2026-08-07 |
| R09-EXT-01-2026-W33 | R09 | Alta | 2026-08-10..2026-08-14 |  | EXT-01 | El motivo de parada 'falta de insumo' se repite 5 veces en la semana en la misma línea. | 5 ocurrencias tras normalizar: 'Falta de insumo' (5), fechas: 2026-08-10, 2026-08-12, 2026-08-13, 2026-08-14, 2026-08-14 |
| R09-EXT-02-2026-W33 | R09 | Alta | 2026-08-12..2026-08-14 |  | EXT-02 | El motivo de parada 'falla electrica' se repite 5 veces en la semana en la misma línea. | 5 ocurrencias tras normalizar: 'falla electrica' (2), 'Falla electrica' (2), 'Falla eléctrica' (1), fechas: 2026-08-12, 2026-08-12, 2026-08-13, 2026-08-13, 2026-08-14 |
| R09-EXT-02-2026-W34 | R09 | Alta | 2026-08-17..2026-08-21 |  | EXT-02 | El motivo de parada 'falla electrica' se repite 4 veces en la semana en la misma línea. | 4 ocurrencias tras normalizar: 'falla electrica' (2), 'Falla electrica' (1), 'Falla eléctrica' (1), fechas: 2026-08-17, 2026-08-20, 2026-08-21, 2026-08-21 |
| R09-TRZ-01-2026-W34 | R09 | Alta | 2026-08-17..2026-08-19 |  | TRZ-01 | El motivo de parada 'mantenimiento programado' se repite 4 veces en la semana en la misma línea. | 4 ocurrencias tras normalizar: 'Mantenimiento programado' (4), fechas: 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-19 |
| R09-EXT-02-2026-W35 | R09 | Alta | 2026-08-24..2026-08-28 |  | EXT-02 | El motivo de parada 'falla electrica' se repite 7 veces en la semana en la misma línea. | 7 ocurrencias tras normalizar: 'Falla electrica' (3), 'falla electrica' (3), 'Falla eléctrica' (1), fechas: 2026-08-24, 2026-08-25, 2026-08-26, 2026-08-26, 2026-08-27, 2026-08-27, 2026-08-28 |
| R03-EXT-02-2026-08-07-Mañana | R03 | Media | 2026-08-07 | Mañana | EXT-02 | Parada registrada sin motivo cargado. | Tiempo_Parada_min = 20, Motivo_Parada = "" (vacío) |
| R03-EXT-02-2026-08-19-Tarde | R03 | Media | 2026-08-19 | Tarde | EXT-02 | Motivo de parada 'Otros' sin observaciones que lo expliquen. | Motivo_Parada = "Otros", Observaciones = "" (vacío) |
| R05-TRZ-01-2026-08-21-Tarde | R05 | Media | 2026-08-21 | Tarde | TRZ-01 | Producción cero con tiempo productivo mayor a 60 minutos. | Cant_Producida = 0, Tiempo_Productivo_min = 480 |
| R08a-EXT-02-2026-08-05 | R08a | Media | 2026-08-05 |  | EXT-02 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-05 en EXT-02, turnos: Mañana, Noche, Tarde |
| R08a-EXT-01-2026-08-06 | R08a | Media | 2026-08-06 |  | EXT-01 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-06 en EXT-01, turnos: Mañana, Noche, Tarde |
| R08a-TRZ-01-2026-08-06 | R08a | Media | 2026-08-06 |  | TRZ-01 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-06 en TRZ-01, turnos: Mañana, Noche, Tarde |
| R08a-TRZ-01-2026-08-07 | R08a | Media | 2026-08-07 |  | TRZ-01 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-07 en TRZ-01, turnos: Mañana, Noche, Tarde |
| R08a-TRZ-01-2026-08-11 | R08a | Media | 2026-08-11 |  | TRZ-01 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-11 en TRZ-01, turnos: Mañana, Noche, Tarde |
| R08a-EXT-02-2026-08-12 | R08a | Media | 2026-08-12 |  | EXT-02 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-12 en EXT-02, turnos: Mañana, Noche, Tarde |
| R08a-EXT-02-2026-08-13 | R08a | Media | 2026-08-13 |  | EXT-02 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-13 en EXT-02, turnos: Mañana, Noche, Tarde |
| R08a-EXT-02-2026-08-20 | R08a | Media | 2026-08-20 |  | EXT-02 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-20 en EXT-02, turnos: Mañana, Noche, Tarde |
| R08a-EXT-02-2026-08-21 | R08a | Media | 2026-08-21 |  | EXT-02 | Se registraron 3 paradas No Planificadas en la misma línea y fecha (más de 2). | 3 paradas No Planificadas el 2026-08-21 en EXT-02, turnos: Mañana, Noche, Tarde |
| R08b-EXT-01-2026-08-03 | R08b | Media | 2026-08-03 |  | EXT-01 | Tiempo de parada acumulado de 165 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 165 (Mañana=120, Tarde=0, Noche=45) |
| R08b-EXT-02-2026-08-03 | R08b | Media | 2026-08-03 |  | EXT-02 | Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 150 (Mañana=85, Tarde=0, Noche=65) |
| R08b-EXT-02-2026-08-04 | R08b | Media | 2026-08-04 |  | EXT-02 | Tiempo de parada acumulado de 175 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 175 (Mañana=80, Tarde=45, Noche=50) |
| R08b-EXT-02-2026-08-05 | R08b | Media | 2026-08-05 |  | EXT-02 | Tiempo de parada acumulado de 350 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 350 (Mañana=65, Tarde=120, Noche=165) |
| R08b-TRZ-01-2026-08-05 | R08b | Media | 2026-08-05 |  | TRZ-01 | Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 200 (Mañana=0, Tarde=90, Noche=110) |
| R08b-EXT-01-2026-08-06 | R08b | Media | 2026-08-06 |  | EXT-01 | Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 135 (Mañana=45, Tarde=45, Noche=45) |
| R08b-EXT-02-2026-08-11 | R08b | Media | 2026-08-11 |  | EXT-02 | Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 170 (Mañana=45, Tarde=45, Noche=80) |
| R08b-TRZ-01-2026-08-11 | R08b | Media | 2026-08-11 |  | TRZ-01 | Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 170 (Mañana=45, Tarde=95, Noche=30) |
| R08b-EXT-02-2026-08-12 | R08b | Media | 2026-08-12 |  | EXT-02 | Tiempo de parada acumulado de 170 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 170 (Mañana=50, Tarde=20, Noche=100) |
| R08b-EXT-02-2026-08-13 | R08b | Media | 2026-08-13 |  | EXT-02 | Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 250 (Mañana=140, Tarde=80, Noche=30) |
| R08b-EXT-02-2026-08-14 | R08b | Media | 2026-08-14 |  | EXT-02 | Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 250 (Mañana=120, Tarde=130, Noche=0) |
| R08b-TRZ-01-2026-08-14 | R08b | Media | 2026-08-14 |  | TRZ-01 | Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 200 (Mañana=60, Tarde=95, Noche=45) |
| R08b-EXT-02-2026-08-17 | R08b | Media | 2026-08-17 |  | EXT-02 | Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 150 (Mañana=50, Tarde=0, Noche=100) |
| R08b-EXT-01-2026-08-19 | R08b | Media | 2026-08-19 |  | EXT-01 | Tiempo de parada acumulado de 145 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 145 (Mañana=0, Tarde=80, Noche=65) |
| R08b-EXT-02-2026-08-20 | R08b | Media | 2026-08-20 |  | EXT-02 | Tiempo de parada acumulado de 150 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 150 (Mañana=45, Tarde=15, Noche=90) |
| R08b-EXT-02-2026-08-21 | R08b | Media | 2026-08-21 |  | EXT-02 | Tiempo de parada acumulado de 270 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 270 (Mañana=60, Tarde=115, Noche=95) |
| R08b-EXT-02-2026-08-25 | R08b | Media | 2026-08-25 |  | EXT-02 | Tiempo de parada acumulado de 175 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 175 (Mañana=20, Tarde=70, Noche=85) |
| R08b-EXT-01-2026-08-26 | R08b | Media | 2026-08-26 |  | EXT-01 | Tiempo de parada acumulado de 165 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 165 (Mañana=50, Tarde=60, Noche=55) |
| R08b-EXT-02-2026-08-26 | R08b | Media | 2026-08-26 |  | EXT-02 | Tiempo de parada acumulado de 255 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 255 (Mañana=0, Tarde=110, Noche=145) |
| R08b-TRZ-01-2026-08-26 | R08b | Media | 2026-08-26 |  | TRZ-01 | Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 135 (Mañana=45, Tarde=90, Noche=0) |
| R08b-EXT-02-2026-08-27 | R08b | Media | 2026-08-27 |  | EXT-02 | Tiempo de parada acumulado de 250 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 250 (Mañana=150, Tarde=15, Noche=85) |
| R08b-EXT-02-2026-08-28 | R08b | Media | 2026-08-28 |  | EXT-02 | Tiempo de parada acumulado de 200 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 200 (Mañana=180, Tarde=0, Noche=20) |
| R08b-TRZ-01-2026-08-28 | R08b | Media | 2026-08-28 |  | TRZ-01 | Tiempo de parada acumulado de 135 minutos en la línea y fecha (mayor a 120). | Suma Tiempo_Parada_min = 135 (Mañana=0, Tarde=75, Noche=60) |
| R12-EXT-01-2026-08-03-Tarde | R12 | Media | 2026-08-03 | Tarde | EXT-01 | Lote abierto con 19 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-03, OF_Lote = OF-4104, días hábiles posteriores hasta el corte = 19 |
| R12-EXT-02-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | EXT-02 | Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4114, días hábiles posteriores hasta el corte = 18 |
| R12-EXT-02-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | EXT-02 | Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4117, días hábiles posteriores hasta el corte = 18 |
| R12-TRZ-01-2026-08-04-Tarde | R12 | Media | 2026-08-04 | Tarde | TRZ-01 | Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4115, días hábiles posteriores hasta el corte = 18 |
| R12-TRZ-01-2026-08-04-Noche | R12 | Media | 2026-08-04 | Noche | TRZ-01 | Lote abierto con 18 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-04, OF_Lote = OF-4118, días hábiles posteriores hasta el corte = 18 |
| R12-TRZ-01-2026-08-06-Mañana | R12 | Media | 2026-08-06 | Mañana | TRZ-01 | Lote abierto con 16 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-06, OF_Lote = OF-4130, días hábiles posteriores hasta el corte = 16 |
| R12-TRZ-01-2026-08-06-Tarde | R12 | Media | 2026-08-06 | Tarde | TRZ-01 | Lote abierto con 16 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-06, OF_Lote = OF-4133, días hábiles posteriores hasta el corte = 16 |
| R12-EXT-01-2026-08-07-Tarde | R12 | Media | 2026-08-07 | Tarde | EXT-01 | Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4140, días hábiles posteriores hasta el corte = 15 |
| R12-EXT-01-2026-08-07-Noche | R12 | Media | 2026-08-07 | Noche | EXT-01 | Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4143, días hábiles posteriores hasta el corte = 15 |
| R12-TRZ-01-2026-08-07-Mañana | R12 | Media | 2026-08-07 | Mañana | TRZ-01 | Lote abierto con 15 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-07, OF_Lote = OF-4139, días hábiles posteriores hasta el corte = 15 |
| R12-EXT-01-2026-08-10-Mañana | R12 | Media | 2026-08-10 | Mañana | EXT-01 | Lote abierto con 14 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-10, OF_Lote = OF-4146, días hábiles posteriores hasta el corte = 14 |
| R12-EXT-01-2026-08-11-Mañana | R12 | Media | 2026-08-11 | Mañana | EXT-01 | Lote abierto con 13 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-11, OF_Lote = OF-4155, días hábiles posteriores hasta el corte = 13 |
| R12-EXT-01-2026-08-12-Tarde | R12 | Media | 2026-08-12 | Tarde | EXT-01 | Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4167, días hábiles posteriores hasta el corte = 12 |
| R12-EXT-02-2026-08-12-Noche | R12 | Media | 2026-08-12 | Noche | EXT-02 | Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4171, días hábiles posteriores hasta el corte = 12 |
| R12-TRZ-01-2026-08-12-Mañana | R12 | Media | 2026-08-12 | Mañana | TRZ-01 | Lote abierto con 12 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-12, OF_Lote = OF-4166, días hábiles posteriores hasta el corte = 12 |
| R12-EXT-01-2026-08-13-Mañana | R12 | Media | 2026-08-13 | Mañana | EXT-01 | Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4173, días hábiles posteriores hasta el corte = 11 |
| R12-EXT-01-2026-08-13-Noche | R12 | Media | 2026-08-13 | Noche | EXT-01 | Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4179, días hábiles posteriores hasta el corte = 11 |
| R12-TRZ-01-2026-08-13-Tarde | R12 | Media | 2026-08-13 | Tarde | TRZ-01 | Lote abierto con 11 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-13, OF_Lote = OF-4178, días hábiles posteriores hasta el corte = 11 |
| R12-TRZ-01-2026-08-14-Noche | R12 | Media | 2026-08-14 | Noche | TRZ-01 | Lote abierto con 10 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-14, OF_Lote = OF-4190, días hábiles posteriores hasta el corte = 10 |
| R12-EXT-02-2026-08-17-Noche | R12 | Media | 2026-08-17 | Noche | EXT-02 | Lote abierto con 9 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-17, OF_Lote = OF-4198, días hábiles posteriores hasta el corte = 9 |
| R12-EXT-02-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | EXT-02 | Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4201, días hábiles posteriores hasta el corte = 8 |
| R12-EXT-02-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | EXT-02 | Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4204, días hábiles posteriores hasta el corte = 8 |
| R12-TRZ-01-2026-08-18-Mañana | R12 | Media | 2026-08-18 | Mañana | TRZ-01 | Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4202, días hábiles posteriores hasta el corte = 8 |
| R12-TRZ-01-2026-08-18-Tarde | R12 | Media | 2026-08-18 | Tarde | TRZ-01 | Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4205, días hábiles posteriores hasta el corte = 8 |
| R12-TRZ-01-2026-08-18-Noche | R12 | Media | 2026-08-18 | Noche | TRZ-01 | Lote abierto con 8 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-18, OF_Lote = OF-4208, días hábiles posteriores hasta el corte = 8 |
| R12-EXT-02-2026-08-19-Tarde | R12 | Media | 2026-08-19 | Tarde | EXT-02 | Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4213, días hábiles posteriores hasta el corte = 7 |
| R12-TRZ-01-2026-08-19-Mañana | R12 | Media | 2026-08-19 | Mañana | TRZ-01 | Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4211, días hábiles posteriores hasta el corte = 7 |
| R12-TRZ-01-2026-08-19-Noche | R12 | Media | 2026-08-19 | Noche | TRZ-01 | Lote abierto con 7 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-19, OF_Lote = OF-4217, días hábiles posteriores hasta el corte = 7 |
| R12-EXT-01-2026-08-20-Mañana | R12 | Media | 2026-08-20 | Mañana | EXT-01 | Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4218, días hábiles posteriores hasta el corte = 6 |
| R12-EXT-02-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | EXT-02 | Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4225, días hábiles posteriores hasta el corte = 6 |
| R12-TRZ-01-2026-08-20-Noche | R12 | Media | 2026-08-20 | Noche | TRZ-01 | Lote abierto con 6 días hábiles transcurridos sin cerrarse (corte 2026-08-30). | Estado_Lote = Abierto, Fecha = 2026-08-20, OF_Lote = OF-4226, días hábiles posteriores hasta el corte = 6 |
| R11-EXT-01-Noche | R11 | Baja |  | Noche | EXT-01 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-101 (OEE=73.5%) vs OP-102 (OEE=83.9%) dif=10.4pts; OP-102 (OEE=83.9%) vs OP-104 (OEE=66.4%) dif=17.5pts; OP-103 (OEE=78.4%) vs OP-104 (OEE=66.4%) dif=11.9pts; OP-104 (OEE=66.4%) vs OP-105 (OEE=80.8%) dif=14.4pts; OP-104 (OEE=66.4%) vs OP-106 (OEE=81.5%) dif=15.0pts |
| R11-EXT-02-Mañana | R11 | Baja |  | Mañana | EXT-02 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-101 (OEE=74.6%) vs OP-104 (OEE=57.3%) dif=17.3pts; OP-103 (OEE=83.6%) vs OP-104 (OEE=57.3%) dif=26.3pts; OP-103 (OEE=83.6%) vs OP-106 (OEE=70.8%) dif=12.8pts; OP-104 (OEE=57.3%) vs OP-105 (OEE=76.7%) dif=19.4pts; OP-104 (OEE=57.3%) vs OP-106 (OEE=70.8%) dif=13.6pts |
| R11-EXT-02-Tarde | R11 | Baja |  | Tarde | EXT-02 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-102 (OEE=72.0%) vs OP-106 (OEE=84.3%) dif=12.3pts; OP-104 (OEE=73.1%) vs OP-106 (OEE=84.3%) dif=11.2pts; OP-105 (OEE=72.1%) vs OP-106 (OEE=84.3%) dif=12.3pts |
| R11-EXT-02-Noche | R11 | Baja |  | Noche | EXT-02 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-101 (OEE=72.3%) vs OP-105 (OEE=84.9%) dif=12.6pts; OP-102 (OEE=70.8%) vs OP-105 (OEE=84.9%) dif=14.1pts; OP-103 (OEE=70.1%) vs OP-105 (OEE=84.9%) dif=14.8pts; OP-104 (OEE=68.0%) vs OP-105 (OEE=84.9%) dif=16.9pts; OP-105 (OEE=84.9%) vs OP-106 (OEE=64.4%) dif=20.6pts |
| R11-TRZ-01-Tarde | R11 | Baja |  | Tarde | TRZ-01 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-101 (OEE=73.9%) vs OP-103 (OEE=85.8%) dif=11.9pts; OP-103 (OEE=85.8%) vs OP-104 (OEE=69.5%) dif=16.3pts |
| R11-TRZ-01-Noche | R11 | Baja |  | Noche | TRZ-01 | Diferencia mayor a 10 puntos de OEE entre operarios en la misma línea y turno. | OP-103 (OEE=80.0%) vs OP-105 (OEE=68.7%) dif=11.4pts; OP-104 (OEE=72.0%) vs OP-106 (OEE=83.7%) dif=11.8pts; OP-105 (OEE=68.7%) vs OP-106 (OEE=83.7%) dif=15.1pts |
| R13-TRZ-02-2026-08-29-Tarde | R13 | Baja | 2026-08-29 | Tarde | TRZ-02 | Motivo_Parada fuera del catálogo cerrado de motivos. | Motivo_Parada = "aa" |
| R13-TRZ-03-2026-08-30-Noche | R13 | Baja | 2026-08-30 | Noche | TRZ-03 | Motivo_Parada fuera del catálogo cerrado de motivos. | Motivo_Parada = "x" |
