class ContratoBase:
    def calcular_multa(self, salario):
        raise NotImplementedError("Método calcular_multa deve ser implementado.")

class ContratoCLT(ContratoBase):
    def calcular_multa(self, salario):
        return salario * 0.4

class ContratoPJ(ContratoBase):
    def calcular_multa(self, salario):
        return salario * 0.1