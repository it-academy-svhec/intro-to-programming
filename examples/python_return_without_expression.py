def find_element(elements, target):
    for element in elements:
        if element == target:
            print("Found the element.")
            return


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_element = int(input("Enter the element you are looking for: "))

find_element(elements, search_element)
