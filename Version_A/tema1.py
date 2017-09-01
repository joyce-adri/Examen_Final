# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def etiquetado_consumo_energia(porcentaje):
    clasificacion_escala_int = "ninguna"
    rango = "ninguno"
    if porcentaje >= 0 and porcentaje < 90: # [0, 90)
        rango = "los más eficientes"
        if porcentaje < 30 and porcentaje >= 0 : # [0, 30)
            clasificacion_escala_int = "A++"
        elif porcentaje >= 30 and porcentaje < 42 : # [30, 42)
            clasificacion_escala_int = "A+"
        elif porcentaje >= 42 and porcentaje < 55 : # [42, 55)
            clasificacion_escala_int = "A"
        elif porcentaje >= 55 and porcentaje < 75 : # [55, 75)
            clasificacion_escala_int = "B"
        elif porcentaje >= 75 and porcentaje < 90 : # [75, 90)
            clasificacion_escala_int = "C"
    elif porcentaje >= 90 and porcentaje < 110: # [90, 110)
        rango = "consumo medio"
        if porcentaje >= 90 and porcentaje < 100 : # [90, 100)
            clasificacion_escala_int = "D"
        elif porcentaje >= 100 and porcentaje < 110 : # [100, 110)
            clasificacion_escala_int = "E"
    elif porcentaje >= 110: # [110, Infinity)
        rango = "alto consumo energético"
        if porcentaje >= 110 and porcentaje <= 125 : # [110, 125]
            clasificacion_escala_int = "F"
        elif porcentaje > 125 : # [126, Infinity)
            clasificacion_escala_int = "G"
    etiqueta = "escala: %s , eficiencia: %s" % (clasificacion_escala_int, rango)
    return etiqueta