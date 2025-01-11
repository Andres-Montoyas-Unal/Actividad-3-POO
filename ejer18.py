class Empleado():
    def __init__(self,codigo,nombres,horas_trabajadas,valor_hora,porcentaje):
        self.codigo=codigo
        self.nombres=nombres
        self.horas_trabajadas=horas_trabajadas
        self.valor_hora=valor_hora
        self.porcentaje=porcentaje
    def calcular_salario_bruto(self):
        return float(self.horas_trabajadas)*float(self.valor_hora)
    def calcular_salario_neto(self):
        bruto=self.calcular_salario_bruto()
        return bruto-(bruto*(float(self.porcentaje)/100))
    
