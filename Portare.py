import requests
from bs4 import BeautifulSoup

while True:
    number = input("Enter a number: ")

    # Verifică dacă numărul este format doar din cifre și are o lungime corectă
    if number.isdigit() and len(number) == 10:  # Presupunând că numărul de telefon are 10 cifre în România
        # URL-ul paginii de unde vrei să preiei datele
        url = 'https://www.portabilitate.ro/NumberSearch.aspx?lang=ro&number=' + str(number)

        # Faci o solicitare HTTP pentru a obține HTML-ul
        response = requests.get(url)
        html = response.text

        # Parsezi HTML-ul cu BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Utilizează selectorul CSS pentru a găsi containerul cu informațiile despre numărul de telefon
        container = soup.select_one('#ctl00_cphBody_panelDetails > table')

        # Verifică dacă containerul a fost găsit
        if container:
            # Caută textul folosind 'string' în loc de 'text'
            operator_curent_label = container.find(string='Operator curent:')
            if operator_curent_label:
                operator_curent = operator_curent_label.find_next().get_text(strip=True)
            else:
                operator_curent = "Informație lipsă"

            operator_initial_label = container.find(string='Operator iniţial:')
            if operator_initial_label:
                operator_initial = operator_initial_label.find_next().get_text(strip=True)
            else:
                operator_initial = operator_curent

            data_curenta_label = container.find(string='Data curentă:')
            if data_curenta_label:
                data_curenta = data_curenta_label.find_next().get_text(strip=True)
            else:
                data_curenta = "Informație lipsă"

            tip_numar_label = container.find(string='Tip număr:')
            if tip_numar_label:
                tip_numar = tip_numar_label.find_next().get_text(strip=True)
            else:
                tip_numar = "Informație lipsă"

            print(f"Operator curent: {operator_curent}")

            if operator_curent != operator_initial:
                print(f"Operator inițial: {operator_initial}")

            print(f"Data curentă: {data_curenta}")
            print(f"Tip număr: {tip_numar}")

            break  # Ieși din buclă dacă informațiile au fost găsite și afișate corect
        else:
            print("Eroare la găsirea containerului")
    else:
        print("Numărul introdus nu este valid. Te rog să introduci un număr de telefon valid format doar din 10 cifre.")
