# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def clasificacion_clientes(montoDepositado, informacionBuro):
    enviarBoletinInformativo = "No"    #1
    clasificacionCliente = "no es digno de crédito"   #1
    if informacionBuro:  # True: digno de credito, False: no es digno de credito   #2
        if montoDepositado >= 30000:   #3
            clasificacionCliente = "AAA"
        elif montoDepositado >= 20000 and montoDepositado < 30000:    #4  #5
            clasificacionCliente = "AA"
        elif montoDepositado >= 15000 and montoDepositado < 20000:    #6  #7
            clasificacionCliente = "A"
        elif montoDepositado >= 10000 and montoDepositado < 15000:   #8   #9
            clasificacionCliente = "B"
        elif montoDepositado >= 5000 and montoDepositado < 10000:    #10  #11
            clasificacionCliente = "C"
        enviarBoletinInformativo = "Si"   #F
    return "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)   #F