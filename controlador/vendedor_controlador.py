class VendedorControlador:
    def __init__(self, registro, vista):
        self.registro = registro
        self.vista = vista

    def inicio(self):
        opcion = self.vista.mostrar_menu()

        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
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

        vendedor = self.registro.registrar_vendedor(cedula,nombre,categoria,salario_base,meta_mensual)
        
        if (vendedor is not None):
            self.vista.mostrar_mensaje("Vendedor registrado exitosamente.")
            
        else:
            self.vista.mostrar_mensaje("Error al registrar el vendedor.")
    
    def consultar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_vendedor(cedula)

        if (vendedor is not None):
            self.vista.mostrar_datos_vendedor(vendedor)

        else:
            self.vista.mostrar_mensaje("Vendedor no encontrado. Verifique la cedula ingeresada.")

    def modificar_vendedor(self):
        cedula = self.vista.solicitar_cedula()
        vendedor = self.registro.buscar_vendedor(cedula)

        if (vendedor is not None):
            nuevo_nombre = self.vista.solicitar_nuevo_nombre()
            nueva_categoria = self.vista.solicitar_nueva_categoria()
            nuevo_salario_base = self.vista.solicitar_nuevo_salario_base()
            nueva_meta_mensual = self.vista.solicitar_nueva_meta_mensual()

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

    def listar_vendedor(self):
        vendedores = self.registro.listar_vendedores()

        if (vendedores is not None):
            self.vista.mostrar_titulo_vendedores()
            for vendedor in vendedores:
                self.vista.mostrar_vendedor(vendedor)

            self.vista.mostrar_mensaje("====================================")

    def regresar_menu_principal(self):
        self.inicio()
#======================================================================
#===============================REPORTES===============================
#======================================================================