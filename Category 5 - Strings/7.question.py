# Split a given string on hyphens into several substrings and display each substring

str = "Katty-is-a-data-scientist"

paragraphs = str.split("-")
print("🐛 text", paragraphs)

for paragraph in paragraphs:
    print(paragraph, end=" " ) 
