email = input("Pls enter your email!: ").strip()

name = email[:email.index("@")]
service = email[email.index("@")+1:email.index(".")]
domain = email[email.index(".")+1:]

print(f"Your Name Is {name}")
print(f"Email Service Provider Is {service}")
print(f"Top Level Domain Is {domain}")