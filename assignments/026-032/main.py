# 01
my_list = [1, 2, 3, 3, 4, 5, 1]

uniquSet = set(my_list)
unique_list = list(uniquSet)

print( unique_list)
print(type( unique_list))
unique_list.pop(-1)
print( unique_list)

# 02
print("#"*10)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums|letters)
print(nums.union(letters))
print(set(list(nums) + list(letters)))
# # print(nums + letters)
# print(nums+letters)

# 03
print("#"*10)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
letters.discard("C")
my_set.update(letters)
print(my_set)
letters.discard("C")