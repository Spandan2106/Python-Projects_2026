# to merge 2 lists and sort without using built in functions
def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    sorted_list = []
    
    while merged_list:
        min_value = merged_list[0]
        for item in merged_list:
            if item < min_value:
                min_value = item
        sorted_list.append(min_value)
        merged_list.remove(min_value)
    
    return sorted_list
# Example usage
list1 = [5, 2, 9]
list2 = [1, 4, 3]
result = merge_and_sort(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 9]
