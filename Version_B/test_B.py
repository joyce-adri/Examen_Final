# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1(self):
        plazo = 120
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: mini nevera electrolux")

    def test_tema1_prueba_2(self):
        plazo = 180
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: minicomponente LG")

    def test_tema1_prueba_3(self):
        plazo = 360
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: tv led LG")


    '''
    def test_tema2_prueba_1(self):
        tipoCliente = "AAA"
        monto = 20001
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Gold")

    def test_tema2_prueba_2(self):
        tipoCliente = "AAA"
        monto = 19999
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_3(self):
        tipoCliente = "AA"
        monto = 16000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Platinum")

    def test_tema2_prueba_4(self):
        tipoCliente = "A"
        monto = 14000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Internacional")

    def test_tema2_prueba_5(self):
        tipoCliente = "B"
        monto = 6000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Club Miles")

    def test_tema2_prueba_6(self):
        tipoCliente = "C"
        monto = 4000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Advantage")

    def test_tema2_prueba_7(self):
        tipoCliente = "AA"
        monto = 13000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_8(self):
        tipoCliente = "A"
        monto = 9000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_9(self):
        tipoCliente = "B"
        monto = 4000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_10(self):
        tipoCliente = "C"
        monto = 2000
        tarjeta = tema2.ofrecer_tarjeta_con_chip(monto, tipoCliente)
        self.assertEquals(tarjeta, "Tipo de tarjeta: Clasica")
    '''
if __name__ == '__main__':
    unittest.main()
