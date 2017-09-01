# -*- coding: utf-8 -*-


import unittest
from tema1 import *
import tema1
import tema2


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1(self):
        plazo = 120
        monto = 15000

        msg = tema1.premios_depositos_plazo_fijo(plazo,monto)
        self.assertEquals(msg, "Arrocera Electrolux 1.8L")

    def test_tema1_prueba_2(self):
        plazo = 120
        monto = 28000

        msg = tema1.premios_depositos_plazo_fijo(plazo,monto)
        self.assertEquals(msg, "Aspiradora Electrolux")

    def test_tema1_prueba_3(self):
        plazo = 120
        monto = 55000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Mini nevera 5 pies Electrolux")

    def test_tema1_prueba_4(self):
        plazo = 180
        monto = 16000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Licuadora 5 velocidades Electrolux")

    def test_tema1_prueba_5(self):
        plazo = 180
        monto = 35000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Samsung Galaxy J1")

    def test_tema1_prueba_6(self):
        plazo = 180
        monto = 60000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Minicomponente LG")

    def test_tema1_prueba_7(self):
        plazo = 360
        monto = 12000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Microondas Electrolux 20L")

    def test_tema1_prueba_8(self):
        plazo = 360
        monto = 40000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Tablet Samsung")

    def test_tema1_prueba_9(self):
        plazo = 360
        monto = 70000

        msg = tema1.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Tv LED 32 LG")

    def test_tema2_prueba_1(self):
        tipo_cliente = "AAA"
        monto = 20000

        msg = tema2.ofrecer_tarjeta_con_chip(monto,tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Gold")

    def test_tema2_prueba_2(self):
        tipo_cliente = "AA"
        monto = 16000

        msg = tema2.ofrecer_tarjeta_con_chip(monto, tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Platinum")

    def test_tema2_prueba_3(self):
        tipo_cliente = "A"
        monto = 12000

        msg = tema2.ofrecer_tarjeta_con_chip(monto, tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Internacional")
    def test_tema2_prueba_4(self):
        tipo_cliente = "B"
        monto = 6000

        msg = tema2.ofrecer_tarjeta_con_chip(monto, tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Club Miles")

    def test_tema2_prueba_5(self):
        tipo_cliente = "C"
        monto = 4000

        msg = tema2.ofrecer_tarjeta_con_chip(monto, tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Advantage")

    def test_tema2_prueba_6(self):
        tipo_cliente = "D"
        monto = 2000

        msg = tema2.ofrecer_tarjeta_con_chip(monto, tipo_cliente)
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")


if __name__ == '__main__':
    unittest.main()
