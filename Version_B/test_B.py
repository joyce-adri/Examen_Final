# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

#tema 1
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
    elif plazo == 360:
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
        # inserte su codigo de prueba
        #ID caso 1 con plazo = 60 y monto de Inversion = 10000
        msg = premio_por_deposito_a_plazo_fijo(60,10000)
        self.assertEquals(msg, "Tipo de premio: no recibe premio")

    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        #ID caso 2 con plazo = 120 y monto de Inversion = 10000
        msg = premio_por_deposito_a_plazo_fijo(120,10000)
        self.assertEquals(msg, "Tipo de premio: no recibe premio")

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        #ID caso 3 con plazo = 120 y monto de Inversion = 15000
        msg = premio_por_deposito_a_plazo_fijo(120,15000)
        self.assertEquals(msg, "Tipo de premio: arrocera electrolux")

    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        #ID caso 4 con plazo = 120 y monto de Inversion = 30000
        msg = premio_por_deposito_a_plazo_fijo(120,30000)
        self.assertEquals(msg, "Tipo de premio: aspiradora electrolux")

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        #ID caso 5 con plazo = 120 y monto de Inversion = 50001
        msg = premio_por_deposito_a_plazo_fijo(120,50001)
        self.assertEquals(msg, "Tipo de premio: mini nevera electrolux")

    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        #ID caso 6 con plazo = 180 y monto de Inversion = 10000
        msg = premio_por_deposito_a_plazo_fijo(180,10000)
        self.assertEquals(msg, "Tipo de premio: no recibe premio")

    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        #ID caso 7 con plazo = 180 y monto de Inversion = 15000
        msg = premio_por_deposito_a_plazo_fijo(180,15000)
        self.assertEquals(msg, "Tipo de premio: licuadora electrolux")

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        #ID caso 8 con plazo = 180 y monto de Inversion = 30000
        msg = premio_por_deposito_a_plazo_fijo(180,30000)
        self.assertEquals(msg, "Tipo de premio: samsumg galaxy J1")

    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        #ID caso 9 con plazo = 180 y monto de Inversion = 50001
        msg = premio_por_deposito_a_plazo_fijo(180,50001)
        self.assertEquals(msg, "Tipo de premio: minicomponente LG")

    def test_tema1_prueba_10(self):
        # inserte su codigo de prueba
        #ID caso 10 con plazo = 360 y monto de Inversion = 10000
        msg = premio_por_deposito_a_plazo_fijo(360,10000)
        self.assertEquals(msg, "Tipo de premio: no recibe premio")

    def test_tema1_prueba_11(self):
        # inserte su codigo de prueba
        #ID caso 11 con plazo = 360 y monto de Inversion = 15000
        msg = premio_por_deposito_a_plazo_fijo(360,15000)
        self.assertEquals(msg, "Tipo de premio: microondas electrolux")

    def test_tema1_prueba_12(self):
        # inserte su codigo de prueba
        #ID caso 12 con plazo = 360 y monto de Inversion = 30000
        msg = premio_por_deposito_a_plazo_fijo(360,30000)
        self.assertEquals(msg, "Tipo de premio: tablet samsumg")

    def test_tema1_prueba_13(self):
        # inserte su codigo de prueba
        #ID caso 13 con plazo = 360 y monto de Inversion = 50001
        msg = premio_por_deposito_a_plazo_fijo(360,50001)
        self.assertEquals(msg, "Tipo de premio: tv led LG")
    """
    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        #ID caso 1 con plazo = 60 y monto de Inversion = 10000
        msg = ofrecer_tarjeta_con_chip(20000,"AAA")
        self.assertEquals(msg, "Tipo de tarjeta: Gold")

    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        #ID caso 2 con plazo = 120 y monto de Inversion = 10000
        msg = ofrecer_tarjeta_con_chip(10000,"AAA")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        #ID caso 3 con plazo = 120 y monto de Inversion = 15000
        msg = ofrecer_tarjeta_con_chip(17000,"AA")
        self.assertEquals(msg, "Tipo de tarjeta: Platinum")

    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        #ID caso 4 con plazo = 120 y monto de Inversion = 30000
        msg = ofrecer_tarjeta_con_chip(10000,"AA")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_5(self):
        # inserte su codigo de prueba
        #ID caso 5 con plazo = 120 y monto de Inversion = 50001
        msg = ofrecer_tarjeta_con_chip(11000,"A")
        self.assertEquals(msg, "Tipo de tarjeta: Internacional")

    def test_tema2_prueba_6(self):
        # inserte su codigo de prueba
        #ID caso 6 con plazo = 180 y monto de Inversion = 10000
        msg = ofrecer_tarjeta_con_chip(5000,"A")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_7(self):
        # inserte su codigo de prueba
        #ID caso 7 con plazo = 180 y monto de Inversion = 15000
        msg = ofrecer_tarjeta_con_chip(7000,"B")
        self.assertEquals(msg, "Tipo de tarjeta: Club Miles")

    def test_tema2_prueba_8(self):
        # inserte su codigo de prueba
        #ID caso 8 con plazo = 180 y monto de Inversion = 30000
        msg = ofrecer_tarjeta_con_chip(2000,"B")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_9(self):
        # inserte su codigo de prueba
        #ID caso 9 con plazo = 180 y monto de Inversion = 50001
        msg = ofrecer_tarjeta_con_chip(4000,"C")
        self.assertEquals(msg, "Tipo de tarjeta: Advantage")

    def test_tema2_prueba_10(self):
        # inserte su codigo de prueba
        #ID caso 10 con plazo = 360 y monto de Inversion = 10000
        msg = ofrecer_tarjeta_con_chip(1000,"C")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    def test_tema2_prueba_11(self):
        # inserte su codigo de prueba
        #ID caso 11 con plazo = 360 y monto de Inversion = 15000
        msg = ofrecer_tarjeta_con_chip(30000,"F")
        self.assertEquals(msg, "Tipo de tarjeta: Clasica")

    """
    """
    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()
    """

if __name__ == '__main__':
    unittest.main()