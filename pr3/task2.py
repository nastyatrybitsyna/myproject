if __name__ == "__main__": 
    def v(n):
        n_str = str(n)
        nn = int(n_str * 2)
        nnn = int(n_str * 3)
        result = n + nn + nnn
        return result
    n = int(input("Введіть ціле число n: "))
    result = v(n)
    print(f"Результат обчислення для {n} + {n}{n} + {n}{n}{n} = {result}")