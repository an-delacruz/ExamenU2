from modelos.persona import Persona
from DTO.personaDTO import PersonaDTO
from logger import log

def MostrarPersonas():
    personas = PersonaDTO.seleccionar()
    if not personas:
        print('No hay personas')
    print(f'Listado de personas'.center(50, '='))
    print('Id\tNombre\tEdad\tCorreo')
    for persona in personas:
        print(f'{persona.id}\t{persona.nombre}\t{persona.edad}\t{persona.correo}')
        
def MostrarPersona():
    id = int(input('Ingrese el id de la persona: '))
    persona = PersonaDTO.seleccionarPorId(id)
    if not persona:
        log.error("No se pudo encontrar la persona")
    else:
        print(f'Persona\n{persona}')
    
def CrearPersona():
    nombre = input('Ingrese el nombre de la persona: ')
    edad = int(input('Ingrese la edad de la persona: '))
    correo = input('Ingrese el correo de la persona: ')
    persona = Persona(nombre, edad, correo)
    if PersonaDTO.insertar(persona):
        log.info("Persona creada")
    else:
        log.error("No se pudo crear la persona")

def ActualizarPersona():
    id = int(input('Ingrese el id de la persona: '))
    persona = PersonaDTO.seleccionarPorId(id)
    if not persona:
        log.error("No se pudo seleccionar la persona")
    else:
        print(f'Persona\n{persona}')
        nombre = input(f'Ingrese el nombre de la persona ({persona.nombre}): ') or persona.nombre
        edad = input(f'Ingrese la edad de la persona ({persona.edad}): ') or persona.edad
        correo = input(f'Ingrese el correo de la persona ({persona.correo}): ') or persona.correo
        log.debug(f'Persona antes actualizacion: {persona}')
        persona.nombre = nombre
        persona.edad = edad
        persona.correo = correo
        if PersonaDTO.actualizar(persona):
            log.debug(f'Persona actualizada: {persona}')
            print('Persona actualizada')
        else:
            log.error("No se pudo actualizar la persona")
            
def EliminarPersona():
    id = int(input('Ingrese el id de la persona: '))
    persona = PersonaDTO.seleccionarPorId(id)
    if not persona:
        log.error("No se pudo seleccionar la persona")
    else:
        print(f'Persona\n{persona}')
        if PersonaDTO.eliminar(id):
            log.info("Persona eliminada {persona}")
        else:
            log.error("No se pudo eliminar la persona")

def MostrarContratosPersona():
    correo = input('Ingrese el correo de la persona: ')
    contratos = PersonaDTO.seleccionarContratosPorCorreo(correo)
    if not contratos:
        log.error("No se pudo seleccionar los contratos")
    else:
        print(f'Contratos de {correo}'.center(50, '='))
        print('Id\tFecha\tValor')
        for contrato in contratos:
            print(f'{contrato.id}\t{contrato.fecha_inicio}\t{contrato.costo}')

        suma = sum(contrato.costo for contrato in contratos)
        print(f'El costo total de los contratos es: {suma}')
        
        
def MenuPersona():
    print(f'Menu Personas'.center(50, '='))
    while True:
        opcion = input('[1] Mostrar todas las personas\n' \
             '[2] Mostrar una persona\n' \
             '[3] Crear una persona\n' \
             '[4] Actualizar una persona\n' \
             '[5] Eliminar una persona\n' \
             '[6] Mostrar contratos de una persona\n' \
             '[0] Salir\n' \
             'Seleccione una opcion: ')
        if opcion == '1':
            MostrarPersonas()
        elif opcion == '2':
            MostrarPersona()
        elif opcion == '3':
            CrearPersona()
        elif opcion == '4':
            ActualizarPersona()
        elif opcion == '5':
            EliminarPersona()
        elif opcion == '6':
            MostrarContratosPersona()
        elif opcion == '0':
            break
        else:
            print('Opcion no valida')