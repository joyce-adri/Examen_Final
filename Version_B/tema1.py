# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Premios:
    def premios_depositos_plazo_fijo(self,plazo,monto):
        if monto>10000 & monto < 20001:
             # se ejecuta otro codigo
            if plazo==120:
    	     return "Arrocera Electrolux"
            elif plazo== 180:
             return "Licuadora 5 Velocidades"
            else:
             return "Microondas Electrolux"
        elif monto>20000 & monto < 50001:
        # se ejecuta otro codigo
            if plazo == 120:
                return "Aspiradora Electrolux"
            elif plazo == 180:
                return "Samsung Galaxy j1"
            else:
                return "Tablet Samsung"
        elif monto>50000:
        # se ejecuta otro codigo
            if plazo == 120:
                return "mini nevera 5 pies"
            elif plazo == 180:
                return "minicomponente LG"
            else:
                return "tv LED 32 LG"