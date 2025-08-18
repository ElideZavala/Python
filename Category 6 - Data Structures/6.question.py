# Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}


print("****************************************")

print("first subset", first_set.issubset(second_set) )
print("second subset", second_set.issubset(first_set) )
print("****************************************")

print("first superset", first_set.issuperset(second_set) )
print("SECOND superset", second_set.issuperset(first_set) )
print("****************************************")

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()
print("****************************************")

print("🐛 ", first_set)
print("🐛 ", second_set)

