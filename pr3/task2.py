if __name__ == "__main__": 
    def v(n):
        n_str = str(n)
        nn = int(n_str * 2)
        nnn = int(n_str * 3)
        result = n + nn + nnn
        return result
    n = int(input("Vvedit tsile chislo n: "))
    result = v(n)
    print(f"Rezultat obchyslennya dlya {n} + {n}{n} + {n}{n}{n} = {result}")
