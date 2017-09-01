# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def ofrecer_tarjeta_con_chip(montoEndeudamiento, tipoCliente):
    tipoTarjeta = "Clasica"
    if tipoCliente == "AAA":
        if montoEndeudamiento >= 20000:
            tipoTarjeta = "Gold"
    elif tipoCliente == "AA":
        if montoEndeudamiento >= 15000 and montoEndeudamiento < 20000:
            tipoTarjeta = "Platinum"
    elif tipoCliente == "A":
        if montoEndeudamiento >= 10000 and montoEndeudamiento < 15000:
            tipoTarjeta = "Internacional"
    elif tipoCliente == "B":
        if montoEndeudamiento >= 5000 and montoEndeudamiento < 10000:
            tipoTarjeta = "Club Miles"
    elif tipoCliente == "C":
        if montoEndeudamiento >= 3000 and montoEndeudamiento < 5000:
            tipoTarjeta = "Advantage"
    return "Tipo de tarjeta: %s" % tipoTarjeta