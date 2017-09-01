# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def premio_por_deposito_a_plazo_fijo(plazo, montoInversion):
    premio = "no recibe premio"
    if plazo is 120:
        if montoInversion >= 50001:
            premio = "mini nevera electrolux"
        elif montoInversion >= 20001 and montoInversion < 50001:
            premio = "aspiradora electrolux"
        elif montoInversion >= 10001 and montoInversion < 20001:
            premio = "arrocera electrolux"
    elif plazo is 180:
        if montoInversion >= 50001:
            premio = "minicomponente LG"
        elif montoInversion >= 20001 and montoInversion < 50001:
            premio = "samsumg galaxy J1"
        elif montoInversion >= 10001 and montoInversion < 20001:
            premio = "licuadora electrolux"
    elif plazo is 360:
        if montoInversion >= 50001:
            premio = "tv led LG"
        elif montoInversion >= 20001 and montoInversion < 50001:
            premio = "tablet samsumg"
        elif montoInversion >= 10001 and montoInversion < 20001:
            premio = "microondas electrolux"
    return "Tipo de premio: %s" % premio