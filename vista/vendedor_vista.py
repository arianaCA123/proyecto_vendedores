class VendedorVista:
    #Menu principal
    def mostrar_menu(self):
        print()
        print("------- SISTEMA DE GESTION DE VENDEDORES -------")
        print("1) Gestion de Vendedores")
        print("2) Registrar / Actualizar datos del mes ")
        print("3) Procesar Planilla de un Vendedor ")
        print("4) Procesar planilla de todos los vendedores ")
        print("5) Reportes  ")
        print("6) Iniciar nuevo mes  ")
        print("7) Salir ")
        return input("Seleccione una opcion: ")
   #submenu de vendedores
    def mostrar_submenu_vendedores(self):
        print()
        print("------- GESTION DE VENDEDORES -----_--")
        print("1) Registrar vendedor")
        print("2) Consultar vendedor")
        print("3) Modificar vendedor")
        print("4) Eliminar vendedor")
        print("5) Listar vendedores")
        print("6) Regresar")
        return input("Seleccione una opcion: ")
     #submenu de reportes
    def mostrar_submenu_reportes(self):
        print()
        print("------- REPORTES -------")
        print("1) Reporte general ")
        print("2) Vendedor con mayores ventas ")
        print("3) Mayor porcentaje de cumplimiento ")
        print("4) Total y promedio de ventas ")
        print("5) Vendedores que no alcanzaron la meta ")
        print("6) Total de comisiones ")
        print("7) Total de planilla ")
        print("8) Estadísticas por categoria ")
        print("9) Regresar  ")
        return input("Selecciona una opcion: ")
        
     
    #_____________________________________________________________________________
    #Datos para registrar el vendedor  (la categoria se comprara y se asigna)
    def solicitar_cedula(self):
        return input("Digite la Cedula: ")
        
    def solicitar_nombre(self):
        return input("Digite el nombre: ")
        
    def solicitar_categoria(self):
        print("1) Junior")
        print("2) SemiSenior" )
        print("3) Senior")
        return int(input("Seleccione una Categoria: "))
    
    def solicitar_salario_base(self):
        return float(input("Digite el salario base: "))

    def solicitar_meta_mensual(self):
        return float(input("Digite la meta mensual: "))

    
    #______________________________________________________
    #datos que se modifican al vendedor
    
    def solicitar_nuevo_nombre(self):
        return input("Digite el nuevo nombre: ")

    def solicitar_nueva_categoria(self):
        print("1) Junior")
        print("2) SemiSenior")
        print("3) Senior")
        return int(input("Seleccione la nueva categoria: "))

    def solicitar_nuevo_salario_base(self):
        return float(input("Digite el nuevo salario base: "))

    def solicitar_nueva_meta_mensual(self):
        return float(input("Digite la nueva meta mensual: "))

    
    #__________________________________________________________
    #datos mensuales (modificacion)
    
    #al registrar un vendedor los valores iniciales sean 0,
    #estos se utilizan cuando el usuario registra o modifica la información del mes
    
    def solicitar_ventas_mes(self):
        return float(input("Digite las ventas del mes: "))

    def solicitar_horas_extra(self):
        return int(input("Digite las horas extra: "))

    def solicitar_dias_ausencia(self):
        return int(input("Digite los dias de ausencia: "))

    def solicitar_bono_especial(self):
        return float(input("Digite el bono especial: "))
   
   #________________________________________________________
    #mostrar informacion
    
    def mostrar_titulo_vendedores(self):
        print()
        print("===== VENDEDORES REGISTRADOS =====")
    
    def mostrar_vendedor(self, vendedor):    #(listar vendedores del submenu vendedores)
        print()
        print(vendedor)
        print("=========================")    
    
    def mostrar_mensaje(self, mensaje):
        print(mensaje)
     
    #muestra la informacion de (consultar)vendedor y listas asociadas
    def mostrar_info_vendedor(self, vendedor, ventas_mes, horas_extra, dias_ausencia, bono_especial, planilla_procesada, salario_neto):
        print()
        print("======== INFORMACION DEL VENDEDOR ========")
        print("Cedula:", vendedor.get_cedula())
        print("Nombre:", vendedor.get_nombre())
        print("Categoría:", vendedor.get_categoria())
        print("Salario base:", vendedor.get_salario_base())
        print("Meta mensual:", vendedor.get_meta_mensual())
        print("__________________________________________")
        print("Ventas del mes:", ventas_mes)
        print("Horas extra:", horas_extra)
        print("Días de ausencia:", dias_ausencia)
        print("Bono especial:", bono_especial)
        print("__________________________________________")
        print("Ventas acumuladas:", vendedor.get_ventas_acumuladas())
        print("Comisiones acumuladas:", vendedor.get_comisiones_acumuladas())
        print("Meses procesados:", vendedor.get_meses_procesados())
        print("__________________________________________")
        print("Planilla procesada:", planilla_procesada)
        

        if planilla_procesada:
            print("Salario neto:", salario_neto)
        
        print("=========================================")
    
    def mostrar_planilla(self, vendedor, ventas_mes, horas_extra,
                         bono_especial, porcentaje_cumplimiento,
                         comision_inicial, ajuste_categoria,
                         comision_final, pago_horas_extra,
                         bono_rendimiento, total_ingresos,
                         deduccion_ausencias, deduccion_obligatoria,
                         impuesto_academico, salario_neto):
        print()
        print("============= DESGLOSE DE PLANILLA DEL VENDEDOR ============")
        print()
        #nombre y categoria
        print("Nombre: ",vendedor.get_nombre())
        print("Categoria: ",vendedor.get_categoria())
        
        #salario base
        print("Salario base: ",vendedor.get_salario_base())
        
        #ventas, meta y porcentaje
        print("Ventas realizadas: ", ventas_mes)
        print("Meta mensual: ",vendedor.get_meta_mensual())
        print("Porcentaje de cumplimiento: ", porcentaje_cumplimiento)
        
        #comision inicial, ajuste por categoria,comision final
        print("Comisión inicial: ", comision_inicial)
        print("Ajuste por categoría: ", ajuste_categoria)
        print("Comisión final: ", comision_final)
        
        #horas extra y pago
        print("Horas extra: ", horas_extra)
        print("Pago por horas extra: ", pago_horas_extra)
        
         # bonos
        print("Bono por rendimiento:", bono_rendimiento)
        print("Bono especial:", bono_especial)
        
        
        # total de ingresos
        print("Total de ingresos:", total_ingresos)

        # deducciones
        print("Deducción por ausencias:", deduccion_ausencias)
        print("Deducción obligatoria:", deduccion_obligatoria)
        print("Impuesto académico:", impuesto_academico)

        # salario neto
        print("Salario neto:", salario_neto)

        print("=====================================================")

        
        
        
        
    
 