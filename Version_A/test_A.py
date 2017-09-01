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
        prueba = tema1.etiquetado_consumo_energia(25)
        esperado = tema1.etiquetado_consumo_energia(0)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(40)
        esperado = tema1.etiquetado_consumo_energia(30)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(50)
        esperado = tema1.etiquetado_consumo_energia(42)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(70)
        esperado = tema1.etiquetado_consumo_energia(55)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(85)
        esperado = tema1.etiquetado_consumo_energia(75)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(95)
        esperado = tema1.etiquetado_consumo_energia(90)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(105)
        esperado = tema1.etiquetado_consumo_energia(100)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(120)
        esperado = tema1.etiquetado_consumo_energia(110)
        self.assertEquals(prueba, esperado)

    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        prueba = tema1.etiquetado_consumo_energia(130)
        esperado = tema1.etiquetado_consumo_energia(126)
        self.assertEquals(prueba, esperado)

    

    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        monto = 35000
        buro = True
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(30000, True)
        self.assertEquals(mensaje1, mensaje2)

    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        monto = 25000
        buro = True
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(20000, True)
        self.assertEquals(mensaje1, mensaje2)
        
    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        monto = 17000
        buro = True
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(15000, True)
        self.assertEquals(mensaje1, mensaje2)

    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        monto = 12000
        buro = True
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(10000, True)
        self.assertEquals(mensaje1, mensaje2)

    def test_tema2_prueba_5(self):
        # inserte su codigo de prueba
        monto = 7000
        buro = True
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(5000, True)
        self.assertEquals(mensaje1, mensaje2)

    def test_tema2_prueba_6(self):
        # inserte su codigo de prueba
        monto = 7000
        buro = False
        mensaje1 = tema2.clasificacion_clientes(monto, buro)
        mensaje2 = tema2.clasificacion_clientes(6000, False)
        self.assertEquals(mensaje1, mensaje2)


if __name__ == '__main__':
    unittest.main()