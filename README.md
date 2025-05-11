# luhn_check
i would create my first algorithm i wondered which one i can begin so i choose luhn checking who is system of verification of card number 
# 🔐 Luhn Check – Vérification de Numéros de Cartes Bancaires

Ce projet Python permet de **vérifier la validité des numéros de cartes bancaires** à l’aide de l’**algorithme de Luhn**, utilisé par la majorité des systèmes de paiement (Visa, Mastercard, etc.).

---

## ✨ Fonctionnalités

- ✅ Vérification automatique d'une liste de cartes prédéfinies
- 📥 Saisie manuelle d'un numéro de carte par l'utilisateur
- 🧠 Implémentation claire de l'algorithme de Luhn
- 📄 Formatage propre en groupes de 4 chiffres

---

## 🧪 Exemple d'utilisation

```bash
$ python luhn_checker.py
Entrez votre numéro de carte (avec ou sans espaces) : 4539148803436467

🔍 Vérification des numéros de carte :

4539 1488 0343 6467 est  VALIDE  
5500 0000 0000 0004 est  VALIDE  
1234 5678 9012 3456 est  INVALIDE  
4012 8888 8888 1881 est  VALIDE  
4111 1111 1111 1112 est  INVALIDE  
4539 1488 0343 6467 est  VALIDE  
