# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_ID1(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(120,50002)
        self.assertEquals(msg,"Tipo de premio: mini nevera electrolux")

    def test_tema1_prueba_ID2(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(120,20002)
        self.assertEquals(msg,"Tipo de premio: aspiradora electrolux")

    def test_tema1_prueba_ID3(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(120,10002)
        self.assertEquals(msg,"Tipo de premio: arrocera electrolux")




    def test_tema1_prueba_ID4(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(180,50002)
        self.assertEquals(msg,"Tipo de premio: minicomponente LG")


    def test_tema1_prueba_ID5(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(180,20002)
        self.assertEquals(msg,"Tipo de premio: samsumg galaxy J1")

    def test_tema1_prueba_ID6(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(180,10002)
        self.assertEquals(msg,"Tipo de premio: licuadora electrolux")

    def test_tema1_prueba_ID7(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(360,50001)
        self.assertEquals(msg,"Tipo de premio: tv led LG")

    def test_tema1_prueba_ID8(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(360,20001)
        self.assertEquals(msg,"Tipo de premio: tablet samsumg")

    def test_tema1_prueba_ID9(self):
        # inserte su codigo de prueba
        msg=tema1.premio_por_deposito_a_plazo_fijo(360,10001)
        self.assertEquals(msg,"Tipo de premio: microondas electrolux")



    def test_tema2_prueba_ID1(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(20000,"AAA")
        self.assertEquals(msg,"Tipo de tarjeta: Gold")


    def test_tema2_prueba_ID2(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(15000,"AA")
        self.assertEquals(msg,"Tipo de tarjeta: Platinum")

    def test_tema2_prueba_ID3(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10000,"A")
        self.assertEquals(msg,"Tipo de tarjeta: Internacional")

    def test_tema2_prueba_ID4(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(5000,"B")
        self.assertEquals(msg,"Tipo de tarjeta: Club Miles")

    def test_tema2_prueba_ID5(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(3000,"C")
        self.assertEquals(msg,"Tipo de tarjeta: Advantage")


    def test_tema2_prueba_ID6(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10,"AAA")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID7(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(99999999,"AA")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID8(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10,"AA")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID9(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(99999999,"A")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID10(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10,"A")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID11(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(99999999,"B")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")

    def test_tema2_prueba_ID12(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10,"B")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")

    def test_tema2_prueba_ID13(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(99999999,"C")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")


    def test_tema2_prueba_ID14(self):
        # inserte su codigo de prueba
        msg=tema2.ofrecer_tarjeta_con_chip(10,"C")
        self.assertEquals(msg,"Tipo de tarjeta: Clasica")



if __name__ == '__main__':
	unittest.main()
