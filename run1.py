from VectorSpace import VectorSpace
import os
#from pprint import pprint


    #test data
#documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
def run1(querylist):
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

	vectorSpace= VectorSpace(documents)
    #pprint(vectorSpace.related(1))
	result = vectorSpace.search(querylist)
	order = sorted(result,reverse = True)
	#print type(result)
	#print order
	print "Term Frequency Weighting + Cosine Similarity:\n"
	print "DocID    Score"
	for i in range(5):
		print str(namelist[result.index(order[i])]) + "   %.6f" % order[i]

