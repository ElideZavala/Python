# Removal all the characters other than integers from a string

str = 'I am 25 years and 10 months old'


result = "".join([item for item in str if item.isdigit()])
print("🐛 result", result)

