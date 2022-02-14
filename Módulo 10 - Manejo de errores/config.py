def main():
    try:
        config = open('config.txt')
    except FileNotFoundError:
    #except Exception:
        print('El archivo config.txt no fue encontrado')
    except IsADirectoryError:
        print('Intenta abrir un directorio')
    except (BlockingIOError, TimeoutError):
        print('El sistema de archivos esta bajo mucha carga, no es posible completar la lectura')


if __name__ == '__main__':
    main()