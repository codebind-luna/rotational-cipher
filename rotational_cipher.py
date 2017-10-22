import string

def rotate(text, key):
    array_of_alphabets = list(string.ascii_lowercase)
    cipher = ''
    
    for char in text:
        lowercase_of_char = char.lower()
        if lowercase_of_char in array_of_alphabets:
            pos = (array_of_alphabets.index(lowercase_of_char) + key) % 26
            
            if char.islower():
                cipher += array_of_alphabets[pos]
            else:
                cipher += array_of_alphabets[pos].upper()
        else:
            cipher += char
    
    return cipher
