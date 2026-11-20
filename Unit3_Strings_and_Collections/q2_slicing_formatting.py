"""Unit 3 - Q2: String Slicing and String Formatting"""

full_name = input("Enter full name: ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()

# Slicing the name
space = full_name.index(" ")
first_name = full_name[:space]
last_name = full_name[space + 1:]
reversed_name = full_name[::-1]

# Slicing the email
at = email.index("@")
username = email[:at]
domain = email[at + 1:]

# Last four digits of mobile
last_four = mobile[-4:]

print("\nFirst name    :", first_name)
print("Last name     :", last_name)
print("Reversed name :", reversed_name)
print("Username      :", username)
print("Domain        :", domain)
print("Last 4 digits :", last_four)

print("\n--- Formatting techniques ---")
print(f"f-string      : Name={full_name}, Email={email}, Mobile=XXXXXX{last_four}")
print("format()      : Name={}, Email={}, Mobile=XXXXXX{}".format(full_name, email, last_four))
print("%% operator    : Name=%s, Email=%s, Mobile=XXXXXX%s" % (full_name, email, last_four))
print(f"Aligned       : |{first_name:<12}|{last_name:^12}|{last_four:>8}|")

print("\n--- Positive and negative indexing ---")
print(f"full_name[0]  = '{full_name[0]}'   (first character)")
print(f"full_name[-1] = '{full_name[-1]}'   (last character)")
print(f"full_name[2]  = '{full_name[2]}'")
print(f"full_name[-3] = '{full_name[-3]}'")
print(f"full_name[1:4]   = '{full_name[1:4]}'")
print(f"full_name[-4:-1] = '{full_name[-4:-1]}'")
