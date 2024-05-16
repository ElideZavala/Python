# -----------------------------------------------------
# ------------**## Scope ##**--------------------------

# Local Variables
# Global Variables

# ! ************ Example 14 ************
def comment(date):
    content = "amazing landscape"


comment("May 23, 2135")

#  ! ************ Example 15 ************

content = "just do it"


def post(date):
    content = "i am on a trip"


post("Jan 1, 1970")

# print(content)

# ! ************ Example 16 ************
dog_name = "Hachi"


def animal_names():
    global dog_name
    dog_name = "Georgie"


animal_names()

print(dog_name)
