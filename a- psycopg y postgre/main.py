from conexion.cursor import CursorPool
from logger import log
if __name__ == '__main__':
    try:
        with CursorPool() as cp:
            cp.execute("SELECT 1")
            if cp.fetchone():
                print("Conexion exitosa")
            else:
                print("Conexion fallida")
    except Exception as e:
        log.error(f'Error al conectar a la base de datos - {e}')
        exit()
    while True:
        opcion = input('[1] Personas\n' \
                    '[2] Contratos\n' \
                    '[3] Contratos por persona\n' \
                    '[4] Salir\n' \
                    'Ingrese una opcion: ')
        if opcion == '1':
            from controladores.persona import MenuPersona
            MenuPersona()
        elif opcion == '2':
            from controladores.contrato import MenuContrato
            MenuContrato()
        elif opcion == '3':
            from controladores.contratoPersona import MenuContratoPersona
            MenuContratoPersona()
        elif opcion == '4':
            break
        else:
            print('Opcion invalida')
