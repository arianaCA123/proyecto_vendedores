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

#=======================str========================

    def __str__(self):
        return "||Cedula: "+self.get_cedula()+" \n||Nombre: "+self.get_nombre()+" \n||Categoria: "+self.get_categoria()+" \n||Salario Base: "+str(self.get_salario_base())+" \n||Meta Mensual: "+str(self.get_meta_mensual())+" \n||Ventas Acumuladas: "+str(self.get_ventas_acumuladas())+" \n||Comisiones Acumuladas: "+str(self.get_comisiones_acumuladas())+" \n||Meses Procesados: "+str(self.get_meses_procesados())