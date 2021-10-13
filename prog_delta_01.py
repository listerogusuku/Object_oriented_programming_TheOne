# n = 2
































# s = str(n)
# if n % 2 != 0:
#     s += ' (ímpar)'


# ano = 2021


# #Código original:

# if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
#     s = str(ano)
# else:
#     s = str(ano) + ' (normal)'




# #Código reescrito:

# s = str(ano)
# if (ano % 400 != 0) and (ano % 4 != 0 or ano % 100 == 0):
#     s += ' (normal) '







# #Código original:

# def divide(a, b):
#     if b == 0:
#         return a
#     else:
#         return a / b




# #Código reescrito:

# def divide(a, b):
#     if b == 0:
#         return a
#     return a / b





'''

def verifica_nota(nota_provas, nota_de_listas, nota_de_projetos):
    if nota_provas < 5:
        return False
    elif (nota_de_listas + nota_de_projetos)/2 >= 7:
        return True



def verifica_nota(nota_provas, nota_de_listas, nota_de_projetos):
    if nota_provas >= 5 and (nota_de_listas + nota_de_projetos)/2 >= 7:
        return True
    else:
        return False



def verifica_correspondente(a, op, b):
    if op != '+' or '-' or '*' or '/':
        return 0
    else:
        return a op b

'''



# i = 0

# while i < 5:
#     print(i)
#     i+=1

# k = 1
# while k <= 15:
#     w = k
#     k += 1
#     print(k, w)

# for i in range(1, 16):
#     w = i
#     print(i, w)


# for i in range(1, 10, 2):
#     print(f'{i} é ímpar')


# j = 1
# while j < 10:
#     print(j)
#     j+=2

'''
def laco_interno():
    for j in range(3):
        print('*', end='')
    print()

for i in range(3):
    laco_interno()

'''

# s = 0
# for x in lista:
#     s += x
# m = s / len(lista)


# i = 0
# for j in lista:
#     i = (i-j) * (i-j)
# resp = i/len(lista)


# def decrescente(lista):
#     for i in range(1, len(lista)):
#         if v[i] < v[i + 1]:
#             return False
#     return True


"""

# import math
from math import inf

# print(math.inf)

# lista = []

def maior_modulo():
    for i in len(lista-1):
        if 

"""

'''
def inteiros_positivos(lista):
    lista_pares = []
    lista_impares = []
    for i in range(len(lista)):
        # print(i)
        if lista[i] % 2 == 0:
            # print(lista[i])
            lista_pares.append(lista[i])
        else:
            lista_impares.append(lista[i])
    return lista_pares, lista_impares


lista_inteiros = [97,3,7,6,8,10,24,5,1,23,45,68,70,80]

print(inteiros_positivos(lista_inteiros))
'''

nomes_dos_alunos = [
    ['gabrielaa3@al.insper.edu.br', 'DE ARAUJO ALVES', 'GABRIEL'],
    ['listeror@al.insper.edu.br', 'OGUSUKU RIBEIRO', 'LISTER'],
    ['pedroom@al.insper.edu.br', 'OSBORN MAHFUZ', 'PEDRO'],
]


# i = 0
# while i < len(nomes_dos_alunos):
#     dict_user = dict()
#     dict_name = dict()
#     lista_de_dicionarios = []
#     guarda_user = nomes_dos_alunos[i][0]
#     x = guarda_user.find('@')
#     dict_user['login'] = guarda_user[:x]
#     guarda_nome = nomes_dos_alunos[i][2]
#     guarda_sobrenome = nomes_dos_alunos[i][1]
#     string_vazia = ' '
#     dict_name['nome'] =  guarda_nome + string_vazia + guarda_sobrenome
#     lista_de_dicionarios.append(dict_user)
#     lista_de_dicionarios.append(dict_name)
#     print(lista_de_dicionarios)
#     i+=1









'''
def registra_alunos(nomes_dos_alunos):
    i = 0
    lista_de_dicionarios = []
    while i < len(nomes_dos_alunos):
        dict_aluno = dict()
        # dict_name = dict()
        guarda_user = nomes_dos_alunos[i][0]
        x = guarda_user.find('@')
        dict_aluno['login'] = guarda_user[:x]
        guarda_nome = nomes_dos_alunos[i][2]
        guarda_sobrenome = nomes_dos_alunos[i][1]
        dict_aluno['nome'] =  guarda_nome + ' ' + guarda_sobrenome
        lista_de_dicionarios.append(dict_aluno)
        i+=1
    return lista_de_dicionarios


print(registra_alunos(nomes_dos_alunos = [
    ['gabrielaa3@al.insper.edu.br', 'DE ARAUJO ALVES', 'GABRIEL'],
    ['listeror@al.insper.edu.br', 'OGUSUKU RIBEIRO', 'LISTER'],
    ['pedroom@al.insper.edu.br', 'OSBORN MAHFUZ', 'PEDRO'],
]))
'''










