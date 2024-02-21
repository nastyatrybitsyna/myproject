if __name__ == "__main__": 
   import math

def P():
    try:
        r = float(input("Vvedit radiys kola: "))
        area = math.pi * r ** 2
        print(f"Plosha kola z radiysom {r} odynyts: {area:.2f}")

    except ValueError:
        print("Error: Write korekt chislo.")

P()
