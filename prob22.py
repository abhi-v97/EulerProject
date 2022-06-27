"""

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def compute():
    with open('names.txt') as names:
        content = names.read()
        #print(content)
        
        #put names in a list, remove excess characters
        list = content.replace("\"", "").split(",")
        #print(list)

    x = sum((i + 1) * (ord(y) - ord('A') + 1)
    for (i, name) in enumerate(sorted(list))
    for y in name)

    return str(x)

if __name__ == "__main__":
    print(compute())