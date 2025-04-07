lista =  []

while True:
    item = input('>>')
    if item == 'fim':
        lista.append(item)
        print(f'a lista tem {len(item)}')
        break
    else:
        lista.append(item)
        print(f'a lista tem {len(lista)}')
        break


lista = []

while True:
     addItem = input('adicione um Item: ')
     lista.append(addItem)

     if addItem == 'fim':
         break

     lista.append(addItem)

print(f' o tamanho da minha lista é: {len(lista)}')

















