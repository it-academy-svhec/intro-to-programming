def find_element(elements, target):
    for element in elements:
        if element == target:
            return True
        else:
            return False


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_element = int(input("Enter the element you are looking for: "))

result = find_element(elements, search_element)
print(result)

print("Found the element." if result else "Element not found.")
