class employee:
    def __init__(self,name,id_number,place,year):
        self.name=name
        self.id_number=id_number
        self.place=place
        self.year=year
    def showthedetail(self):
        print(self.name)
        print(self.id_number)
        print(self.place)
        print(self.year)

#creating object

e=employee("ishaq",529,"trichy",2026)
e.showthedetail()