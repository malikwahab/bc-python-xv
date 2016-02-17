def is_vowel(char):
    char = char.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False

def print_vowels(words):
    for char in words:
        if is_vowel(char):
            print(char)

print_vowels("maleEq")
