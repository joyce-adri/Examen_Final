# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    def test_tema1_prueba_1(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(10)
        esperado = "escala: A++ , eficiencia: los más eficientes"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(40)
        # print(etiqueta)
        esperado = "escala: A+ , eficiencia: los más eficientes"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(50)
        # print(etiqueta)
        esperado = "escala: A , eficiencia: los más eficientes"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(60)
        # print(etiqueta)
        esperado = "escala: B , eficiencia: los más eficientes"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_5(self):
        etiqueta = tema1.etiquetado_consumo_energia(80)
        esperado = "escala: C , eficiencia: los más eficientes"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(95)
        # print(etiqueta)
        esperado = "escala: D , eficiencia: consumo medio"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(105)
        # print(etiqueta)
        esperado = "escala: E , eficiencia: consumo medio"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(120)
        # print(etiqueta)
        esperado = "escala: F , eficiencia: alto consumo energético"
        self.assertEquals(esperado, etiqueta)
    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(130)
        # print(etiqueta)
        esperado = "escala: G , eficiencia: alto consumo energético"
        self.assertEquals(esperado, etiqueta)

    # INICIO DE TEMA 2

    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(35000, False)
        esperado = "Tipo de cliente: no es digno de crédito, Envio de boletin: No"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(35000, True)
        esperado = "Tipo de cliente: AAA, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(25000, True)
        esperado = "Tipo de cliente: AA, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(17000, True)
        esperado = "Tipo de cliente: A, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_5(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(12000, True)
        esperado = "Tipo de cliente: B, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_6(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(7000, True)
        esperado = "Tipo de cliente: C, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)
    def test_tema2_prueba_7(self):
        # inserte su codigo de prueba
        obtenido = tema2.clasificacion_clientes(4000, True)
        esperado = "Tipo de cliente: no es digno de crédito, Envio de boletin: Si"
        self.assertEquals(esperado, obtenido)

if __name__ == '__main__':
    unittest.main()