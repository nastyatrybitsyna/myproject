if __name__ == "__main__":
    n = int(input("Vvedit chislo: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("Summa chisel vid 1 do", n, "=", sum)