# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def etiquetado_consumo_energia(porcentaje):
    clasificacion_escala_int = "ninguna"
    rango = "ninguno"
    if porcentaje >= 0 and porcentaje < 90: #1
        rango = "los más eficientes" #2
        if porcentaje < 30 and porcentaje >= 0 : #3
            clasificacion_escala_int = "A++" #4
        elif porcentaje >= 30 and porcentaje < 42 : #5
            clasificacion_escala_int = "A+" #6
        elif porcentaje >= 42 and porcentaje < 55 : #7
            clasificacion_escala_int = "A"  #8
        elif porcentaje >= 55 and porcentaje < 75 : #9
            clasificacion_escala_int = "B" #10
        elif porcentaje >= 75 and porcentaje < 90 : #11
            clasificacion_escala_int = "C" #12
    elif porcentaje >= 90 and porcentaje < 110: #13
        rango = "consumo medio"#14
        if porcentaje >= 90 and porcentaje < 100 : #15
            clasificacion_escala_int = "D" #16
        elif porcentaje >= 100 and porcentaje < 110 : #17
            clasificacion_escala_int = "E" #18
    elif porcentaje >= 110: #19
        rango = "alto consumo energético" #20
        if porcentaje >= 110 and porcentaje <= 125 : #21
            clasificacion_escala_int = "F" #22
        elif porcentaje > 125 : #23
            clasificacion_escala_int = "G" #24
    etiqueta = "escala: %s , eficiencia: %s" % (clasificacion_escala_int, rango) #25
    return etiqueta #26