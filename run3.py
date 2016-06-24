from VectorSpace import VectorSpace
import os

def run3(querylist):
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
	result = vectorSpace.searchtfidfcosine(querylist)
	#print result
	order = sorted(result,reverse = True)
	print "TF-IDF Weighting + Cosine Similarity:\n"
	#print type(result)
	#print order
	print "DocID    Score"
	for i in range(5):
		print str(namelist[result.index(order[i])]) + "   %.6f" % order[i]

