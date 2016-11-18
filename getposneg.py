def getposneg(searchword,str):

	import csv
	import numpy

	# def median(lst):
		# return numpy.median(numpy.array(lst))
	k = open("wordcsv_simp.csv","r")


	pos = []
	neg = []
	found = 0
	for row in csv.DictReader(k):
		if row['Word'] == searchword:
			#if row['Attr'] != 'n':
			if 'JJ' in str:
				if row['Attr'] == 'a':
					pos.append(float(row['Pos']))
					neg.append(float(row['Neg']))
			if 'NN' in str:
				if row['Attr'] == 'n':
					pos.append(float(row['Pos']))
					neg.append(float(row['Neg']))
			if 'VB' in str:
				if row['Attr'] == 'v':
					pos.append(float(row['Pos']))
					neg.append(float(row['Neg']))
		found = 1

	if found == 0:
		return 0
#		break
	# elif numpy.median(pos) > numpy.median(neg):
		# return 1
	# elif numpy.median(pos) < numpy.median(neg):
		# return -1
	# else:
		# return 0
	elif sum(pos) - sum(neg) > 0.05:
		return 1
	elif sum(pos) - sum(neg) <-0.05:
		return -1
	else:
		return 0
	k.close()


#print getposneg("food","NN")