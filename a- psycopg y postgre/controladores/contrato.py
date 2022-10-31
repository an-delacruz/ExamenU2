from modelos.contrato import Contrato
from DTO.contratoDTO import ContratoDTO
from logger import log

def MostrarContratos():
    contratos = ContratoDTO.seleccionar()
    if not contratos:
        print('No hay contratos')
    print(f'Listado de contratos'.center(50, '='))
    print('Id\tNo. Contrato\tCosto\tFecha Inicio\tFecha Fin')
    for contrato in contratos:
        print(f'{contrato.id}\t{contrato.no_contrato}\t\t{contrato.costo}\t{contrato.fecha_inicio}\t{contrato.fecha_fin}')

def MostrarContrato():
    id = int(input('Ingrese el id del contrato: '))
    contrato = ContratoDTO.seleccionarPorId(id)
    if not contrato:
        print('No se encontró el contrato')
    else:
        print(f'Contrato\n{contrato}')

def CrearContrato():
    costo = int(input('Ingrese el costo del contrato: '))
    fecha_inicio = input('Ingrese la fecha de inicio del contrato (yyyy-mm-dd): ')
    fecha_fin = input('Ingrese la fecha de fin del contrato (yyyy-mm-dd): ')
    contrato = Contrato(costo, fecha_inicio, fecha_fin)
    if ContratoDTO.insertar(contrato):
        print('Contrato creado')
    else:
        print('No se pudo crear el contrato')
    
def ActualizarContrato():
    id = int(input('Ingrese el id del contrato: '))
    contrato = ContratoDTO.seleccionarPorId(id)
    if not contrato:
        print('No se encontró el contrato')
    else:
        print(f'Contrato\n{contrato}')
        costo = int(input(f'Ingrese el costo del contrato ({contrato.costo}): ') or contrato.costo)
        fecha_inicio = input(f'Ingrese la fecha de inicio del contrato ({contrato.fecha_inicio}): ') or contrato.fecha_inicio
        fecha_fin = input(f'Ingrese la fecha de fin del contrato ({contrato.fecha_fin}): ') or contrato.fecha_fin
        log.debug(f'Contrato antes actualizacion: {contrato}')
        contrato.costo = costo
        contrato.fecha_inicio = fecha_inicio
        contrato.fecha_fin = fecha_fin
        if ContratoDTO.actualizar(contrato):
            log.debug(f'Contrato actualizado: {contrato}')
            print('Contrato actualizado')
        else:
            print('No se pudo actualizar el contrato')

def EliminarContrato():
    id = int(input('Ingrese el id del contrato: '))
    contrato = ContratoDTO.seleccionarPorId(id)
    if not contrato:
        print('No se encontró el contrato')


    if ContratoDTO.eliminar(id):
        log.debug(f'Contrato eliminado: {contrato}')
        print('Contrato eliminado')
    else:
        print('No se pudo eliminar el contrato')
        
def MenuContrato():
    print(f'Menu Contratos'.center(50, '='))
    while True:
        opcion = input('[1] Mostrar contratos\n'\
                    '[2] Mostrar contrato\n'\
                    '[3] Crear contrato\n'\
                    '[4] Actualizar contrato\n'\
                    '[5] Eliminar contrato\n'\
                    '[6] Salir\n'\
                    'Ingrese una opción: ')

        if opcion == '1':
            MostrarContratos()
        elif opcion == '2':
            MostrarContrato()
        elif opcion == '3':
            CrearContrato()
        elif opcion == '4':
            ActualizarContrato()
        elif opcion == '5':
            EliminarContrato()
        elif opcion == '6':
            break
        else:
            print('Opción inválida')
