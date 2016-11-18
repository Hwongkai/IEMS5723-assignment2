import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
import getsentiment
import os

test = []
file = open("test.txt")
i =0
while 1:
	line = file.readline().replace("\n","")
	if not line:
		break
	else:
		test.append(line)
file.close()

result=[]
label = []
for item in test:
	a = getsentiment.getsentiment(item)
	label.append(a)
	item = "".join([item,a])
	result.append(item)
	print item

print label 
correct_label = [' +',' +',' +',' +',' +',' 0',' 0',' 0',' 0',' 0',' -',' -',' -',' -',' -']
count = 0
for index in range(0,len(correct_label)):
	if correct_label[index] == label[index]:
		count = count + 1
print "accuracy on review comments:", float(count)/15



file = open("result.txt","w")
for index in range(0,len(result)):
		result_line = result[index]
		file.write(result_line)
		file.write('\n')
file.close()
   


