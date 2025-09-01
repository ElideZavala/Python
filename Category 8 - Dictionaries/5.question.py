# Create a new dictionary by extracting the following keys from a below dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}


# new_dictionary = {
#     sampleDict.get("name"),
#     sampleDict.get("salary")
# }
keys = ["name", "salary"]

new_dictionary = {
    k: sampleDict[k] for k in keys
}
print('new_dictionary: ', new_dictionary)