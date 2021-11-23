import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
def my_deepcopy(xs):
    out = []
    for x in xs:
        if type(x) is list:
            out.append(my_deepcopy(x))
        else:
            out.append(x)
    return out
    
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
my_dc = my_deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)
print("--my deep copy--")
print(my_dc)

