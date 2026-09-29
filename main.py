from modelo.registro_vendedores import RegistroVendedores
from vista.vendedor_vista import VendedorVista
from controlador.vendedor_controlador import VendedorControlador

def main():
    registro = RegistroVendedores()
    vista = VendedorVista()
    controlador = VendedorControlador(registro, vista)
    controlador.inicio()

if __name__ == "__main__":
    main()
    