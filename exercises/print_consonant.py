def is_vowel(char):
    char = char.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False

def print_consonant(words):
    for char in words:
        if not is_vowel(char):
            print(char)

print_consonant("khadbab")
