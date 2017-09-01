# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        resultado = tema1.etiquetado_consumo_energia(-10)
        esperado = "escala: ninguna , eficiencia: ninguno"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_2(self):
        resultado = tema1.etiquetado_consumo_energia(0)
        esperado = "escala: A++ , eficiencia: los más eficientes"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_3(self):
        resultado = tema1.etiquetado_consumo_energia(31)
        esperado = "escala: A+ , eficiencia: los más eficientes"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_4(self):
        resultado = tema1.etiquetado_consumo_energia(42)
        esperado = "escala: A , eficiencia: los más eficientes"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_5(self):
        resultado = tema1.etiquetado_consumo_energia(74)
        esperado = "escala: B , eficiencia: los más eficientes"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_6(self):
        resultado = tema1.etiquetado_consumo_energia(75)
        esperado = "escala: C , eficiencia: los más eficientes"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_7(self):
        resultado = tema1.etiquetado_consumo_energia(90)
        esperado = "escala: D , eficiencia: consumo medio"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_8(self):
        resultado = tema1.etiquetado_consumo_energia(100)
        esperado = "escala: E , eficiencia: consumo medio"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_9(self):
        resultado = tema1.etiquetado_consumo_energia(110)
        esperado = "escala: F , eficiencia: alto consumo energético"
        self.assertEquals(resultado, esperado)

    def test_tema1_prueba_10(self):
        resultado = tema1.etiquetado_consumo_energia(130)
        esperado = "escala: G , eficiencia: alto consumo energético"
        self.assertEquals(resultado, esperado)

##INICIA TEMA 2
    def test_tema2_prueba_1(self):
        resultado = tema2.clasificacion_clientes(3000,False)
        esperado = "Tipo de cliente: no es digno de crédito, Envio de boletin: No"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_2(self):
        resultado = tema2.clasificacion_clientes(30000,True)
        esperado = "Tipo de cliente: AAA, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_3(self):
        resultado = tema2.clasificacion_clientes(25000,True)
        esperado = "Tipo de cliente: AA, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_4(self):
        resultado = tema2.clasificacion_clientes(15000,True)
        esperado = "Tipo de cliente: A, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_5(self):
        resultado = tema2.clasificacion_clientes(10000,True)
        esperado = "Tipo de cliente: B, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_6(self):
        resultado = tema2.clasificacion_clientes(5000,True)
        esperado = "Tipo de cliente: C, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)

    def test_tema2_prueba_7(self):
        resultado = tema2.clasificacion_clientes(2000,True)
        esperado = "Tipo de cliente: no es digno de crédito, Envio de boletin: Si"
        self.assertEquals(resultado, esperado)


if __name__ == '__main__':
    unittest.main()