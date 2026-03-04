dictionary={"Bulgaria":"Sofia", "Serbia":"Belgrade","Hungary":"Budapest","Austria":"Vienna","Germany":"Berlin", "Luxembourg":"Luxembourg","France":"Paris"}
print(dictionary["Bulgaria"])
print(dictionary.values())
print(dictionary.items())
print(dictionary.keys())
dictionary["Belgium"]="Brussels"
print(dictionary)
del dictionary["Belgium"]
print(dictionary)