'''
materias_insper = [
    ['COMNUV - Computação em Nuvem', 'Engenharia de Computação'],
    ['MATMEC - Materiais para Construção Mecânica', 'Engenharia Mecânica'],
    ['DESCOM - Design de Computadores', 'Engenharia de Computação'],
    ['MAQACI - Máquinas Elétricas e Acionamentos', 'Engenharia Mecatrônica'],
    ['AUTIND - Automação Industrial', 'Engenharia Mecatrônica'],
    ['TRACAL - Transferência de Calor', 'Engenharia Mecânica'],
]


materias = dict()
lista_materias_comp, lista_materias_mecat, lista_materias_mec = [], [], []

for i in materias_insper:
    if i[1] == "Engenharia de Computação":
        materia_comp = i[0]
        lista_materias_comp.append(materia_comp[9:])
        materias['COMP'] = lista_materias_comp
    elif i[1] == 'Engenharia Mecatrônica':
        materia_mecat = i[0]
        lista_materias_mecat.append(materia_mecat[9:])
        materias['MECAT'] = lista_materias_mecat
    else:
        materia_mec = i[0]
        lista_materias_mec.append(materia_mec[9:])
        materias['MEC'] = lista_materias_mec
print()
print(materias)
print()





# {
#     'COMP': ['Computação em Nuvem', 'Design de Computadores'],
#     'MECAT': ['Máquinas Elétricas e Acionamentos', 'Automação Industrial'],
#     'MEC': ['Materiais para Construção Mecânica', 'Transferência de Calor'],
# }




# materias_do_Insper = {
#     'COMP': ['Computação em Nuvem', 'Design de Computadores'],
#     'MECAT': ['Máquinas Elétricas e Acionamentos', 'Automação Industrial'],
#     'MEC': ['Materiais para Construção Mecânica', 'Transferência de Calor'],
# }

# print(materias_do_Insper.keys())






# # 
# # 
# for i in nomes_dos_alunos:
#     dict_user = dict()
#     print(nomes_dos_alunos[i][0])


# # nomes_dos_alunos2 = [
# #     {'login': 'gabrielaa3', 'nome': 'GABRIEL DE ARAUJO ALVES'},
# #     {'login': 'listeror', 'nome': 'LISTER OGUSUKU RIBEIRO'},
# #     {'login': 'pedroom', 'nome': 'PEDRO OSBORN MAHFUZ'},
# # ]


'''

'''
matriz_01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def transposta(matriz):
    for i, j in enumerate(matriz):
        print(i, j)

print(transposta(matriz_01))
'''



dict_list = [
    {'id': 123, 'nome': 'MARIANA', 'sobrenome': 'SOUZA', 'idade': 25},
    {'id': 456, 'nome': 'JOSÉ', 'sobrenome': 'COSTA E SILVA', 'idade': 44},
    {'id': 789, 'nome': 'MARIA', 'sobrenome': 'DA SILVA', 'idade': 37},
]



dicionario_final = dict()
for i in dict_list:
    new_key = i['id']
    dicionario_final[new_key] = new_key
    complet_name = i['nome'].capitalize() + ' ' + i['sobrenome'].title()#.capitalize()
    if 'DA' or 'DE' or 'DO' or 'E' in i['sobrenome']: #complet_name[espaco:]:
        complet_name = complet_name.replace('Da', 'da')
        complet_name = complet_name.replace('Do', 'do')
        complet_name = complet_name.replace('De', 'de')
        complet_name = complet_name.replace('E', 'e')

    dicionario_dados = dict()

    for j in dicionario_final:
        print(j)
        dicionario_final[j] = complet_name
        i['id'] = complet_name
    
print(dicionario_final)













# dicionario_final = dict()
# for i in dict_list:
#     new_key = i['id']
#     complet_name = i['nome'].capitalize() + ' ' + i['sobrenome']
#     if 'DA' or 'DE' or 'DO' or 'E' in complet_name:
#         # print(i['sobrenome'])
#         x = complet_name.find('DA')
#         print(complet_name[x:])
#     else:
#         continue

#     dicionario_final = new_key
#     # print(complet_name)



# # {
# #     123: {'nome': 'Mariana Souza', 'idade': 25},
# #     456: {'nome': 'José Costa e Silva', 'idade': 44},
# #     789: {'nome': 'Maria da Silva', 'idade': 37},
# # }