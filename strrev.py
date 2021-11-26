def rev(str):
    words = str.split()
    words.reverse()
    return " ".join(words)

def countVowels(str):
    count = 0
    vow = ['a','e','i','o','u']
    for c in str:
        if c in vow:
            count += 1

    return count
class Str:
    revstr =""
    vowelct = 0
    def __init__(self,str):
        self.revstr = rev(str)
        self.vowelct = countVowels(self.revstr)

strings = []
for i in range(0,3):
    st = input('enter a string')
    str1 = Str(st)
    strings.append(str1)

strings.sort(key = lambda x:x.vowelct, reverse=True)

for str in strings:
    print(str.revstr)

