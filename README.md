# Sistema de Gestión de Planilla y Rendimiento de Vendedores

Proyecto #1 – Desarrollo de Software II – Informática Empresarial – II Ciclo 2026

Sistema de consola en Python que administra a los vendedores de una empresa de
equipos tecnológicos y calcula su planilla mensual: comisión según el
cumplimiento de la meta, ajuste por categoría, horas extra, bonos, deducciones,
impuesto académico y salario neto. Además genera reportes de ventas y
rendimiento, y permite iniciar un nuevo mes sin perder los acumulados
históricos de cada vendedor.

## Desarrolladores

| Nombre | Carné | Módulo a cargo |
|---|---|---|
| Ariana | _carné_ | Gestión de vendedores y datos del mes |
| Michelle | _carné_ | Procesamiento de planilla |
| Carlos | _carné_ | Reportes y estadísticas |

## Stack tecnológico

| Tecnología | Uso en el proyecto |
|---|---|
| **Python 3** | Lenguaje de programación de todo el sistema (sin librerías externas) |
| **Programación Orientada a Objetos** | Clase `Vendedor` con atributos privados y métodos get/set |
| **Patrón MVC** | Separación en Modelo, Vista y Controlador |
| **Listas unidimensionales** | Lista de objetos `Vendedor` y listas asociadas por posición (sin matrices ni diccionarios) |
| **Thonny** | Entorno de desarrollo (IDE) |
| **Git / Git Bash** | Control de versiones |
| **GitHub** | Repositorio remoto, ramas por integrante y Pull Requests |

El sistema trabaja en memoria: no usa archivos ni bases de datos.

## Cómo ejecutar

1. Tener instalado Python 3.
2. Abrir la carpeta del proyecto.
3. Ejecutar `main.py`:

```
python main.py
```

En Thonny: abrir `main.py` y presionar **Run** (F5).
Siempre se debe ejecutar `main.py`, no los otros archivos.

## Estructura del proyecto (MVC)

```
proyecto_planilla/
├── modelo/
│   ├── vendedor.py               Clase Vendedor (atributos privados, get/set)
│   └── registro_vendedores.py    Listas, búsquedas, cálculos y reportes
├── vista/
│   └── vendedor_vista.py         Menús, lectura de datos y mensajes
├── controlador/
│   └── vendedor_controlador.py   Conecta la vista con el modelo
└── main.py                       Punto de entrada del sistema
```

## Funcionalidades

- **Gestión de vendedores:** registrar, consultar, modificar, eliminar y listar.
- **Datos del mes:** ventas, horas extra, días de ausencia y bono especial.
- **Planilla:** procesamiento individual o de todos los vendedores, con control
  para no procesar dos veces al mismo vendedor en el mismo mes.
- **Reportes:** reporte general, mayores ventas, mayor cumplimiento, total y
  promedio de ventas, vendedores bajo la meta, total de comisiones, total de
  planilla y estadísticas por categoría.
- **Nuevo mes:** reinicia los datos mensuales y conserva los acumulados.

## Organización del trabajo

Cada archivo está dividido en secciones con el comentario
`===== INTEGRANTE X =====` y cada integrante escribe solo en su sección.

| Rama | Responsable |
|---|---|
| `main` | Versión estable (solo se actualiza con Pull Request) |
| `gestion` | Ariana |
| `planilla` | Michelle |
| `reportes` | Carlos |

## Consideraciones para la revisión

- Se agregó la lista `comisiones_mes`, además de las 6 listas obligatorias,
  para calcular el reporte de total de comisiones sin recalcularlas. Se mantiene
  sincronizada igual que las demás.
- El desglose de la planilla se devuelve como tupla; no se usan diccionarios
  ni listas bidimensionales.
- Validaciones incluidas: cédulas duplicadas, vendedores inexistentes, meta
  mayor que cero, doble procesamiento de planilla y confirmación antes de
  iniciar un nuevo mes.
