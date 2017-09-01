# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def clasificacion_clientes(montoDepositado, informacionBuro):
    enviarBoletinInformativo = "No"
    clasificacionCliente = "no es digno de crédito"
    if informacionBuro:  # True: digno de credito, False: no es digno de credito  # Nodo 1
        if montoDepositado >= 30000:  #Nodo 2
            clasificacionCliente = "AAA" #Nodo 3
        elif montoDepositado >= 20000 and montoDepositado < 30000: #Nodo 4
            clasificacionCliente = "AA" #Nodo 5
        elif montoDepositado >= 15000 and montoDepositado < 20000: #Nodo 6
            clasificacionCliente = "A" #Nodo 7
        elif montoDepositado >= 10000 and montoDepositado < 15000: #Nodo 8
            clasificacionCliente = "B" #Nodo 9
        elif montoDepositado >= 5000 and montoDepositado < 10000: #Nodo 10
            clasificacionCliente = "C" #Nodo 11
        enviarBoletinInformativo = "Si" #Nodo 12
    return "Tipo de cliente: %s, Envio de boletin: %s" % (clasificacionCliente, enviarBoletinInformativo) #Nodo 13