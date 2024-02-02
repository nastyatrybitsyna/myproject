if __name__ == "__main__": 

    def v(lst):
        res = 1
        for e in lst:
            res *= e
        return res

    list = [5, 12, 7, 2]
    result = v(list)
    print(f"Dobutok elementiv u spysku {list} dorivnyuye {result}")