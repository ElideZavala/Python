# Count all lower case, upper case, digits, and special symbols from a given string
str = "h@#el26a^&5le"

def find_digits_chars_symbols(str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str:
        if char.islower() or char.isupper():
            char_count += 1
        elif char.isnumeric():
            digit_count += 1        
        else:
            symbol_count += 1
    
    print(f"Tenemos {char_count} minusculas/mayusculas, {digit_count} numeros y {symbol_count} symbolos especiales")
        
find_digits_chars_symbols(str)


