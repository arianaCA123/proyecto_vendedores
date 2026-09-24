class VendedorVista:
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
        
        
        
        
        
        
        
        
        