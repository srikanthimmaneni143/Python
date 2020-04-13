class student:
    College=None
    Name = None
    phone = None
    ID = None
    def __init__(self):
        self.Name='Not yet given'
        self.phone='Not yet given'
        self.ID='Not yet given'
    def add_details(self,aa,bb,cc):
        self.Name=aa
        self.phone=bb
        self.ID=cc
    @classmethod
    def Modify(cls):
        cls.College='SMCEEE'
        cls.phone='9555556661'
        cls.ID='I1'
        cls.Name='Sri'

st1=student()
DB=list()
DB.append(student())
DB.append(student())



DB[0].Modify()

DB[0].add_details('Anvesh','8106930836','P1')
print('Name: ',DB[0].Name,'\tPhone: ',DB[0].phone,'\tID: ',DB[0].ID,'\t College: ',DB[0].College)
DB[1].add_details('Sv','9652556628','C1')
print('Name: ',DB[1].Name,'\tPhone: ',DB[1].phone,'\tID: ',DB[1].ID,'\t College: ',DB[0].College)

DB[0].add_details('Anveshhhh','88888106930836','P111')
print('Name: ',DB[0].Name,'\tPhone: ',DB[0].phone,'\tID: ',DB[0].ID,'\t College: ',DB[0].College)



#print(type(DB))
#print("Length is: ",len(DB))
#print('Name: ',DB[0].Name,'\tPhone: ',DB[0].phone,'\tID: ',DB[0].ID)
##print('Name: ',st1.Name,'\nPhone: ',st1.phone,'\nID: ',st1.ID)
#st1.add('Srikanth','9542019638','i1')
#print('Name: ',st1.Name,'\nPhone: ',st1.phone,'\nID: ',st1.ID)
