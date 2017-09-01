# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1(self):
        # plazo=120, montoInversion>50001
        plazo = 120
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: mini nevera electrolux")
    def test_tema1_prueba_2(self):
        # plazo=120, montoInversion=50001
        plazo = 120
        montoInversion = 50001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: mini nevera electrolux")
    def test_tema1_prueba_3(self):
        # plazo=120, montoInversion > 20001 and montoInversion < 50001
        plazo = 120
        montoInversion = 35000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: aspiradora electrolux")
    def test_tema1_prueba_4(self):
        # plazo=120, montoInversion=20001
        plazo = 120
        montoInversion = 20001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: aspiradora electrolux")
    def test_tema1_prueba_5(self):
        # plazo=120, montoInversion > 10001 and montoInversion < 20001
        plazo = 120
        montoInversion = 15000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: arrocera electrolux")
    def test_tema1_prueba_6(self):
        # plazo=120, montoInversion=10001
        plazo = 120
        montoInversion = 10001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: arrocera electrolux")
    def test_tema1_prueba_7(self):
        # plazo=120, montoInversion<10001
        plazo = 120
        montoInversion = 10000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: no recibe premio")
    def test_tema1_prueba_8(self):
        # plazo=180, montoInversion>50001
        plazo = 180
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: minicomponente LG")
    def test_tema1_prueba_9(self):
        # plazo=180, montoInversion>50001
        plazo = 180
        montoInversion = 50001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: minicomponente LG")
    def test_tema1_prueba_10(self):
        # plazo=180, montoInversion > 20001 and montoInversion < 50001
        plazo = 180
        montoInversion = 35000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: samsumg galaxy J1")
    def test_tema1_prueba_11(self):
        # plazo=180, montoInversion=20001
        plazo = 180
        montoInversion = 20001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: samsumg galaxy J1")
    def test_tema1_prueba_12(self):
        # plazo=180, montoInversion > 10001 and montoInversion < 20001
        plazo = 180
        montoInversion = 15000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: licuadora electrolux")
    def test_tema1_prueba_13(self):
        # plazo=180, montoInversion = 10001
        plazo = 180
        montoInversion = 10001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: licuadora electrolux")
    def test_tema1_prueba_14(self):
        # plazo=180, montoInversion<10001
        plazo = 180
        montoInversion = 10000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: no recibe premio")
    def test_tema1_prueba_15(self):
        # plazo=360, montoInversion>50001
        plazo = 360
        montoInversion = 50002
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: tv led LG")
    def test_tema1_prueba_16(self):
        # plazo=360, montoInversion>50001
        plazo = 360
        montoInversion = 50001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: tv led LG")
    def test_tema1_prueba_17(self):
        # plazo=360, montoInversion > 20001 and montoInversion < 50001
        plazo = 360
        montoInversion = 35000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: tablet samsumg")
    def test_tema1_prueba_18(self):
        # plazo=360, montoInversion=20001
        plazo = 360
        montoInversion = 20001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: tablet samsumg")
    def test_tema1_prueba_19(self):
        # plazo=360, montoInversion > 10001 and montoInversion < 20001
        plazo = 360
        montoInversion = 15000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: microondas electrolux")
    def test_tema1_prueba_20(self):
        # plazo=360, montoInversion = 10001
        plazo = 360
        montoInversion = 10001
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: microondas electrolux")
    def test_tema1_prueba_21(self):
        # plazo=360, montoInversion<10001
        plazo = 360
        montoInversion = 10000
        premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(premio, "Tipo de premio: no recibe premio")

    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 10
        tipoCliente = "Z"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 20000
        tipoCliente = "AAA"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Gold")
    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 17000
        tipoCliente = "AA"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Platinum")
    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 14000
        tipoCliente = "AA"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_5(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 21000
        tipoCliente = "AA"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_6(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 12000
        tipoCliente = "A"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Internacional")
    def test_tema2_prueba_7(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 9000
        tipoCliente = "A"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_8(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 16000
        tipoCliente = "A"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_9(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 8000
        tipoCliente = "B"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Club Miles")
    def test_tema2_prueba_10(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 4000
        tipoCliente = "B"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_11(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 11000
        tipoCliente = "B"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_12(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 4000
        tipoCliente = "C"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Advantage")
    def test_tema2_prueba_13(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 2000
        tipoCliente = "C"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")
    def test_tema2_prueba_14(self):
        # inserte su codigo de prueba
        montoEndeudamiento = 6000
        tipoCliente = "C"
        tipoTarjeta = tema2.ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente)
        self.assertEquals(tipoTarjeta, "Tipo de tarjeta: Clasica")



if __name__ == '__main__':
    unittest.main()
