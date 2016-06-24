from VectorSpace import VectorSpace
#from VectorSpace import searchtfjab
import os
#from pprint import pprint


    #test data
#documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
def run2(querylist):
	documents = []
	namelist = []
	docdir = "./documents/"
	for root , dirs , files in os.walk(docdir):
		for filename in files:
			f = open(docdir + filename , 'r')
			filename = filename.split(".")
			namelist.append(filename[0])
			line = f.read()
			documents.append(line)
			f.close()
	
	vectorSpace= VectorSpace()
    #pprint(vectorSpace.related(1))
	result = vectorSpace.searchtfjab(querylist , documents)
	#print result
	order = sorted(result,reverse = True)
	#print type(result)
	#print order
	print "Term Frequent Weighting + Jaccard Similarity:\n"
	print "DocID    Score"
	for i in range(5):
		#print str(namelist[result.index(order[i])]) + "   " + str(order[i])
		print str(namelist[result.index(order[i])]) + "   %.6f" % order[i]

