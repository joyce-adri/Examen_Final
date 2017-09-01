# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	def test_tema1_prueba_1(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(120,60001)
		self.assertEquals(msg,"Tipo de premio: mini nevera electrolux")


    #def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        #self.assertEquals()

if __name__ == '__main__':
    unittest.main()