#!/usr/bin/env python3
import sys

totalVentas = 0
ciudadAnterior = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    ciudad, importe = data

    if ciudadAnterior and ciudadAnterior != ciudad:
        print(ciudadAnterior, "\t", totalVentas)
        ciudadAnterior = ciudad  # ??
        totalVentas = 0

    ciudadAnterior = ciudad
    totalVentas += float(importe)

if ciudadAnterior != None:
    print(ciudadAnterior, "\t", totalVentas)
