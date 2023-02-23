sequence = [4, 3, 5, 0, 1]

# Your Code Here
def bubble_sort(list_of_nums):
    swaps = 0
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for idx in range(len(list_of_nums)-1):
            if list_of_nums[idx] > list_of_nums[idx+1]:
                swaps += 1
                is_swapped = True
                list_of_nums[idx], list_of_nums[idx + 1] = list_of_nums[idx+1], list_of_nums[idx]

    return list_of_nums, swaps


print(f"Final result: {bubble_sort(sequence)}")
# print(f"Swaps: {swaps}")
