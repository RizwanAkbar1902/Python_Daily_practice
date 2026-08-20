print("=" * 50)
print("        PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = input("Enter a password: ").strip()

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
        

if (
    8 <= len(password) <= 20
    and has_upper
    and has_lower
    and has_digit
):
    print("\n✅ Strong Password")
else:
    print("\n❌ Weak Password")
    print("Password must:")
    print("- Be between 8 and 20 characters")
    print("- Contain at least one uppercase letter")
    print("- Contain at least one lowercase letter")
    print("- Contain at least one digit")