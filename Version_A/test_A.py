# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
    def test_tema1_prueba_1(self):
        porcentaje = 85
        mensaje = tema1.etiquetado_consumo_energia(porcentaje)
        self.assertEquals(mensaje, "escala: C , eficiencia: los más eficientes")

    def test_tema1_prueba_2(self):
        porcentaje = 105
        mensaje = tema1.etiquetado_consumo_energia(porcentaje)
        self.assertEquals(mensaje, "escala: E , eficiencia: consumo medio")

    def test_tema1_prueba_3(self):
        porcentaje = 130
        mensaje = tema1.etiquetado_consumo_energia(porcentaje)
        self.assertEquals(mensaje, "escala: G , eficiencia: alto consumo energético")

    def test_tema2_prueba_1(self):
        monto = 30000
        informacion = True
        mensaje = tema2.clasificacion_clientes(monto, informacion)
        self.assertEquals(mensaje, "Tipo de cliente: AAA, Envio de boletin: Si")

    def test_tema2_prueba_2(self):
        monto = 30000
        informacion = False
        mensaje = tema2.clasificacion_clientes(monto, informacion)
        self.assertEquals(mensaje, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
    unittest.main()