def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit():
        return False
    if not s.isalnum():
        return False
    if s[-1].isdigit():
        return False
    return True 

plate = input("vanity plate: ")
if is_valid(plate):
    print("Valid")
else:
    print("Invalid")    