
class PremiosDepositosPlazoFijo():
    def obtenerPremio(self, plazo_dias, inversion):
        if inversion >= 10001 and inversion <= 20000:
            if plazo_dias == 120:
                return "arrocera electrolux 1.8l"
            elif plazo_dias == 180:
                return "licuadora 5 velocidades electrolux"
            elif plazo_dias == 360:
                return "microondas electrolux 20l"
        elif inversion >= 20001 and inversion <= 50000:
            if plazo_dias == 120:
                return "aspiradora electrolux"
            elif plazo_dias == 180:
                return "samsung galaxy j1"
            elif plazo_dias == 360:
                return "tablet samsung"
        elif inversion >= 50001:
            if plazo_dias == 120:
                return "mini nevera 5 pies electrolux"
            elif plazo_dias == 180:
                return "minicomponente lg"
            elif plazo_dias == 360:
                return "tv led 32 lg"
