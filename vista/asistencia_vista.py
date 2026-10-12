class AsistenciaVista:
    
    def mostrar_menu(self):
        print("---------------------")
        print("        MENU        ")
        print("1. Registrar estudiante ")
        print("2. Registrar asistencia semanal ")
        print("3. Consultar asistencia de un estudiante ")
        print("4. Mostrar resumen general de asistencia ")
        print("5. Salir ")
        print("----------------------------------------")
        print()
        return int(input("Digite la opcion que desea: "))
    
    def solicitar_datos_estudiante(self):
        carnet=input("Digite el carnet: ")
        nombre=input("Digite el nombre: ")
        return carnet, nombre
    
    def solicitar_carnet(self):
        return input("Digite el carnet: ")
    
    def solicitar_asistencia_semanal(self, dias ):
        asistencia_semana=[]  # ocupo una lista para guardar resultados
        
        for dia in dias:
            valor= int(input(f"Digite la asistencia del dia {dia} (1) Si  ,  0) No): "))
            asistencia_semana.append(valor)
        return asistencia_semana
    
    def mostrar_consulta_estudiante(self, estudiante, fila_asistencia, total_asistencias, dias ):
        print("-------------  ASISTENCIA DEL ESTUDIANTE --------------- ")
        print(estudiante)
        
        for i in range(len(dias)):
            print(f"{dias[i]}: {fila_asistencia[i]}")
            
        print(f"total dias que asistio: ", total_asistencias)
            
    def mostrar_resumen_general(self, resumen, promedio_grupo, dia_mayor, cantidad_mayor_asistencias):
        print("-----------------RESUMEN GENERAL DE ASISTENCIA ------------------")
        
        if resumen == 0:
            print("No hay estudiantes registrados")
            return 
            
        
        for estudiante , total_asistencia in resumen:
            print(f"{estudiante} ---Total asistencias: {total_asistencia} ")
            
        print(f"Promedio del total de asistencias : {promedio:.2f} dias ")
        print(f"El dia con mayor asistencias es: {dia_mayor} {(cantidad_mayor_asistencias)}")
        
    def mostrar_mensaje(self, mensaje):
        print(mensaje)
    
        
    