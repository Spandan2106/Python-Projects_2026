
#Find index of element without index(), Perform set union, intersection, difference, Check common elements using sets,Find unique elements using set.
#Find index of element without index() in set
def search_index(s, element):
    for index, value in enumerate(s):
        if value == element:
            return index
    return -1
#Perform set union, intersection, difference
def set_operations(set1, set2):
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    return union, intersection, difference
#Check common elements using sets
def common_elements(set1, set2):
    return set1.intersection(set2)
#Find unique elements using set
def unique_elements(s):
    return set(s)
# Example usage
set1 = {1, 2, 3, 4,5,6,7,8,9,0}
set2 = {3, 4, 5, 6,7,8,1,2,22,33,44,55,66,77,88,99,100}
print("Index of element 3 in set1:", search_index(set1, 3))
union, intersection, difference = set_operations(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Common elements:", common_elements(set1, set2))
print("Unique elements in set1:", unique_elements(set1))

