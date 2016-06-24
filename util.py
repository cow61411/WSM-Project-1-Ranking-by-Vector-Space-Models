import sys

#http://www.scipy.org/
try:
	from numpy import dot
	from numpy.linalg import norm
except:
	print "Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?"
	sys.exit() 

def removeDuplicates(list):
	""" remove duplicates from a list """
	return set((item for item in list))


def cosine(vector1, vector2):
	""" related documents j and q are in the concept space by comparing the vectors :
		cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
	return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))

def jaccard(list1 , list2):
	#return jaccardscore(vector2 , vector1)
	set1 = set(list1)
	set2 = set(list2)
	un = set1.union(set2)
	inter = set1.intersection(set2)
	return float(len(inter)) / len(un)
