text_user = input('Введите пароль: ')
answer = len(text_user)
score = 0

def is_very_long(text_user):
    return len(text_user) > 12
    
def has_digit(letter):
    return any(symbol.isdigit() for symbol in letter)

def has_lower_letters(letter):
    return any(symbol.islower() for symbol in letter)

def has_upper_letters(letter):
    return any(symbol.isupper() for symbol in letter)

def has_symbols(letter):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in letter)

functions = [is_very_long, has_digit, has_lower_letters, has_upper_letters, has_symbols]

for function in functions:
    score += 2 if function(text_user) else 0

print("Рейтинг пароля:", score)