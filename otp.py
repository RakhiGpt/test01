import random

def generate_otp():
    return str(random.randint(100000, 999999))

# Example usage
if __name__ == "_main_":
    otp = generate_otp()
    print(otp)