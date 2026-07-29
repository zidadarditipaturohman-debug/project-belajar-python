weight = int(input('weight:'))
unit = input('(L)bs or (K)g')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'your weight is: {converted} kilos')
else:
    converted = weight / 0.45
    print(f'your weight is: {converted}kilos')


    #mungkin akan aku terjemahkan kalau == merupakan "yang dijawab"
    #jadi, dapat aku simpulkan memang logika dari python untuk sementara yang aku pahami adalah berurutan dari atas
    # ke bawah. dan mungkin ini yang aku pahami untuk sementara