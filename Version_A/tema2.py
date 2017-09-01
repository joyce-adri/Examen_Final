# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def clasificacion_clientes(montoDepositado, informacionBuro):
    enviarBoletinInformativo = "No"                                                            #A
    clasificacionCliente = "no es digno de crédito"                                            #A
    if informacionBuro:  # True: digno de credito, False: no es digno de credito               #B
        if montoDepositado >= 30000:                                                           #C
            clasificacionCliente = "AAA"
        elif montoDepositado >= 20000 and montoDepositado < 30000:                             #D
            clasificacionCliente = "AA"
        elif montoDepositado >= 15000 and montoDepositado < 20000:                             #E
            clasificacionCliente = "A"
        elif montoDepositado >= 10000 and montoDepositado < 15000:                             #F
            clasificacionCliente = "B"
        elif montoDepositado >= 5000 and montoDepositado < 10000:                              #G
            clasificacionCliente = "C"
        enviarBoletinInformativo = "Si"                                                        #H
    return "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo)     #I