class Vendedor:

    def __init__(self, cedula, nombre, categoria, salario_base, meta_mensual,
                 ventas_acumuladas=0.0, comisiones_acumuladas=0.0,
                 meses_procesados=0):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__categoria = categoria
        self.__salario_base = salario_base
        self.__meta_mensual = meta_mensual
        self.__ventas_acumuladas = ventas_acumuladas
        self.__comisiones_acumuladas = comisiones_acumuladas
        self.__meses_procesados = meses_procesados

    # ----------------------------- GET -----------------------------
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_salario_base(self):
        return self.__salario_base

    def get_meta_mensual(self):
        return self.__meta_mensual

    def get_ventas_acumuladas(self):
        return self.__ventas_acumuladas

    def get_comisiones_acumuladas(self):
        return self.__comisiones_acumuladas

    def get_meses_procesados(self):
        return self.__meses_procesados

    # ----------------------------- SET -----------------------------
    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    def set_meta_mensual(self, meta_mensual):
        self.__meta_mensual = meta_mensual

    def set_ventas_acumuladas(self, ventas_acumuladas):
        self.__ventas_acumuladas = ventas_acumuladas

    def set_comisiones_acumuladas(self, comisiones_acumuladas):
        self.__comisiones_acumuladas = comisiones_acumuladas

    def set_meses_procesados(self, meses_procesados):
        self.__meses_procesados = meses_procesados
