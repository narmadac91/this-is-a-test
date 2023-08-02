
raw = open(r"C:\Users\Abhijit\Desktop\f.txt", "r")
unfilteredList = raw.readlines()

conU = 0
conG = 0
genreList = []
#while conU < len(unfilteredList):
for x in unfilteredList:
    print(x)
    x = x[0:len(x) - 1]
    if x not in genreList:
        genreList.append(x)
print(genreList)


