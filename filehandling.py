text = open("sample.txt","r")
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1



desc = sorted(d.items(), key=lambda x: x[1], reverse=True)
count = 0
for i in desc:
    count += 1
    print(i[0], i[1])
    if(count == 10):
        break

keys = list(d.keys())
for key in keys:
    print(key,":",len(key))

sum=0
for key in keys:
    sum += len(key)

print("avg length is {}".format(sum/len(keys)))