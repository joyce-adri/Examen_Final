# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Banco:

    def premios_depositos_plazo_fijo(self,dias, monto):
        if (dias == 120):
            if(monto>=10.001 and monto <=20000):
                return "Arrocera Electrolux 1.8L"
            elif(monto>=20.001 and monto <=50000):
                return "Aspiradora Electrolux"
            elif (monto > 50.001):
                return "Mini nevera 5 pies Electrolux"

        elif (dias==180):
            if (monto >= 10.001 and monto <= 20000):
                return "Licuadora 5 velocidades Electrolux"
            elif (monto >= 20.001 and monto <= 50000):
                return "Samsung Galaxy J1"
            elif (monto > 50.001):
                return "Minicomponente LG"

        elif (dias==360):
            if (monto >= 10.001 and monto <= 20000):
                return "Microondas Electrolux 20L"
            elif (monto >= 20.001 and monto <= 50000):
                return "Tablet Samsung"
            elif (monto > 50.001):
                return "Tv LED 32 LG"
