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
        montoInversion = 50001
        solucion = "Tipo de premio: mini nevera electrolux"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
        
    def test_tema1_prueba_2(self):
        plazo = 120
        montoInversion = 20001
        solucion = "Tipo de premio: aspiradora electrolux"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
        
    def test_tema1_prueba_3(self):
        plazo = 120
        montoInversion = 10001
        solucion = "Tipo de premio: arrocera electrolux"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
        
    def test_tema1_prueba_4(self):
        plazo = 180
        montoInversion = 50001
        solucion = "Tipo de premio: minicomponente LG"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
        
    def test_tema1_prueba_5(self):
        plazo = 180
        montoInversion = 20001
        solucion = "Tipo de premio: samsumg galaxy J1"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
        
    def test_tema1_prueba_6(self):
        plazo = 180
        montoInversion = 10001
        solucion = "Tipo de premio: licuadora electrolux"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
    
    def test_tema1_prueba_7(self):
        plazo = 360
        montoInversion = 50001
        solucion = "Tipo de premio: tv led LG"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
    
    def test_tema1_prueba_8(self):
        plazo = 360
        montoInversion = 20001
        solucion = "Tipo de premio: tablet samsumg"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
    
    def test_tema1_prueba_9(self):
        plazo = 360
        montoInversion = 10001
        solucion = "Tipo de premio: microondas electrolux"
        resp = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(resp, solucion)
    
#tema 2    
    def test_tema2_prueba_1(self):
		tipoCliente = 'AAA'
		montoDeuda = 20000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Gold")

    def test_tema2_prueba_2(self):
		tipoCliente = 'AAA'
		montoDeuda = 19000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")
        
    def test_tema2_prueba_3(self):
		tipoCliente = 'AA'
		montoDeuda = 15000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Platinum")   
 
    def test_tema2_prueba_4(self):
		tipoCliente = 'AA'
		montoDeuda = 14000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")
        
    def test_tema2_prueba_5(self):
		tipoCliente = 'A'
		montoDeuda = 10000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Internacional")   
 
    def test_tema2_prueba_6(self):
		tipoCliente = 'A'
		montoDeuda = 9000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

    def test_tema2_prueba_7(self):
		tipoCliente = 'B'
		montoDeuda = 5000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Club Miles")   
 
    def test_tema2_prueba_8(self):
		tipoCliente = 'B'
		montoDeuda = 4000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")
    
    def test_tema2_prueba_9(self):
		tipoCliente = 'C'
		montoDeuda = 3000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Advantage")   
 
    def test_tema2_prueba_10(self):
		tipoCliente = 'C'
		montoDeuda = 2000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")
    
    def test_tema2_prueba_11(self):
		tipoCliente = 'F'
		montoDeuda = 2000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")
    
if __name__ == '__main__':
    unittest.main()