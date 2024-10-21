stored_pass = "password"
password = ""

pass_mismatch = stored_pass != password

while pass_mismatch:
    print("Enter your password: ")
    password = input()
    pass_mismatch = stored_pass != password


print("Access granted.")