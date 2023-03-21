def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join([char for char in word if char not in vowels])

def main():
    name = input("Input: ")
    print(f"hello, {shorten(name)}")

if __name__ == "__main__":
    main()