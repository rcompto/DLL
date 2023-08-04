import ctypes

# Carregar a biblioteca .dll para 64bits
FDLL = ctypes.windll.LoadLibrary('C:\\Users\\x\\Documents\\Python\\GERSAT64.dll')
# Abrir o arquivo de saída
F = open('C:\\Users\\x\\Documents\\Python\\GERSATDLL.txt', 'w')

try:
    for i in dir(FDLL):
        F.write(i)
        F.write('\n')
finally:
    F.close()