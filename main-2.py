if __name__ == "__main__":
    number = input("Vvedit chislo: ") 
    
    if number.isdigit():
        number = int(number)
    if number % 3 == 0:
        print(f"{number} mozna podiliti na 3.")
    else:
        print(f"{number} ne mozna podiliti na 3.")
else:
    print("Vvedene znachennya ne e chislom.")