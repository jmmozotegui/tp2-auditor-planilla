#!/usr/bin/env python3
"""
Verificación independiente de R11 — cálculo determinístico fuera del agente.

Aplica la regla tal como está escrita en el contrato, sin intervención de un modelo:
    R11: diferencia mayor a 10 puntos entre el OEE de dos operarios en la misma
    Maquina_Linea y el mismo Turno. El OEE de un operario en esa combinación es
    el promedio simple de sus filas. Solo entran operarios con 2 o más turnos
    registrados en esa combinación.

Sirve como oráculo: permite decidir si una corrida del agente acertó o no,
sin depender de otra corrida del agente.

Uso:  python3 verificacion_r11.py planilla_produccion_mes.csv
"""
import csv, sys, collections, statistics

UMBRAL = 10.0
MIN_TURNOS = 2


def cargar(ruta):
    grupos = collections.defaultdict(lambda: collections.defaultdict(list))
    for fila in csv.DictReader(open(ruta, encoding="utf-8")):
        operario = (fila["Operario"] or "").strip()
        oee = (fila["OEE_pct"] or "").strip()
        if not operario or not oee:
            continue  # sin operario o sin OEE: no imputable, se declara aparte
        grupos[(fila["Maquina_Linea"], fila["Turno"])][operario].append(float(oee))
    return grupos


def evaluar(grupos):
    hallazgos, no_evaluables = [], []
    for clave in sorted(grupos):
        elegibles = {op: statistics.mean(v) for op, v in grupos[clave].items()
                     if len(v) >= MIN_TURNOS}
        if len(elegibles) < 2:
            no_evaluables.append((clave, len(elegibles)))
            continue
        alto = max(elegibles, key=elegibles.get)
        bajo = min(elegibles, key=elegibles.get)
        dif = elegibles[alto] - elegibles[bajo]
        if dif > UMBRAL:
            hallazgos.append({
                "id": f"R11-{clave[0]}-{clave[1]}",
                "diferencia": round(dif, 2),
                "mejor": (alto, round(elegibles[alto], 2), len(grupos[clave][alto])),
                "peor": (bajo, round(elegibles[bajo], 2), len(grupos[clave][bajo])),
            })
    return hallazgos, no_evaluables


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "planilla_produccion_mes.csv"
    hallazgos, no_evaluables = evaluar(cargar(ruta))

    print(f"R11 — hallazgos esperados: {len(hallazgos)}\n")
    for h in hallazgos:
        mo, mv, mn = h["mejor"]
        po, pv, pn = h["peor"]
        print(f"  {h['id']:<24} dif {h['diferencia']:>6.2f}   "
              f"{mo}={mv} ({mn} turnos) vs {po}={pv} ({pn} turnos)")

    print(f"\nCombinaciones sin par comparable: {len(no_evaluables)}")
    for clave, n in no_evaluables:
        print(f"  {clave[0]}/{clave[1]}: {n} operario(s) con {MIN_TURNOS}+ turnos")

    print("\nIDs esperados:")
    for h in hallazgos:
        print(h["id"])
