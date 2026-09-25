class VendedorVista:
    #__Menu principal
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
   #submenus
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
        
     #_____Datos para registrar el vendedor  (la categoria se comprara y se asigna)
    #_____________________________________________________________________________
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

    #datos que se modifican al vendedor
    #______________________________________________________
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

    #datos mensuales (modificacion)
    #__________________________________________________________
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
    
    def mostrar_mensaje(self, mensaje):
        print(mensaje)
     
     #muestra la informacion de un vendedor 6.2
    def mostrar_info_vendedor(self, vendedor, ventas_mes, horas_extra, dias_ausencia, bono_especial, planilla_procesada, salario_neto):
        print()
        print("====== INFORMACIÓN DEL VENDEDOR ======")
        print("Cédula:", vendedor.get_cedula())
        print("Nombre:", vendedor.get_nombre())
        print("Categoría:", vendedor.get_categoria())
        print("Salario base:", vendedor.get_salario_base())
        print("Meta mensual:", vendedor.get_meta_mensual())
        print("Ventas del mes:", ventas_mes)
        print("Horas extra:", horas_extra)
        print("Días de ausencia:", dias_ausencia)
        print("Bono especial:", bono_especial)
        print("Ventas acumuladas:", vendedor.get_ventas_acumuladas())
        print("Comisiones acumuladas:", vendedor.get_comisiones_acumuladas())
        print("Meses procesados:", vendedor.get_meses_procesados())
        print("Planilla procesada:", planilla_procesada)

        if planilla_procesada:
            print("Salario neto del mes:", salario_neto)
    
    
 