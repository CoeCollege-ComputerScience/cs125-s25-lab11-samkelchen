# Activity 0

set1 = set("abcdijklm")
set2 = set("defghijnop")
set3 = set("qrstklmijnop")

# get {i,j}
set4 = set1.intersection(set2, set3)
print(set4)

# get {a,b,c}
set5 = set1.difference(set2, set3)
print(set5)

# get {i,j,n,o,p}
set6 = set2.intersection(set3)
print(set6)

# get {d}
set7 = set1.intersection(set2).difference(set3)
print(set7)

# get {k,l,m,n,o,p}
set8 = set1.union(set2).intersection(set3).difference(set("ij"))
print(set8)

# I genuinely sat on this for half an hour and I cannot figure out how to remove the i,j from the new set

