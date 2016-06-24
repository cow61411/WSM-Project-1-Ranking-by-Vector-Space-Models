from VectorSpace import VectorSpace
import os
#from pprint import pprint


    #test data
#documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
def run5(querylist):
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
	result = vectorSpace.searchtfjab(querylist , documents)
	order = sorted(result,reverse = True)
	relID = namelist[result.index(order[0])]
	f = open(docdir + relID + ".product" , 'r')
	line = f.read()
	relstr = []
	relstr.append(line)
	result = vectorSpace.searchtfjabPlusRelevent(querylist , relstr , documents)
	order = sorted(result,reverse = True)
	print "Feedback Queries + TF-IDF Weighting + Jaccard Similarity:\n"
	#print type(result)
	#print order
	print "DocID    Score"
	for i in range(5):
		print str(namelist[result.index(order[i])]) + "   %.6f" % order[i]

