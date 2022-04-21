senha = 1
min = int(input('Digite os minutos: '))

while min > 1:
    senha = senha * min
    min = min - 1
print('A senha de desbloqueio é LIBERDADE', senha)