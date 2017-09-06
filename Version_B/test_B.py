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
        self.assertEquals(solucion, resp)

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()