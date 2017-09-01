# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente):
    tipoTarjeta = "Clasica"#1
    if tipoCliente == "AAA":#2
        if montoEndeudamiento >= 20000:#3
            tipoTarjeta = "Gold"#4
    elif tipoCliente == "AA":#5
        if montoEndeudamiento >= 15000 and montoEndeudamiento < 20000:#6 #7
            tipoTarjeta = "Platinum"#8
    elif tipoCliente == "A":#9
        if montoEndeudamiento >= 10000 and montoEndeudamiento < 15000:#10#11
            tipoTarjeta = "Internacional"#12
    elif tipoCliente == "B":#13
        if montoEndeudamiento >= 5000 and montoEndeudamiento < 10000:#14 #15
            tipoTarjeta = "Club Miles"#16
    elif tipoCliente == "C":#17
        if montoEndeudamiento >= 3000 and montoEndeudamiento < 5000:#18 #19
            tipoTarjeta = "Advantage"#20
    return "Tipo de tarjeta: %s" % tipoTarjeta#21