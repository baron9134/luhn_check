def luhn_check(card_number: str) -> bool:
    card_number = card_number.replace(" ", "")
    total = 0
    reversed_digits = card_number[::-1]

    for index, digit in enumerate(reversed_digits):
        digit = int(digit)
        if index % 2 == 1:  # On double UNE FOIS sur deux à partir de la droite
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


def get_card_number():
    card_numbers = [
        "4539 1488 0343 6467",  # ✅ valide (Visa)
        "5500 0000 0000 0004",  # ✅ valide (Mastercard)
        "1234 5678 9012 3456",  # ❌ invalide
        "4012 8888 8888 1881",  # ✅ valide (Visa)
        "4111 1111 1111 1112"   # ❌ invalide
    ]

    # Demande à l'utilisateur de saisir un numéro
    user_card = input("Entrez votre numéro de carte (avec ou sans espaces) : ").replace(" ", "")

    while len(user_card) != 16 or not user_card.isdigit():
        print("Numéro invalide. Il doit contenir 16 chiffres.")
        user_card = input("Entrez à nouveau votre numéro : ").replace(" ", "")

    full_number = ' '.join([user_card[i:i+4] for i in range(0, 16, 4)])  # formatage propre
    card_numbers.append(full_number)

    print("\n🔍 Vérification des numéros de carte :\n")
    for card in card_numbers:
        if luhn_check(card):
            print(f"{card} est  VALIDE")
        else:
            print(f"{card} est  INVALIDE")

# Lancer le programme
get_card_number()
