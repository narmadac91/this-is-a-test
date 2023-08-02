raw = open(r"C:\Users\russianvodka\Desktop\f.txt", "r")
unfilteredList = raw.readlines()

def findSemiCol(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def semiColRem (string):
    genreList = []
    semList = findSemiCol(string,';')
    if not semList:
        return string[0:len(string)-1]
    it = 0
    lastSem = 0
    while it <= len(semList):
        if it < len(semList):
            end = semList[it]
            if it is 0:
                lastSem = -2
        else:
            end = len(string) - 1
        genreList.append(string[lastSem+2:end])
        lastSem = end

        it += 1
    return genreList

albumCon = 0
genreList = []

while albumCon < len(unfilteredList):
    albumGenres = semiColRem(unfilteredList[albumCon])
    if isinstance(albumGenres, list) is False:
        if albumGenres not in genreList:
            genreList.append(albumGenres)
    else:
        genreCon = 0
        while genreCon < len(albumGenres):
            if albumGenres[genreCon] not in genreList:
                genreList.append(albumGenres[genreCon])
            genreCon += 1
    albumCon += 1

for sortGenre in sorted(genreList):
        print(sortGenre)