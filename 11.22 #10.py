def replace(s, old, new):
    return s.replace(old, new)

# Helper test function
def test(actual):
    if actual:
        print("Test passed")
    else:
        print("Test failed")

# Tests
test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

test(replace(s, "om", "am") == 
     "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") == 
     "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
