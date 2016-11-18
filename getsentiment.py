def getsentiment(line):
	import nltk
	from nltk.tokenize import sent_tokenize
	import getposneg
#text = "I bought a Samsung G12 camera. In the past week, I used the camera a lot. The photos from my Samy are not that great, and the battery life is short too"
#text = "It sucks,fucks,smell like shit"
	small_sentences = sent_tokenize(line)
	result = []
	flag = 0
	for small_sentence in small_sentences:
		text_tok = nltk.word_tokenize(small_sentence)
		Tag = nltk.pos_tag(text_tok)
	for index in range(len(Tag)):
		if "JJ" in Tag[index][1]:
			flag = 1 
			ans =  getposneg.getposneg(Tag[index][0],Tag[index][1]) 
			if Tag[index-1][0] =="not" or Tag[index-2][0] == "not" or  Tag[index-1][0] =="n't" or Tag[index-2][0] == "n't":
				ans = ans * (-1)
				result.append(ans)
			else:
				result.append(ans)
		else:
			pass	
	if flag == 0 or sum(result)==0 :
		for index in range(len(Tag)):
			if "VB" in Tag[index][1] :
				ans =  getposneg.getposneg(Tag[index][0],Tag[index][1]) 
				if Tag[index-1][0] =="not" or Tag[index-2][0] == "not" or Tag[index-1][0] =="n't" or Tag[index-2][0] == "n't":
					ans = ans * (-1)
					result.append(ans)
				else:
					result.append(ans)	  
			else:
				pass
	if flag == 0 or sum(result) == 0:
		for index in range(len(Tag)):
			if "NN" in Tag[index][1] :
				ans =  getposneg.getposneg(Tag[index][0],Tag[index][1]) 
				if Tag[index-1][0] =="not" or Tag[index-2][0] == "not" or Tag[index-1][0] =="n't" or Tag[index-2][0] == "n't":
					ans = ans * (-1)
					result.append(ans)
				else:
					result.append(ans)	  
			else:
				pass
	print result
	s = 0
	s_2 = 0
	if len(result) %2 ==0:
		for i in result:
			if i > 0:
				s = s+1
			if i < 0:
				s_2 =s_2+1
		if s  == s_2:
			return " 0"
		elif s < s_2:
			return " -"
		else:
			return " +"

	else: 
		for i in result:
			if i > 0:
				s = s +1
			if i < 0:
				s_2 = s_2+1
		if s_2 == s:
			if abs(sum(result))< 0.5:
				return " 0"
			elif sum(result) >= 0.5:
				return " +"
			else: 
				return " -"
		elif s_2 < s:
			if abs(sum(result))< 0.5:
				return " 0"
			else: 
				return " +"
		else:
			if abs(sum(result))< 0.5:
				return " 0"
			else:
				return " -"

	"""abs(sum(result))<0.5:
		return " 0"
	elif sum(result) <= -0.5:
		return " -"
	elif sum(result) >= 0.5:
		return " +""" 