from typing import TypeVar, List
T = TypeVar('T')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



def insert_elements(array: List[T], elements_to_insert: [T], pos: int) -> [T]:
    if pos <= len(array):
        new_array: list[T] = [None] * (len(array) + len(elements_to_insert))
        print(new_array)
        for i in range(pos - 1):
            new_array[i] = array[i]
        j = 0
        for i in range(pos - 1, pos + len(elements_to_insert) - 1):
            new_array[i] = elements_to_insert[j]
            j = j + 1
        k = pos - 1
        for i in range(pos + len(elements_to_insert) - 1, len(new_array)):
            new_array[i] = array[k]
            k = k + 1
        print(array)
        print(new_array)
    else:
        # einzufügende Position ist größer als das Array
        return []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,0]
    elementToInsert = 10
    elementsToInsert = [11,12,13,14,15]
    insert_elements(arr, elementsToInsert, 3)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
