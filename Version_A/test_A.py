# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_ID(self):
        # inserte su codigo de prueba
        #Prueba 1
        self.assertEqual(tema1.etiquetado_consumo_energia(29),"escala: A++ , eficiencia: los más eficientes")
        #Prueba 2
        self.assertEqual(tema1.etiquetado_consumo_energia(30),"escala: A+ , eficiencia: los más eficientes")
        #Prueba 3
        self.assertEquals(tema1.etiquetado_consumo_energia(42),"escala: A , eficiencia: los más eficientes")
        #self.assertEquals()

    #def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
    #    self.assertEquals()

if __name__ == '__main__':
    unittest.main()