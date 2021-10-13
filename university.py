# class University(object):
#     def __init__(self, regMEC, regDOU):
#         self.MEC, self.DOU = regMEC, regDOU
#         # self.DOU = regDOU
#         print(f'\nConstrutor inicializado com sucesso.\n')
#     def UniversityInfos(self, nome):
#         print(f'Name: {nome};\nReg. MEC nº: {self.MEC};\nReg. DOU ano: {self.DOU}.\n')


# Insper = University(2553, '17/02/2020')
# Insper.UniversityInfos('Insper')


# def imprime_tabuada(n):
#     j=1
#     while j<=n:    
#         i=1
#         while i <= n:
#             print(j*i, end=' ')
#             i+=1
#         print()
#         j+=1

# print(imprime_tabuada(9))


# def imprime_tabuada(n):
#     j = 1
#     while j <= n:
#         c = 1
#         while c <= n:
#             print(j*c, end=' ')
#             c+=1
#         j+=1
#         print()

# print(imprime_tabuada(10))



# for i in range(10):
#     print(i)


# def imprime_grade(n):
#     j = 1
#     while j <= n:
#         i = 1
#         while i <= n:
#             print("+-+"*(n+1)/2)
#             print('| |'*(n+1)/2)
#             print('+-+'*(n+1)/2)
#             i+=1
#         j+=1

# print(imprime_grade(1))



# def numero_digitos(s):
#     digito = 0
#     for i in s:
#         print(i)
#         if i.isdigit() == True:
#             digito += 1
#     return digito

# print(numero_digitos('senha123'))

def junta_nomes(nomes_masc, nomes_fem, sobrenomes):
    lista_nomes = []
    string_vazia = ' '
    i = 0
    while i < len(nomes_masc):
        junta_nome = nomes_masc[i] + string_vazia + sobrenomes[i]
        junta_nome2 = nomes_masc[i] + string_vazia + sobrenomes[i-1]
        lista_nomes.append(junta_nome)
        lista_nomes.append(junta_nome2)
        i+=1
    j = 0
    while j < len(nomes_fem):
        junta_nome3 = nomes_fem[j] + string_vazia + sobrenomes[j]
        junta_nome4 = nomes_fem[j] + string_vazia + sobrenomes[j-1]
        lista_nomes.append(junta_nome3)
        lista_nomes.append(junta_nome4)
        j+=1

    return lista_nomes



    # for i, j in nomes_masc, sobrenomes:
    #     # print(i, j)
    #     soma_nomes = i + j
    #     print(soma_nomes)
    # novos_nomes = []
    # for i in nomes_masc:
    #     for x in sobrenomes:
    #         while len(nomes_masc) <= len(sobrenomes):
    #             novo_nome = i + x
    #             novos_nomes.append(novo_nome)
            
    # return novos_nomes


nomes_homem = ['João', 'Jose']
nomes_mulher = ['Maria', 'Mariana']
sobrenome = ['Silva', 'Souza']

print(junta_nomes(nomes_homem, nomes_mulher, sobrenome))


# def posicoes_minusculas(s):
#     pequeno = 0
#     for i in s:
#         print(i)
#         if s.islower() == True:
#             pequeno = s[i]
#         print(pequeno)

# print(posicoes_minusculas('AbCdEf'))