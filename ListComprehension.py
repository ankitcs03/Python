
Line = "the quick brown fox jumps over the lazy dog"
Words =  Line.split()
LengthList = [ ]
for word in Words:
	if (word != "the" ):
		LengthList.append(len(word))
print(LengthList)

NewLengthList = [len(x) for x in Line.split() if x != "the"]
print(NewLengthList)