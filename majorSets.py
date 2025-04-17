
def Majors(file):
    members = set()
    with open(file) as infile:
        infile.readline()
        for line in infile:
            line = line.strip().split(",")
            fname = line[0]
            lname = line[1]
            members.add(fname + " " + lname)  
        infile.close()
        return members

csMems = (Majors("cs.txt"))
mathMems = (Majors("math.txt"))

doubleMajors = csMems.intersection(mathMems)
# print(doubleMajors)

stemMajors = csMems.union(mathMems) 
# print(stemMajors)

csMajors = csMems.difference(mathMems)
# print(csMajors)


def classMajors():
    classDict = {}
    students = set()
    infile = open("studentYear.txt", "r")
    for line in infile:
        line = line.strip()
        data = line.split("\t")
        year = data[0]
        if len(data) > 1:   
            name = data[1].split(",")
            fname = name[0]
            lname = name[1]
            student = fname + " " + lname
            students.add(student)
        if year not in classDict:
            classDict[year] = students
    infile.close()
    return classDict
classMajors()


def getSets():
    classDict = classMajors()
    for year, students in classDict.items():
        if year == "2":
            sophCS = students.intersection(csMems)
        if year == "1":
            freshNotStem = students.difference(csMems, mathMems)
        if year == "4":
            seniorDouble = students.intersection(csMems, mathMems)
    return sophCS, freshNotStem, seniorDouble

sophCS, freshNotStem, seniorDouble = getSets()

print("Sophomore CS Majors:")
for name in sophCS:
    print(name)

print("\nFreshman Non-STEM Majors:")
for name in freshNotStem:
    print(name)

print("\nSenior Double Majors:")
for name in seniorDouble:
    print(name)

        


        

