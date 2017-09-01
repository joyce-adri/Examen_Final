# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Tarjeta():
    def obtener(self, tipo, monto):
        if tipo == "AAA" and monto >= 20000:
           return "gold"
        elif tipo == "AA" and monto >= 15000:
            return "platinum"
        elif tipo == "A" and monto >= 10000:
                return "internacional"
        elif tipo == "B" and monto >= 5000:
            return "club miles"
        elif tipo == "C" and monto >= 3000:
            return "advantage"
        else:
            return "-"