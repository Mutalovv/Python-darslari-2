from uuid import uuid4
class Avto:
    __avtolar_soni = 0

    def __init__(self, kompaniya, model, narx, yil, __km=0):
        self.kompaniya = kompaniya
        self.model = model
        self.narx = narx
        self.yil = yil
        self.__km = __km
        self.__id = uuid4()

        Avto.__avtolar_soni += 1 

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    @classmethod 
    def get_avtolar_soni(cls):
        return cls.__avtolar_soni

avto_1 = Avto("Gm","Gentra",18000,2020,10200)
avto_2 = Avto("GM","Cobalt",16000,2021,35000)

print(avto_1.get_km())
print(avto_1.get_id())
print(avto_1.get_avtolar_soni())
print(avto_2.get_km())
print(avto_2.get_id())

    
