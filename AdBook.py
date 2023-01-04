'Skonstruuj pętlę, która wyświetli całą zawartość listy wizytówek tak'
' aby w jednej linii widoczne było imię, nazwisko i adres e-mail właściciela wizytówki.'

class Business_card:
    def __init__(self, name, surname, company_name, position, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.email = email

BC_1 = Business_card(name = 'Tytus', surname = 'Bomba',  company_name = 'Gwiezdna Flota',position = 'Kapitan', email = 'KapitanBomba@gmail.com')

BC_2 = Business_card(name = 'Janusz', surname = 'Sram', company_name = 'Gwiezdna Flota', position = 'Szeregowy', email = 'JanuszSram@gmail.com')

BC_3 = Business_card(name = 'Sebastian', surname = 'Bąk', company_name = 'Gwiezdna Flota', position = 'Szeregowy', email = 'SebastianBak@gmail.com')

BC_4 = Business_card(name = 'Michał', surname = 'Jachaś', company_name = 'Galak Pizza', position = 'Prezes', email = 'Margharita30cm@onet.pl')

BC_5 = Business_card(name = 'Michał', surname = 'Głuś', company_name = 'Kosmici niezrzeszeni', position = 'Szpieg', email = 'Mikele@onet.pl')

list = (BC_1, BC_2, BC_3, BC_4, BC_5)

for Business_card in list:
    print(Business_card.name,",", Business_card.surname,",", Business_card.email)