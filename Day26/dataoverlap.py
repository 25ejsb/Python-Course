nums1 = None
nums2 = None
with open("Day26/list1.txt") as file:
    nums1 = [num for num in str(file.read()).split("\n")]
with open("Day26/list2.txt") as file:
    nums2 = [num for num in str(file.read()).split("\n")]

result = [num for num in nums1 if num in nums2]
print(result)