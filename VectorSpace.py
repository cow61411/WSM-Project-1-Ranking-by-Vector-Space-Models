from pprint import pprint
from Parser import Parser
import util
from math import log

class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers.
    A document is represented as a vector. Each dimension of the vector corresponds to a
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """

    #Collection of document term vectors
    documentVectors = []

    #Mapping of vector index to keyword
    vectorKeywordIndex=[]

    #Tidies terms
    parser=None


    def __init__(self, documents=[]):
        self.documentVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)

    def build(self,documents):
        """ Create the vector space for the passed document strings """
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.documentVectors = [self.makeVector(document) for document in documents]

        #print self.vectorKeywordIndex
        #print self.documentVectors


    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """

        #Mapped documents into a single word string
        vocabularyString = " ".join(documentList)

        vocabularyList = self.parser.tokenise(vocabularyString)
        #Remove common words which have no search value
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = util.removeDuplicates(vocabularyList)

        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex  #(keyword:position)


    def getVectorKeywordIndexSeprated(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """
        vectorIndex = []
        for document in documentList:

            vocabularyList = self.parser.tokenise(document)
            #Remove common words which have no search value
            vocabularyList = self.parser.removeStopWords(vocabularyList)
            uniqueVocabularyList = util.removeDuplicates(vocabularyList)
            vectorIndex.append(uniqueVocabularyList)

        return vectorIndex  #set[keywords]

    def makeVector(self, wordString):
        """ @pre: unique(vectorIndex) """

        #Initialise vector with 0's
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
        return vector


    def buildQueryVector(self, termList):
        """ convert query string into a term vector """
        query = self.makeVector(" ".join(termList))
        return query


    def related(self,documentId):
        """ find documents that are related to the document indexed by passed Id within the document Vectors"""
        ratings = [util.cosine(self.documentVectors[documentId], documentVector) for documentVector in self.documentVectors]
        #ratings.sort(reverse=True)
        return ratings


    def search(self,searchList):
        """ search for documents that match based on a list of terms """
        queryVector = self.buildQueryVector(searchList)

        ratings = [util.cosine(queryVector, documentVector) for documentVector in self.documentVectors]
        #ratings.sort(reverse=True)
        return ratings

    def searchtfjab(self,searchList , documentList):
        queryVector = self.getVectorKeywordIndex(searchList)
        self.documentVectors = self.getVectorKeywordIndexSeprated(documentList)
        ratings = [util.jaccard(queryVector , documentVector) for documentVector in self.documentVectors]
        return ratings

    def searchtfjabPlusRelevent(self,searchList , releventdocstr , documentList):
        queryVector = self.getVectorKeywordIndex(searchList)
        relevenceVector = self.getVectorKeywordIndex(releventdocstr)
        self.documentVectors = self.getVectorKeywordIndexSeprated(documentList)
        ratings = [util.jaccard(queryVector , documentVector) for documentVector in self.documentVectors]
        ratingrel = [util.jaccard(relevenceVector , documentVector) for documentVector in self.documentVectors]
        for i in range(len(ratings)):
            ratings[i] += (ratingrel[i] * 0.5)
        return ratings

    def searchtfidfcosine(self,searchList):
        queryVector = self.buildQueryVector(searchList)
        queryVector = self.computeidf(queryVector)
        tempVectors = [self.computeidf(documentVector) for documentVector in self.documentVectors]
        ratings = [util.cosine(queryVector , documentVector) for documentVector in tempVectors]
        return ratings


    def computeidf(self , vector):
        result = []
        for i in range(len(vector)):
            if vector[i] != 0:
                count = 0
                for documentVector in self.documentVectors:
                    if documentVector[i] != 0:
                        count += 1
                temp = vector[i] * (1 + log(2048 / count))
                result.append(temp)
            else:
                result.append(0)
        return result


#if __name__ == '__main__':
    #test data
    #documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]

    #vectorSpace= VectorSpace(documents)
    #pprint(vectorSpace.related(1))
    #pprint(vectorSpace.search(["cat"]))

###################################################
