vowels = "aeiouAEIOU"


def main():
    country_name = input("insert a french country name ")
    if country_name == "Etats-Unis" or country_name == "Pays-Bas":
        print(f"les {country_name}")
    if country_name[0] in vowels:
        print(f"l' {country_name}")
    if country_name in ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"]:
        print(f"le {country_name}")
    elif country_name[-1] == "e":
        print(f'la {country_name}')
    else:
        print(f"le {country_name}")


if __name__ == "__main__":
    main()
