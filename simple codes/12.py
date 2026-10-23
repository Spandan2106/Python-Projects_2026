#Sort dictionary by keys, Sort dictionary by values,Find student with highest marks, Merge two dictionaries manually
#Sort dictionary by keys
def dic_sort_by_keys(d):
    return dict(sorted(d.items()))
#Sort dictionary by values
def dic_sort_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
#Find student with highest marks
def highest_marks(d):
    
    return max(d, key=d.get)    
#Merge two dictionaries manually
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
#Example usage
dic1 = dict(item.split(":") for item in input("Enter first dictionary (key:value pairs separated by commas): ").split(","))
dic2 = dict(item.split(":") for item in input("Enter second dictionary (key:value pairs separated by commas): ").split(","))
print("Sorted by keys:", dic_sort_by_keys(dic1))
print("Sorted by values:", dic_sort_by_values(dic1))
print("Student with highest marks:", highest_marks(dic1))
print("Merged dictionaries:", merge_dicts(dic1, dic2))