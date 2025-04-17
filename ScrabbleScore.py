def makeScrabbleDict():
    d = {}
    d[1] = "AEIOULNSTR"
    d[2] = "DG"
    d[3] = "BCMP"
    d[4] = "FHVWY"
    d[5] = "K"
    d[8] = "JX"
    d[10] = "QZ"

    scoreDict = {}
    for k,v in d.items():
        for letter in v:
            scoreDict[letter] = k
    return scoreDict

def scoreWord(word):
    word = word.upper()
    sd = makeScrabbleDict()
    score = 0
    for letter in word:
        score += sd[letter]

    return score


# Note - add your code here if you completed the "Competency" option on the quiz
def topNWords(length, numWords):
    d = {}
    
    infile = open("ScrabbleWords.txt", "r")  
    for word in infile:
        word = word.strip()
        score = scoreWord(word)
        if len(word) == length:
            if score not in d:
                d[score] = []
            d[score].append(word)
    infile.close()
    
    sortLst = []
    for score, words in d.items():
        sortLst.append((score, words))
    sortLst.sort()
    sortLst.reverse()

    count = 0
    for score, words in sortLst:
        for word in words:
            if count < numWords:
                print(f"{score}: {word}")
                count += 1
            else:
                break

topNWords(3, 3)
