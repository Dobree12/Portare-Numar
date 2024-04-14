prefixe = {}
tari = []

with open("country_prefixes.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line and ':' in line:  # Verificăm dacă linia nu este goală și conține caracterul ':'
            prefix, tara = line.split(":")
            prefixe[tara.strip()] = prefix.strip()  # Adăugăm prefixul și țara în dicționar

# Dicționarul invers pentru a căuta după prefix
country_prefixes_reverse = {v: k for k, v in prefixe.items()}

# Funcție pentru a verifica prefixul introdus de utilizator și a afișa țara corespunzătoare
def check_country_by_prefix(prefix):
    if prefix in country_prefixes_reverse:
        country = country_prefixes_reverse[prefix]
        print(f"Prefixul {prefix} este asociat țării {country}")
    else:
        print("Prefixul introdus nu este asociat niciunei țări cunoscute.")

# Testarea funcției cu un prefix introdus de utilizator
user_prefix = input("Introduceți prefixul de verificat: ")
check_country_by_prefix(user_prefix)