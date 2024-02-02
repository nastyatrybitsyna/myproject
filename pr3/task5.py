if __name__ == "__main__":
    
    def v(num):
        if not num:
            return None  
        else:
            return min(num)
    
list = [-6, 1, 8, 12, -5]
res = v(list)
print(f"Naymenshe chyslo u spysku tse {res}")
