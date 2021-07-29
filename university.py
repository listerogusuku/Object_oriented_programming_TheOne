class University(object):
    def __init__(self, regMEC, regDOU):
        self.MEC = regMEC
        self.DOU = regDOU
        print(f'\nConstrutor inicializado com sucesso.\n')
    def UniversityInfos(self, nome):
        print(f'Name: {nome};\nReg. MEC nº: {self.MEC};\nReg. DOU ano: {self.DOU}.\n')


Insper = University(2553, '17/02/2020')
Insper.UniversityInfos('Insper')