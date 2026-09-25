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