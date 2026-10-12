# Sistema de Gestión de Planilla y Rendimiento de Vendedores

Proyecto #1 – Desarrollo de Software II – Informática Empresarial – II Ciclo 2026

Sistema de consola en Python que administra a los vendedores de una empresa de
equipos tecnológicos y calcula su planilla mensual: comisión según el
cumplimiento de la meta, ajuste por categoría, horas extra, bonos, deducciones,
impuesto académico y salario neto. Además genera reportes de ventas y
rendimiento, y permite iniciar un nuevo mes sin perder los acumulados
históricos de cada vendedor.

## Desarrolladores

| Nombre | Carné | Opciones del menú principal a cargo |
|---|---|---|
| Ariana Carrillo Azofeifa | C5D753 | 1. Gestión de vendedores, 2. Registrar / actualizar datos del mes, `main.py`, mejoras y correcciones generales |
| Michelle Hernández | C4l585 | 3. Procesar planilla de un vendedor, 4. Procesar planilla de todos los vendedores |
| Carlos Alvarado | C30348 | 5. Reportes, 6. Iniciar nuevo mes, 7. Salir |

Los tres integrantes trabajaron en conjunto en la vista (`vendedor_vista.py`)
y en el controlador (`vendedor_controlador.py`).

## Stack tecnológico

| Tecnología | Uso en el proyecto |
|---|---|
| **Python 3.10 o superior** | Lenguaje de todo el sistema, sin librerías externas |
| **Programación Orientada a Objetos** | Clase `Vendedor` con atributos privados y métodos get/set |
| **Patrón MVC** | Separación en Modelo, Vista y Controlador |
| **Listas unidimensionales** | Lista de objetos `Vendedor` y listas asociadas por posición, sin matrices ni diccionarios |
| **Thonny** | Entorno de desarrollo (IDE) |
| **Git y GitHub** | Control de versiones y repositorio compartido |

El sistema trabaja en memoria: no usa archivos ni bases de datos. Los datos se
pierden al cerrar el programa.

## Cómo ejecutar

1. Tener instalado **Python 3.10 o superior**. El menú usa `match`/`case`, que
   no existe en versiones anteriores.
2. Abrir la carpeta del proyecto.
3. Ejecutar `main.py`:

```
python main.py
```

En Thonny: abrir `main.py` y presionar **Run** (F5).
Siempre se debe ejecutar `main.py`, no los otros archivos.

## Estructura del proyecto (MVC)

```
Proyecto1_C5D753_C4l585_C30348/
├── modelo/
│   ├── vendedor.py               Clase Vendedor: atributos privados, get/set,
│   │                             cálculos de planilla y actualización de acumulados
│   └── registro_vendedores.py    Lista de objetos, listas asociadas, búsquedas,
│                                 CRUD, procesamiento de planilla y reportes
├── vista/
│   └── vendedor_vista.py         Menús, lectura y validación de datos, mensajes
├── controlador/
│   └── vendedor_controlador.py   Recibe la opción del usuario y conecta vista y modelo
└── main.py                       Punto de entrada del sistema
```

## Funcionalidades

- **Gestión de vendedores:** registrar, consultar, modificar, eliminar y listar.
- **Datos del mes:** ventas, horas extra, días de ausencia y bono especial.
- **Planilla:** procesamiento individual con desglose completo, o de todos los
  vendedores indicando cuántas planillas se procesaron y cuántas se omitieron.
- **Reportes:** reporte general, mayores ventas, mayor cumplimiento, total y
  promedio de ventas, vendedores bajo la meta, total de comisiones, total de
  planilla y estadísticas por categoría.
- **Nuevo mes:** reinicia los datos mensuales y conserva los acumulados de cada
  vendedor.

## Consideraciones para la revisión

- Se agregó la lista `comisiones_mes`, además de las 6 listas obligatorias,
  para el reporte de total de comisiones. Se mantiene sincronizada igual que
  las demás: se agrega al registrar, se elimina en la misma posición y se
  reinicia en el nuevo mes.
- Los cálculos de planilla están en la clase `Vendedor` (modelo). La vista solo
  pide y muestra datos; no contiene cálculos ni accede a las listas.
- Al eliminar un vendedor se usa `pop(posicion)` en todas las listas para
  mantener la correspondencia por posición.
- Validaciones incluidas:
  - Cédulas duplicadas.
  - Vendedores inexistentes al consultar, modificar, eliminar o procesar.
  - Categoría válida (Junior, SemiSenior o Senior).
  - Salario base y meta mensual mayores que cero, para evitar la división
    entre cero.
  - Ventas, horas extra, días de ausencia y bono especial no negativos.
  - No se procesa dos veces la planilla de un vendedor en el mismo mes.
  - No se modifican los datos del mes de un vendedor cuya planilla ya fue
    procesada.
  - Confirmación antes de iniciar un nuevo mes.
- El programa no valida que se escriban letras donde se pide un número; esa
  validación no forma parte de las mínimas del enunciado.
