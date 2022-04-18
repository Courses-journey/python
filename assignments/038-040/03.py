first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")

first_name.strip().capitalize()
second_name.strip().capitalize()

# print(f"Hello {first_name.strip().capitalize()} {second_name.strip().capitalize():.1s}.")
print(f"Hello {first_name.strip().capitalize()} {second_name.strip().capitalize()[0]}.")