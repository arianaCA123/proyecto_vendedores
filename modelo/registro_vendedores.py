from modelo.vendedor import Vendedor


class RegistroVendedores:

    # ==================================================
    # CONSTRUCTOR
    # Lista de objetos Vendedor y listas asociadas.
    # Los datos de un vendedor están en la MISMA posición
    # en todas las listas.
    # ==================================================

    def __init__(self):
        self.__vendedores = []            # objetos Vendedor
        self.__ventas_mes = []            # ventas del mes
        self.__horas_extra = []           # horas extra del mes
        self.__dias_ausencia = []         # días de ausencia del mes
        self.__bonos_especiales = []      # bono especial del mes
        self.__planilla_procesada = []    # True si ya se procesó la planilla
        self.__salarios_netos_mes = []    # salario neto calculado
        self.__comisiones_mes = []        # comisión final (para el reporte de comisiones)

    # ==================================================
    # BÚSQUEDAS
    # ==================================================

    # Devuelve el objeto Vendedor con esa cédula, o None si no existe.
    def buscar_por_cedula(self, cedula):
        for vendedor in self.__vendedores:
            if vendedor.get_cedula() == cedula:
                return vendedor
        return None

    # Devuelve la posición del vendedor en las listas, o None si no existe.
    def buscar_posicion(self, cedula):
        posicion = 0
        for vendedor in self.__vendedores:
            if vendedor.get_cedula() == cedula:
                return posicion
            posicion = posicion + 1
        return None

    def listar_vendedores(self):
        return self.__vendedores

    def esta_vacio(self):
        return len(self.__vendedores) == 0

    def cantidad_vendedores(self):
        return len(self.__vendedores)

    # ==================================================
    # OBTENER DATOS DEL MES (por posición)
    # ==================================================

    def get_ventas_mes(self, posicion):
        return self.__ventas_mes[posicion]

    def get_horas_extra(self, posicion):
        return self.__horas_extra[posicion]

    def get_dias_ausencia(self, posicion):
        return self.__dias_ausencia[posicion]

    def get_bono_especial(self, posicion):
        return self.__bonos_especiales[posicion]

    def get_planilla_procesada(self, posicion):
        return self.__planilla_procesada[posicion]

    def get_salario_neto_mes(self, posicion):
        return self.__salarios_netos_mes[posicion]

    def get_comision_mes(self, posicion):
        return self.__comisiones_mes[posicion]

    # ==================================================
    # REGISTRAR VENDEDOR
    # ==================================================

    def crear_vendedor(self, cedula, nombre, categoria, salario_base, meta_mensual):
        # No se permiten cédulas repetidas
        if self.buscar_por_cedula(cedula) is not None:
            return "CEDULA_DUPLICADA"

        # Los acumulados inician en cero
        nuevo_vendedor = Vendedor(cedula, nombre, categoria, salario_base,
                                  meta_mensual, 0, 0, 0)

        # Se agrega el objeto y un valor inicial en cada lista
        self.__vendedores.append(nuevo_vendedor)
        self.__ventas_mes.append(0)
        self.__horas_extra.append(0)
        self.__dias_ausencia.append(0)
        self.__bonos_especiales.append(0)
        self.__planilla_procesada.append(False)
        self.__salarios_netos_mes.append(0)
        self.__comisiones_mes.append(0)
        return "CREADO"

    # ==================================================
    # MODIFICAR VENDEDOR
    # ==================================================

    def actualizar_vendedor(self, cedula, nuevo_nombre, nueva_categoria,
                            nuevo_salario_base, nueva_meta_mensual):
        vendedor = self.buscar_por_cedula(cedula)

        if vendedor is None:
            return False

        # Se modifica el mismo objeto de la lista con set
        vendedor.set_nombre(nuevo_nombre)
        vendedor.set_categoria(nueva_categoria)
        vendedor.set_salario_base(nuevo_salario_base)
        vendedor.set_meta_mensual(nueva_meta_mensual)
        return True

    # ==================================================
    # ELIMINAR VENDEDOR
    # ==================================================

    def eliminar_vendedor(self, cedula):
        posicion = self.buscar_posicion(cedula)

        if posicion is None:
            return False

        # Se elimina la misma posición en todas las listas
        self.__vendedores.pop(posicion)
        self.__ventas_mes.pop(posicion)
        self.__horas_extra.pop(posicion)
        self.__dias_ausencia.pop(posicion)
        self.__bonos_especiales.pop(posicion)
        self.__planilla_procesada.pop(posicion)
        self.__salarios_netos_mes.pop(posicion)
        self.__comisiones_mes.pop(posicion)
        return True

    # ==================================================
    # REGISTRAR / ACTUALIZAR DATOS DEL MES
    # ==================================================

    def registrar_datos_mes(self, cedula, ventas, horas, dias, bono):
        posicion = self.buscar_posicion(cedula)

        if posicion is None:
            return False

        # Se reemplazan los valores en la posición del vendedor
        self.__ventas_mes[posicion] = ventas
        self.__horas_extra[posicion] = horas
        self.__dias_ausencia[posicion] = dias
        self.__bonos_especiales[posicion] = bono
        return True

    # ==================================================
    # INICIAR NUEVO MES
    # Reinicia los datos del mes. Los acumulados del
    # objeto Vendedor NO se modifican.
    # ==================================================

    def iniciar_nuevo_mes(self):
        posicion = 0
        for vendedor in self.__vendedores:
            self.__ventas_mes[posicion] = 0
            self.__horas_extra[posicion] = 0
            self.__dias_ausencia[posicion] = 0
            self.__bonos_especiales[posicion] = 0
            self.__planilla_procesada[posicion] = False
            self.__salarios_netos_mes[posicion] = 0
            self.__comisiones_mes[posicion] = 0
            posicion = posicion + 1

    # ==================================================
    # CÁLCULOS DE PLANILLA
    # ==================================================

    # Porcentaje de cumplimiento de la meta
    def calcular_porcentaje_cumplimiento(self, posicion):
        meta = self.__vendedores[posicion].get_meta_mensual()
        return (self.__ventas_mes[posicion] / meta) * 100

    # Comisión inicial según el cumplimiento
    def calcular_comision_inicial(self, posicion):
        ventas = self.__ventas_mes[posicion]
        porcentaje = self.calcular_porcentaje_cumplimiento(posicion)

        if porcentaje < 80:
            return 0
        elif porcentaje < 100:
            return ventas * 0.02
        elif porcentaje < 120:
            return ventas * 0.04
        else:
            return ventas * 0.06

    # Ajuste por categoría (Junior 0%, SemiSenior 10%, Senior 20%)
    def calcular_ajuste_categoria(self, posicion):
        comision_inicial = self.calcular_comision_inicial(posicion)
        categoria = self.__vendedores[posicion].get_categoria()

        if categoria == "SemiSenior":
            return comision_inicial * 0.10
        elif categoria == "Senior":
            return comision_inicial * 0.20
        else:
            return 0

    # Comisión final = comisión inicial + ajuste
    def calcular_comision_final(self, posicion):
        return self.calcular_comision_inicial(posicion) + self.calcular_ajuste_categoria(posicion)

    # Pago de horas extra
    def calcular_pago_horas_extra(self, posicion):
        salario_base = self.__vendedores[posicion].get_salario_base()
        valor_hora = salario_base / 240
        valor_hora_extra = valor_hora * 1.5
        return valor_hora_extra * self.__horas_extra[posicion]

    # Bono automático si cumple 110% o más
    def calcular_bono_rendimiento(self, posicion):
        if self.calcular_porcentaje_cumplimiento(posicion) >= 110:
            return 50000
        else:
            return 0

    # Deducción por ausencias
    def calcular_deduccion_ausencias(self, posicion):
        salario_base = self.__vendedores[posicion].get_salario_base()
        valor_dia = salario_base / 30
        return valor_dia * self.__dias_ausencia[posicion]

    # Total de ingresos
    def calcular_total_ingresos(self, posicion):
        salario_base = self.__vendedores[posicion].get_salario_base()
        return (salario_base
                + self.calcular_pago_horas_extra(posicion)
                + self.calcular_comision_final(posicion)
                + self.calcular_bono_rendimiento(posicion)
                + self.__bonos_especiales[posicion])

    # Salario ajustado
    def calcular_salario_ajustado(self, posicion):
        return self.calcular_total_ingresos(posicion) - self.calcular_deduccion_ausencias(posicion)

    # Deducción obligatoria (10%)
    def calcular_deduccion_obligatoria(self, posicion):
        return self.calcular_salario_ajustado(posicion) * 0.10

    # Impuesto académico por tramos
    def calcular_impuesto(self, posicion):
        salario_ajustado = self.calcular_salario_ajustado(posicion)

        if salario_ajustado <= 1000000:
            return 0
        elif salario_ajustado <= 1500000:
            return (salario_ajustado - 1000000) * 0.10
        else:
            return 500000 * 0.10 + (salario_ajustado - 1500000) * 0.15

    # Salario neto
    def calcular_salario_neto(self, posicion):
        return (self.calcular_salario_ajustado(posicion)
                - self.calcular_deduccion_obligatoria(posicion)
                - self.calcular_impuesto(posicion))

    # ==================================================
    # PROCESAR PLANILLA DE UN VENDEDOR
    # ==================================================

    def procesar_planilla(self, cedula):
        posicion = self.buscar_posicion(cedula)

        if posicion is None:
            return "NO_EXISTE"

        # No se procesa dos veces en el mismo mes
        if self.__planilla_procesada[posicion] == True:
            return "YA_PROCESADA"

        comision_final = self.calcular_comision_final(posicion)
        salario_neto = self.calcular_salario_neto(posicion)

        # Se actualizan los acumulados del objeto con get y set
        vendedor = self.__vendedores[posicion]
        vendedor.set_ventas_acumuladas(vendedor.get_ventas_acumuladas() + self.__ventas_mes[posicion])
        vendedor.set_comisiones_acumuladas(vendedor.get_comisiones_acumuladas() + comision_final)
        vendedor.set_meses_procesados(vendedor.get_meses_procesados() + 1)

        # Se actualizan las listas asociadas
        self.__planilla_procesada[posicion] = True
        self.__salarios_netos_mes[posicion] = salario_neto
        self.__comisiones_mes[posicion] = comision_final
        return "PROCESADA"

    # ==================================================
    # PROCESAR PLANILLA DE TODOS
    # Devuelve cuántas se procesaron.
    # Omitidas = cantidad_vendedores() - procesadas
    # ==================================================

    def procesar_todos(self):
        procesadas = 0
        for vendedor in self.__vendedores:
            if self.procesar_planilla(vendedor.get_cedula()) == "PROCESADA":
                procesadas = procesadas + 1
        return procesadas

    # ==================================================
    # REPORTES Y ESTADÍSTICAS
    # ==================================================

    # Vendedor con mayores ventas del mes
    def vendedor_mayores_ventas(self):
        mayor = None
        mayor_ventas = 0
        posicion = 0
        for vendedor in self.__vendedores:
            if mayor is None or self.__ventas_mes[posicion] > mayor_ventas:
                mayor = vendedor
                mayor_ventas = self.__ventas_mes[posicion]
            posicion = posicion + 1
        return mayor

    # Vendedor con mayor porcentaje de cumplimiento
    def vendedor_mayor_cumplimiento(self):
        mayor = None
        mayor_porcentaje = 0
        posicion = 0
        for vendedor in self.__vendedores:
            porcentaje = self.calcular_porcentaje_cumplimiento(posicion)
            if mayor is None or porcentaje > mayor_porcentaje:
                mayor = vendedor
                mayor_porcentaje = porcentaje
            posicion = posicion + 1
        return mayor

    # Total de ventas del mes
    def total_ventas(self):
        total = 0
        for ventas in self.__ventas_mes:
            total = total + ventas
        return total

    # Promedio de ventas del mes
    def promedio_ventas(self):
        if self.esta_vacio():
            return 0
        return self.total_ventas() / len(self.__vendedores)

    # Vendedores con cumplimiento menor a 100%
    def vendedores_bajo_meta(self):
        bajo_meta = []
        posicion = 0
        for vendedor in self.__vendedores:
            if self.calcular_porcentaje_cumplimiento(posicion) < 100:
                bajo_meta.append(vendedor)
            posicion = posicion + 1
        return bajo_meta

    # Total de comisiones de las planillas procesadas
    def total_comisiones_mes(self):
        total = 0
        posicion = 0
        for vendedor in self.__vendedores:
            if self.__planilla_procesada[posicion] == True:
                total = total + self.__comisiones_mes[posicion]
            posicion = posicion + 1
        return total

    # Total de salarios netos de las planillas procesadas
    def total_planilla(self):
        total = 0
        posicion = 0
        for vendedor in self.__vendedores:
            if self.__planilla_procesada[posicion] == True:
                total = total + self.__salarios_netos_mes[posicion]
            posicion = posicion + 1
        return total

    # Cantidad de vendedores de una categoría
    def cantidad_por_categoria(self, categoria):
        cantidad = 0
        for vendedor in self.__vendedores:
            if vendedor.get_categoria() == categoria:
                cantidad = cantidad + 1
        return cantidad

    # Total de ventas de una categoría
    def ventas_por_categoria(self, categoria):
        total = 0
        posicion = 0
        for vendedor in self.__vendedores:
            if vendedor.get_categoria() == categoria:
                total = total + self.__ventas_mes[posicion]
            posicion = posicion + 1
        return total