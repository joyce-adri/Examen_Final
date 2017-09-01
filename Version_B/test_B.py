# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def validar_plazo_dias_0(self):
        if (self == 120):
            return "!"
        elif (self == 180):
            return "!"
        elif (self == 360):
            return "!"

    def validar_plazo_dias_1(self):
        if (self == 120):
            return "Arrocera Electrolux 1.8L"
        elif (self == 180):
            return "Licuadora 5 velocidades Electrolux"
        elif (self == 360):
            return "Microondas Electrolix 20L"
    
    def validar_plazo_dias_2(self):
        if (self == 120):
            return "Aspiradora Electrolux"
        elif (self == 180):
            return "Samsung Galaxy J1"
        elif (self == 360):
            return "Tablet Samsung"
    
    def validar_plazo_dias_3(self):
        if (self == 120):
            return "Mini nevera 5 pies Electrolux"
        elif (self == 180):
            return "Minicomponente LG"
        elif (self == 360):
            return "Tv LED 32' LG"
    
    def validar_monto(self):
        if (self <= 10000):
            return "No recibe premio"
        elif (self <= 20000 and self > 10000):
            return "Recibe premio! "
        elif (self <= 50000 and self > 20000):
            return "Recibe premio! "
        else:
            return "Recibe premio!"

    def test_tema1_prueba_1(self):
        # inserte su codigo de prueba
        mensaje_plazo_1 = self.Test.validar_plazo_dias_0(120)
        mensaje_monto_1 = self.Test.validar_monto(10000)
        mensaje_1 = mensaje_monto_1 + mensaje_plazo_1
        self.assertEquals(mensaje_1, "No recibe premio!")

    def test_tema1_prueba_2(self):
        mensaje_plazo_2 =self.Test.validar_plazo_dias_0(180)
        mensaje_monto_2 = self.Test.validar_monto(1000)
        mensaje_2 = mensaje_monto_2 + mensaje_plazo_2
        self.assertEquals(mensaje_2, "No recibe premio!")

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        mensaje_plazo_3 = self.Test.validar_plazo_dias_0(360)
        mensaje_monto_3 = self.Test.validar_monto(10000)
        mensaje_3 = mensaje_monto_3 + mensaje_plazo_3
        self.assertEquals(mensaje_3, "No recibe premio!")

    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        mensaje_plazo_4 = self.Test.validar_plazo_dias_1(120)
        mensaje_monto_4 = self.Test.validar_monto(10001)
        mensaje_4 = mensaje_monto_4 + " " +  mensaje_plazo_4
        self.assertEquals(mensaje_4, "Recibe premio! Arrocera Electrolux 1.8L")

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        mensaje_plazo_4 = self.Test.validar_plazo_dias_1(180)
        mensaje_monto_4 = self.Test.validar_monto(10001)
        mensaje_4 = mensaje_monto_4 + " " +  mensaje_plazo_4
        self.assertEquals(mensaje_4, "Recibe premio! Licuadora 5 velocidades Electrolux")

    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        mensaje_plazo_4 = self.Test.validar_plazo_dias_1(360)
        mensaje_monto_4 = self.Test.validar_monto(10001)
        mensaje_4 = mensaje_monto_4 + " " +  mensaje_plazo_4
        self.assertEquals(mensaje_4, "Recibe premio! Microondas Electrolix 20L")













    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()