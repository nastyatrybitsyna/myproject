def swapnumbers(array):
    if len(array) % 2 != 0:
        print("Масив повинен мати парну кількість елементів")
        return

    mid = len(array) // 2

    array[:mid], array[mid:] = array[mid:], array[:mid]
  
if __name__ == "__main__":
    my_array = [7, 3, 2, 12, 9, 4]
    print("Початковий масив: ", my_array)

    swapnumbers(my_array)
    print("Змінений масив: ", my_array)
    
