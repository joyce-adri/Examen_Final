# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_1(self):
        res = "escala: A++ , eficiencia: los más eficientes"
        porcentaje = 15
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_2(self):
        res = "escala: A+ , eficiencia: los más eficientes"
        porcentaje = 40
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_3(self):
        res = "escala: A , eficiencia: los más eficientes"
        porcentaje = 50
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_4(self):
        res = "escala: B , eficiencia: los más eficientes"
        porcentaje = 70
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))


    def test_tema1_5(self):
        res = "escala: C , eficiencia: los más eficientes"
        porcentaje = 80
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_6(self):
        res = "escala: E , eficiencia: consumo medio"
        porcentaje = 100
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_7(self):
        res = "escala: D , eficiencia: consumo medio"
        porcentaje = 95
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_8(self):
        res = "escala: F , eficiencia: alto consumo energético"
        porcentaje = 120
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_9(self):
        res = "escala: G , eficiencia: alto consumo energético"
        porcentaje = 130
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema2_1(self):
        clasificacionCliente = "no es digno de crédito"
        enviarBoletinInformativo = "No"
        montoDepositado = 5000
        informacionBuro = False
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

    def test_tema2_2(self):
        clasificacionCliente = "C"
        enviarBoletinInformativo = "Si"
        montoDepositado = 6000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

    def test_tema2_3(self):
        clasificacionCliente = "B"
        enviarBoletinInformativo = "Si"
        montoDepositado = 12000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

    def test_tema2_4(self):
        clasificacionCliente = "A"
        enviarBoletinInformativo = "Si"
        montoDepositado = 16000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

    def test_tema2_5(self):
        clasificacionCliente = "AA"
        enviarBoletinInformativo = "Si"
        montoDepositado = 22000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)
    def test_tema2_6(self):

        clasificacionCliente = "AAA"
        enviarBoletinInformativo = "Si"
        montoDepositado = 32000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

    def test_tema2_7(self):
        clasificacionCliente = "no es digno de crédito"
        enviarBoletinInformativo = "Si"
        montoDepositado = 3000
        informacionBuro = True
        esp = "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)
        res = tema2.clasificacion_clientes(montoDepositado, informacionBuro)
        self.assertEquals(esp, res)

if __name__ == '__main__':
    unittest.main()