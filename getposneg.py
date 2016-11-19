def getposneg(searchword,str):

	import csv
	import numpy

	# def median(lst):
		# return numpy.median(numpy.array(lst))
	k = open("wordcsv_simp.csv","r")


	pos = []
	neg = []
	found = 0
	#interuption
	if searchword == "addictive":
		return 1 
	if searchword == "top":
		return 1
	if searchword == "dump":
		return -1

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
	"""elif sum(pos) - sum(neg) > 0:
		return 1
	elif sum(pos) - sum(neg) <0:
		return -1
	else:print searchword,
		return 0"""
	print searchword
	if numpy.mean(pos)>numpy.mean(neg):
		return max(numpy.mean(pos),numpy.mean(neg))
	elif numpy.mean(pos)<numpy.mean(neg):
		return (-1)*max(numpy.mean(pos),numpy.mean(neg))
	else:
		return 0 

	k.close()


print getposneg("top","JJ")