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
        plazo_en_dias = 130
        monto = 10002
        if(plazo_en_dias>=120 and plazo_en_dias<180):
            if(monto >= 10001 and monto <=20000):
                mensaje = ("Arrocera Electrolux 1.8L")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje, "Arrocera Electrolux 1.8L")

    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        plazo_en_dias = 130
        monto = 25000
        if(plazo_en_dias>=120 and plazo_en_dias<180):
            if(monto >= 20001 and monto <=50000):
                mensaje = ("Aspiradora Electrolux")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Aspiradora Electrolux")

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        plazo_en_dias = 130
        monto = 60000
        if(plazo_en_dias>=120 and plazo_en_dias<180):
            if(monto >= 50000):
                mensaje = ("Mininevera 5 pies Electrolux")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Mininevera 5 pies Electrolux")

    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        plazo_en_dias = 190
        monto = 10002
        if(plazo_en_dias>=180 and plazo_en_dias<360):
            if(monto >= 10001 and monto <=20000):
                mensaje = ("Licuadora 5 velocidades Electrolux")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Licuadora 5 velocidades Electrolux")

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        plazo_en_dias = 190
        monto = 30000
        if(plazo_en_dias>=180 and plazo_en_dias<360):
            if(monto >= 20001 and monto <=50000):
                mensaje = ("Samsung Galaxy J1")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Samsung Galaxy J1")

    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        plazo_en_dias = 190
        monto = 70000
        if(plazo_en_dias>=180 and plazo_en_dias<360):
            if(monto >= 50000):
                mensaje = ("Minicomponente LG")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Minicomponente LG")

    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        plazo_en_dias = 400
        monto = 10002
        if(plazo_en_dias>=360):
            if(monto >= 10001 and monto <=20000):
                mensaje = ("Microondas Electrolux 20L")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Microondas Electrolux 20L")

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        plazo_en_dias = 400
        monto = 40000
        if(plazo_en_dias>=360):
            if(monto >= 20001 and monto <=50000):
                mensaje = ("Tablet Samsung")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Tablet Samsung")

    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        plazo_en_dias = 400
        monto = 70000
        if(plazo_en_dias>=360):
            if(monto >= 50000):
                mensaje = ("Tv LED 32' LG")
            else:
                mensaje = ("Fuera de Rango de monto")
        else:
            mensaje = ("Fuera de Rango de días")
        self.assertEquals(mensaje,"Tv LED 32' LG")

    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        TipoCliente = "AAA"
        monto = 30000
        mensaje = "Clasica"
        if(TipoCliente=="AAA" and monto>=20000):
            mensaje=("Gold")
        self.assertEquals(mensaje,"Gold")
    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        TipoCliente = "AA"
        monto = 16000
        mensaje = "Clasica"
        if(TipoCliente=="AA" and monto>=15000):
            mensaje=("Platinum")
        self.assertEquals(mensaje,"Platinum")
    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        TipoCliente = "AA"
        monto = 16000
        mensaje = "Clasica"
        if(TipoCliente=="AA" and monto<20000):
            mensaje=("Platinum")
        self.assertEquals(mensaje,"Platinum")
    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        TipoCliente = "A"
        monto = 11000
        mensaje = "Clasica"
        if(TipoCliente=="A" and monto>=10000):
            mensaje=("Internacional")
        self.assertEquals(mensaje,"Internacional")
    def test_tema2_prueba_5(self):
        # inserte su codigo de prueba
        TipoCliente = "A"
        monto = 11000
        mensaje = "Clasica"
        if(TipoCliente=="A" and monto<15000):
            mensaje=("Internacional")
        self.assertEquals(mensaje,"Internacional")
    def test_tema2_prueba_6(self):
        # inserte su codigo de prueba
        TipoCliente = "B"
        monto = 6000
        mensaje = "Clasica"
        if(TipoCliente=="B" and monto>=5000):
            mensaje=("Club Miles")
        self.assertEquals(mensaje,"Club Miles")
    def test_tema2_prueba_7(self):
        # inserte su codigo de prueba
        TipoCliente = "B"
        monto = 6000
        mensaje = "Clasica"
        if(TipoCliente=="B" and monto<10000):
            mensaje=("Club Miles")
        self.assertEquals(mensaje,"Club Miles")
    def test_tema2_prueba_8(self):
        # inserte su codigo de prueba
        TipoCliente = "AAA"
        monto = 30000
        mensaje = "Clasica"
        if(TipoCliente=="AAA" and monto>=20000):
            mensaje=("Gold")
        self.assertEquals(mensaje,"Gold")
    def test_tema2_prueba_9(self):
        # inserte su codigo de prueba
        TipoCliente = "AAA"
        monto = 30000
        mensaje = "Clasica"
        if(TipoCliente=="AAA" and monto>=20000):
            mensaje=("Gold")
        self.assertEquals(mensaje,"Gold")
    def test_tema2_prueba_10(self):
        # inserte su codigo de prueba
        TipoCliente = "AAA"
        monto = 30000
        mensaje = "Clasica"
        if(TipoCliente=="AAA" and monto>=20000):
            mensaje=("Gold")
        self.assertEquals(mensaje,"Gold")

if __name__ == '__main__':
    unittest.main()