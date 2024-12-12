#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Eliminar espacios iniciales y finales
    line = line.strip()
    # Separar línea el palabras
    year, hour, city, cat, price, card = line.split("\t")
    print("%s\t%s" % (city, price))
