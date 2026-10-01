class VendedorControlador:
    def __init__(self, registro, vista):
        self.registro = registro
        self.vista = vista

    def inicio(self):
        opcion = self.vista.mostrar_menu()
         #tiene que crearse un ciclo while para que permita regresal al menu principal
        match opcion:
            case "1":
                pass #submenu vendedores
            case "2":
                pass #Registrar / actualizar datos del mes
            case "3":
                pass #procesar la planilla de un vendedor
            case "4":
                pass #procesar la planilla de todos los vendedores
            case "5":
                pass #submenu de reportes 
            case "6":
                pass  #nuevo mes 
            case "7":
                self.vista.mostrar_mensaje("Saliendo del programa...")
            case _:
                self.vista.mostrar_mensaje("Opción inválida. Por favor, seleccione una opción válida.")

        '''
        SISTEMA DE GESTIÓN DE VENDEDORES 
            1. Gestión de vendedores 
            2. Registrar / actualizar datos del mes 
            3. Procesar planilla de un vendedor 
            4. Procesar planilla de todos los vendedores 
            5. Reportes 
            6. Iniciar nuevo mes 
            7. Salir 
        '''

#======================================================================
#============================MENU PRINCIPAL============================
#======================================================================

#======================================================================
#========================GESTIÓN DE VENDEDORES=========================
#======================================================================

    def registrar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        nombre = self.vista.solicitar_nombre()
        categoria = self.vista.solicitar_categoria()
        salario_base = self.vista.solicitar_salario_base()
        meta_mensual = self.vista.solicitar_meta_mensual()
        
        if categoria == 1:
            categoria = "Junior"
        elif categoria == 2:
            categoria = "SemiSenior"
        elif categoria == 3:
            categoria = "Senior"

        if (self.registro.crear_vendedor(cedula, nombre, categoria, salario_base, meta_mensual) == "CREADO"):
            self.vista.mostrar_mensaje("Vendedor registrado exitosamente.")
        else:
            self.vista.mostrar_mensaje("Cédula ya registrada.")

    def consultar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_por_cedula(cedula)

        if vendedor is not None:
            posicion = self.registro.buscar_posicion(cedula)      #busca la posicion de acuerdo a la lista

            ventas_mes = self.registro.get_ventas_mes(posicion)       #conjunto de listas asociadas
            horas_extra = self.registro.get_horas_extra(posicion)
            dias_ausencia = self.registro.get_dias_ausencia(posicion)
            bono_especial = self.registro.get_bono_especial(posicion)
            planilla_procesada = self.registro.get_planilla_procesada(posicion)
            salario_neto = self.registro.get_salario_neto_mes(posicion)

            self.vista.mostrar_info_vendedor(vendedor,ventas_mes,horas_extra,dias_ausencia,bono_especial,planilla_procesada,salario_neto)  #imprime info del vendedor y de listas

        else:
            self.vista.mostrar_mensaje("Vendedor no encontrado. \nVerifique la cedula ingresada.")
    
    
     #______________________________________________________________________________________________
    def modificar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_por_cedula(cedula)

        if (vendedor is not None):
            nuevo_nombre = self.vista.solicitar_nuevo_nombre()
            nueva_categoria = self.vista.solicitar_nueva_categoria()
            nuevo_salario_base = self.vista.solicitar_nuevo_salario_base()
            nueva_meta_mensual = self.vista.solicitar_nueva_meta_mensual()
            
            if nueva_categoria == 1:
                nueva_categoria = "Junior"
            elif nueva_categoria == 2:
                nueva_categoria = "SemiSenior"
            elif nueva_categoria == 3:
                nueva_categoria = "Senior"
                     
            self.registro.modificar_vendedor(cedula, nuevo_nombre, nueva_categoria, nuevo_salario_base, nueva_meta_mensual)
            self.vista.mostrar_mensaje("Vendedor modificado exitosamente.")

        else:
            self.vista.mostrar_mensaje("Vendedor no encontrado. Verifique la cedula ingresada")
        
    def eliminar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_vendedor(cedula)

        if (vendedor is not None):
            self.registro.eliminar_vendedor(cedula)
            self.vista.mostrar_mensaje("Vendedor eliminado exitosamente.")

        else:
            self.vista.mostrar_mensaje("Vendedor no encontrado. Verifique la cedula ingresada")

    def listar_vendedores(self):
        vendedores = self.registro.listar_vendedores()

        if (vendedores is not None):
            self.vista.mostrar_titulo_vendedores()
            for vendedor in vendedores:
                self.vista.mostrar_vendedor(vendedor)

            self.vista.mostrar_mensaje("====================================")

    def registrar_informacion_mes(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_vendedor(cedula)

        if (vendedor is not None):
            ventas_mes = self.vista.solicitar_ventas_mes()
            horas_extra = self.vista.solicitar_horas_extra()
            dias_ausencia = self.vista.solicitar_dias_ausencia()
            bono_especial = self.vista.solicitar_bono_especial()

            self.registro.registrar_informacion_mes(cedula, ventas_mes, horas_extra, dias_ausencia, bono_especial)
            self.vista.mostrar_mensaje("Información del mes registrada exitosamente.")

        else:
            self.vista.mostrar_mensaje("Vendedor no encontrado. Verifique la cedula ingresada.")

    def regresar_menu_principal(self):
        self.inicio()
#======================================================================
#===============================REPORTES===============================
#======================================================================
    
    def reporte_general_vendedores(self):
        vendedores = self.registro.listar_vendedores()

        if (vendedores is not None):
            for vendedor in vendedores:
                posicion = self.registro.buscar_posicion(vendedor.get_cedula())
                ventas_mes = self.registro.get_ventas_mes(posicion)
                porcentaje_cumplimiento = self.registro.obtener_porcentaje_cumplimiento(vendedor.get_cedula())

                self.vista.mostrar_reporte_general(vendedor, ventas_mes, porcentaje_cumplimiento)

        else:
            self.vista.mostrar_mensaje("No hay vendedores registrados.")


    def vendedor_mayor_ventas(self):
        vendedor = self.registro.obtener_vendedor_mayor_ventas()

        if (vendedor is not None):
            posicion = self.registro.buscar_posicion(vendedor.get_cedula())
            ventas_mes = self.registro.get_ventas_mes(posicion)

            self.vista.mostrar_mayor_venta(vendedor, ventas_mes)

        else:
            self.vista.mostrar_mensaje("No hay vendedores registrados.")

    def mayor_cumplimiento_meta(self):
        vendedor = self.registro.vendedor_mayor_cumplimiento()
        if vendedor is not None:
            posicion = self.registro.buscar_posicion(vendedor.get_cedula())
            porcentaje_cumplimiento = self.registro.obtener_porcentaje_cumplimiento(vendedor.get_cedula())

            self.vista.mostrar_mayor_porcentaje_cumplimiento(vendedor, porcentaje_cumplimiento)
        else:
            self.vista.mostrar_mensaje("No hay vendedores registrados.")
            
    def reporte_total_promedio_ventas(self):
        total = self.registro.total_ventas()
        promedio = self.registro.promedio_ventas()
        
        self.vista.mostrar_total_promedio_ventas(total, promedio)         
    
    def reporte_vendedores_bajo_meta(self):
        vendedores = self.registro.vendedores_bajo_meta()
        cantidad = len(vendedores)

        self.vista.mostrar_vendedores_bajo_meta(vendedores, cantidad)

    def reporte_total_comisiones(self):
        total = self.registro.total_comisiones_mes()
        
        self.vista.mostrar_total_comisiones(total)

    def reporte_total_planilla(self):
        total = self.registro.total_planilla()

        self.vista.mostrar_total_planilla(total)   
    
    
    def estadisticas_por_categoria(self):
        cantidad_junior = self.registro.cantidad_por_categoria("Junior")
        ventas_junior = self.registro.ventas_por_categoria("Junior")

        cantidad_semisenior = self.registro.cantidad_por_categoria("SemiSenior")
        ventas_semisenior = self.registro.ventas_por_categoria("SemiSenior")

        cantidad_senior = self.registro.cantidad_por_categoria("Senior")
        ventas_senior = self.registro.ventas_por_categoria("Senior")

        self.vista.estadisticas_por_categoria(cantidad_junior,ventas_junior,cantidad_semisenior,ventas_semisenior,cantidad_senior,ventas_senior)
    