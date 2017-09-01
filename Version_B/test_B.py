# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

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

def ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente):
    tipoTarjeta = "Clasica"
    if tipoCliente == "AAA":
        if montoEndeudamiento >= 20000:
            tipoTarjeta = "Gold"
    elif tipoCliente == "AA":
        if montoEndeudamiento >= 15000 and montoEndeudamiento < 20000:
            tipoTarjeta = "Platinum"
    elif tipoCliente == "A":
        if montoEndeudamiento >= 10000 and montoEndeudamiento < 15000:
            tipoTarjeta = "Internacional"
    elif tipoCliente == "B":
        if montoEndeudamiento >= 5000 and montoEndeudamiento < 10000:
            tipoTarjeta = "Club Miles"
    elif tipoCliente == "C":
        if montoEndeudamiento >= 3000 and montoEndeudamiento < 5000:
            tipoTarjeta = "Advantage"
    return "Tipo de tarjeta: %s" % tipoTarjeta


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=50002)
        self.assertEquals(premio, "Tipo de premio: mini nevera electrolux")

    def test_tema1_prueba_2(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=20002)
        self.assertEquals(premio, "Tipo de premio: aspiradora electrolux")

    def test_tema1_prueba_3(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=10002)
        self.assertEquals(premio, "Tipo de premio: arrocera electrolux")

    def test_tema1_prueba_4(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=50002)
    	self.assertEquals(premio, "Tipo de premio: minicomponente LG")

    def test_tema1_prueba_5(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=20002)
    	self.assertEquals(premio, "Tipo de premio: samsumg galaxy J1")

    def test_tema1_prueba_6(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=10002)
    	self.assertEquals(premio, "Tipo de premio: licuadora electrolux")

    def test_tema1_prueba_7(self):
    	premio = premio_por_deposito_a_plazo_fijo(360, 50001)
    	self.assertEquals(premio, "Tipo de premio: tv led LG")

    def test_tema1_prueba_8(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=360, montoInversion=20001)
    	self.assertEquals(premio, "Tipo de premio: tablet samsumg")

    def test_tema1_prueba_9(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=360, montoInversion=10001)
    	self.assertEquals(premio, "Tipo de premio: microondas electrolux")







    def test_tema2_prueba_1(self):
    	premio = ofrecer_tarjeta_con_chip(montoEndeudamiento=20001, tipoCliente="AAA")
    	self.assertEquals(premio, "Tipo de tarjeta: Gold")

    def test_tema2_prueba_2(self):
    	premio = ofrecer_tarjeta_con_chip(montoEndeudamiento=15001, tipoCliente="AA")
    	self.assertEquals(premio, "Tipo de tarjeta: Platinum")

    def test_tema2_prueba_3(self):
    	premio = ofrecer_tarjeta_con_chip(montoEndeudamiento=10001, tipoCliente="A")
    	self.assertEquals(premio, "Tipo de tarjeta: Internacional")

    def test_tema2_prueba_4(self):
    	premio = ofrecer_tarjeta_con_chip(montoEndeudamiento=5001, tipoCliente="B")
    	self.assertEquals(premio, "Tipo de tarjeta: Club Miles")

    def test_tema2_prueba_5(self):
    	premio = ofrecer_tarjeta_con_chip(montoEndeudamiento=3001, tipoCliente="C")
    	self.assertEquals(premio, "Tipo de tarjeta: Advantage")



if __name__ == '__main__':
    unittest.main()