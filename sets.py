setslist=[1,1,1,1,5454,23,204,5454, "Peter"]
sets=set(setslist)
print(sets)
# print(sets[2]) - cannot access aynthing in the set
if 23 in sets:
    print("23 is available")
else:
    print("23 is not available")
Set=set([])
Set.add(5)
Set.remove(5)
Set.add(454)
print(Set)
Set.discard(8)
a = {4, 566, "Nikolaus", "James", "Jaques"}
b = {4, 566, 666, 777, "Nikolaus"}
print(a | b) # | is a union
print(a & b) # & is used for intersection
print(a - b) # all unique elements of first set - in our case, it's a
print(a ^ b) # symetric difference is union minus intersection