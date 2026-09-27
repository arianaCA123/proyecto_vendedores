class Vendedor:
    def __init__(self, cedula, nombre, categoria, salario_base, meta_mensual, ventas_acumuladas, comisiones_acumuladas, meses_procesados):
        self.set_cedula(cedula)
        self.set_nombre(nombre)
        self.set_categoria(categoria)
        self.set_salario_base(salario_base)
        self.set_meta_mensual(meta_mensual)
        self.set_ventas_acumuladas(ventas_acumuladas)
        self.set_comisiones_acumuladas(comisiones_acumuladas)
        self.set_meses_procesados(meses_procesados)

#========================cedula========================

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_cedula(self):
        return self.__cedula

#=======================nombre========================

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

#=======================categoria========================

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria

#=======================salario_base========================

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

#=======================meta_mensual========================

    def set_meta_mensual(self, meta_mensual):
        self.__meta_mensual = meta_mensual

    def get_meta_mensual(self):
        return self.__meta_mensual

#=======================ventas_acumuladas========================

    def set_ventas_acumuladas(self, ventas_acumuladas):
        self.__ventas_acumuladas = ventas_acumuladas

    def get_ventas_acumuladas(self):
        return self.__ventas_acumuladas

#=======================comisiones_acumuladas========================

    def set_comisiones_acumuladas(self, comisiones_acumuladas):
        self.__comisiones_acumuladas = comisiones_acumuladas

    def get_comisiones_acumuladas(self):
        return self.__comisiones_acumuladas

#=======================meses_procesados========================

    def set_meses_procesados(self, meses_procesados):
        self.__meses_procesados = meses_procesados

    def get_meses_procesados(self):
        return self.__meses_procesados

#==========================================================
#================ ******* CALCULOS ******* ================
#==========================================================

    def calcular_porcentaje_cumplimiento(self, ventas_mes):
        porcentaja_cumplimiento = (ventas_mes / self.get_meta_mensual()) * 100
        return porcentaja_cumplimiento

#=======================================================

    def calcular_comision_inicial(self, ventas_mes):
        porcentaje = self.calcular_porcentaje_cumplimiento(ventas_mes)

        if porcentaje < 80:
            return 0
        elif porcentaje < 100:
            comision_inicial = ventas_mes * 0.02
            return comision_inicial
        
        elif porcentaje < 120:
            comision_inicial = ventas_mes * 0.04
            return comision_inicial
        
        else:
            comision_inicial = ventas_mes * 0.06
            return comision_inicial

#=======================================================

    def calcular_comision_final(self, ventas_mes):
        comision_inicial = self.calcular_comision_inicial(ventas_mes)

        if self.get_categoria() == "SemiSenior":
            comision_final = comision_inicial * 1.10
            return comision_final
        
        elif self.get_categoria() == "Senior":
            comision_final = comision_inicial * 1.20
            return comision_final
        
        comision_final = comision_inicial
        return comision_final

#=======================================================

    def calcular_pago_horas_extra(self, horas_extra):
        valor_hora = self.get_salario_base() / 240
        pago_horas_extra = valor_hora * 1.5 * horas_extra
        return pago_horas_extra

#=======================================================

    def calcular_bono_rendimiento(self, ventas_mes):
        return 50000 if self.calcular_porcentaje_cumplimiento(ventas_mes) >= 110 else 0

#=======================================================

    def calcular_deduccion_ausencias(self, dias_ausencia):
        deduccion_ausencias = (self.get_salario_base() / 30) * dias_ausencia
        return deduccion_ausencias

#=======================================================

    def calcular_salario_neto(self, ventas_mes, horas_extra, dias_ausencia, bono_especial):
        comision_final = self.calcular_comision_final(ventas_mes)

        total_ingresos = (self.get_salario_base()
                           + self.calcular_pago_horas_extra(horas_extra)
                           + comision_final
                           + self.calcular_bono_rendimiento(ventas_mes)
                           + bono_especial)
        
        salario_ajustado = total_ingresos - self.calcular_deduccion_ausencias(dias_ausencia)
        deduccion_obligatoria = salario_ajustado * 0.10
        
        if salario_ajustado <= 1000000:
            impuesto = 0

        elif salario_ajustado <= 1500000:
            impuesto = (salario_ajustado - 1000000) * 0.10

        else:
            impuesto = 500000 * 0.10 + (salario_ajustado - 1500000) * 0.15

        salario_neto = salario_ajustado - deduccion_obligatoria - impuesto
        return salario_neto

#=======================================================================
#================ ******* ACUTALIZAR ACUMULADOS ******* ================
#=======================================================================

    def actualizar_acumulados(self, ventas_mes, comision_final):

        self.set_ventas_acumuladas(self.get_ventas_acumuladas() + ventas_mes)
        self.set_comisiones_acumuladas(self.get_comisiones_acumuladas() + comision_final)
        self.set_meses_procesados(self.get_meses_procesados() + 1)

#=======================================================================
#================ ******* AJUSTE CATEGORIA ******* ================
#=======================================================================

    #sirve para obtener el porcentaje de ajuste de acuerdo a la categoria del vendedor
    def ajuste_categoria(self):
        if self.get_categoria() == "Junior":
            return "0.0"
        elif self.get_categoria() == "SemiSenior":
            return "10.0"
        elif self.get_categoria() == "Senior":
            return "20.0"
        else:
            return "0.0"

#=======================str========================

    def __str__(self):
        return "||Cedula: "+self.get_cedula()+" \n||Nombre: "+self.get_nombre()+" \n||Categoria: "+self.get_categoria()+" \n||Salario Base: "+str(self.get_salario_base())+" \n||Meta Mensual: "+str(self.get_meta_mensual())+" \n||Ventas Acumuladas: "+str(self.get_ventas_acumuladas())+" \n||Comisiones Acumuladas: "+str(self.get_comisiones_acumuladas())+" \n||Meses Procesados: "+str(self.get_meses_procesados())