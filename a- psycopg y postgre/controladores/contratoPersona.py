from modelos.contratoPersona import ContratoPersona
from DTO.contratoPersonaDTO import ContratoPersonaDTO
from logger import log

def MostrarContratosPersona():
    contratosPersonas = ContratoPersonaDTO.seleccionar()
    if not contratosPersonas:
        log.error("No se pudo seleccionar los contratosPersonas")
    print(f'Listado de contratosPersonas'.center(50, '='))
    print('Id\tIdContrato\tIdPersona')
    for contratoPersona in contratosPersonas:
        print(f'{contratoPersona.id}\t\t{contratoPersona.id_contrato}\t\t{contratoPersona.id_persona}')

def MostrarContratoPersona():
    id = int(input('Ingrese el id del contratoPersona: '))
    contratoPersona = ContratoPersonaDTO.seleccionarPorId(id)
    if not contratoPersona:
        log.error("No se pudo seleccionar el contratoPersona")
    else:
        print(f'ContratoPersona\n{contratoPersona}')

def AgregarContratoPersona():
    idContrato = int(input('Ingrese el id del contrato: '))
    idPersona = int(input('Ingrese el id de la persona: '))
    contratoPersona = ContratoPersona(idContrato,idPersona)
    if ContratoPersonaDTO.insertar(contratoPersona):
        log.info("ContratoPersona creado")
    else:
        log.error("No se pudo crear el contratoPersona")

def MenuContratoPersona():
    print(f'Menu Contratos Persona'.center(50, '='))
    while True:
      opcion = input('[1] Mostrar todas las contratos\n' \
                     '[2] Mostrar un contrato\n' \
                     '[3] Agregar un contrato\n' \
                     '[4] Salir\n' \
                     'Ingrese una opcion: ')
      if opcion == '1':
          MostrarContratosPersona()
      elif opcion == '2':
          MostrarContratoPersona()
      elif opcion == '3':
          AgregarContratoPersona()
      elif opcion == '4':
          break
      else:
        print('Opcion invalida')