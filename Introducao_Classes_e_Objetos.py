"""
class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 80
        self.marca = "Philips"

tv = Televisão()
tv.tamanho = 27
tv.marca = "Samsung"
tv_sala = Televisão()
tv_sala.tamanho = 52
tv_sala.marca = "XangLa"

print("tv tamanho=%d marca=%s" % (tv.tamanho,tv.marca ))
print("tv_sala tamanho=%d marca=%s" % (tv_sala.tamanho,tv_sala.marca ))

print(f"tv tamanho={tv.tamanho} marca={tv.marca}")
"""

# class Televisão:
#     def __init__(self):
#         self.ligada = False
#         self.canal = 2
#     def muda_canal_para_cima(self):
#         self.canal += 1
#     def muda_canal_para_baixo(self):
#         self.canal -= 1

# tv = Televisão()
# tv.muda_canal_para_cima()
# tv.muda_canal_para_cima()
# print(tv.canal)
# tv.muda_canal_para_baixo()
# print(tv.canal)

class Televisão():
    def __init__(self, min, max):
        self.canal = 2
        self.ligada = False
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisão(1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for i in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)
