# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente): #I
    tipoTarjeta = "Clasica" #1
    if tipoCliente == "AAA": #2
        if montoEndeudamiento >= 20000: #3
            tipoTarjeta = "Gold" #4
    elif tipoCliente == "AA": #5
        if montoEndeudamiento >= 15000 and montoEndeudamiento < 20000: #6
            tipoTarjeta = "Platinum" #7
    elif tipoCliente == "A": #8
        if montoEndeudamiento >= 10000 and montoEndeudamiento < 15000: #9
            tipoTarjeta = "Internacional" #10
    elif tipoCliente == "B": #11
        if montoEndeudamiento >= 5000 and montoEndeudamiento < 10000: #12
            tipoTarjeta = "Club Miles" #13
    elif tipoCliente == "C": #14
        if montoEndeudamiento >= 3000 and montoEndeudamiento < 5000: #15
            tipoTarjeta = "Advantage" #16
    return "Tipo de tarjeta: %s" % tipoTarjeta #F