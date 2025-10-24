# Filename: two_sum.py

def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_index_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index_map:
            return [num_to_index_map[complement], index]
        num_to_index_map[num] = index

# --- Example Usage ---
my_nums = [2, 7, 11, 15]
my_target = 9
result = two_sum(my_nums, my_target)
print(f"Indices for target {my_target} in {my_nums}: {result}")

another_nums = [3, 2, 4]
another_target = 6
result2 = two_sum(another_nums, another_target)
print(f"Indices for target {another_target} in {another_nums}: {result2}")
