
class Business_card:
    def __init__(self, name, surname, company_name, position, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email
    def _contact(self):
        return f'Kontaktuję się z ... {self.name} {self.surname} {self.position} {self.email}'

    @property
    def _name_length(self):
        return(len(self.name + " " + self.surname))


BC_1 = Business_card(name = 'Jesse', surname = 'Rager',  company_name = 'Wherehouse Music',position = 'CART provider', email = 'JesseRager@armyspy.com')
BC_2 = Business_card(name = 'Robert', surname = 'Amado', company_name = 'HomeBase', position = 'Applications engineer', email = 'RobertAmado@rhyta.com')
BC_3 = Business_card(name = 'Kevin', surname = 'Mills', company_name = 'Crazy Eddie', position = 'Crop farm manager', email = 'KevinMills@jourrapide.com')
BC_4 = Business_card(name = 'David', surname = 'Cato', company_name = 'Plan Smart', position = 'Ornamental ironworker', email = 'DavidCato@jourrapide.com')
BC_5 = Business_card(name = 'Eugenio', surname = 'Gonzalez', company_name = 'Intelacard', position = 'Bartender helper', email = 'EugenioGonzalez@armyspy.com')

BC_list = (BC_1, BC_2, BC_3, BC_4, BC_5)

for Business_card in BC_list:
    print(Business_card._contact())

#print(Business_card._name_length)

