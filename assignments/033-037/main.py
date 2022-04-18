# 01

print(bool("S"))
print(bool(1))
print(bool((1,2)))
print(bool([1,2]))
print(bool({1,2}))

print(bool(""))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

# 02
print("#" * 10)

html = 80
css = 60
javascript = 70

print(html>50 and css>50 and javascript>50)


# 02
print("#" * 10)

num_one = 10
num_two = 20
num = 20

print(num> num_one or num> num_two)
print(num> num_one and num> num_two)

# 03
print("#" * 10)

num_one = 10
num_two = 20

result = num_one + num_two
print(result)

result**=3
print(result)

result %= 26000
print(result)

result /= 5
print(result)

result = str(result)
print(type(result))

