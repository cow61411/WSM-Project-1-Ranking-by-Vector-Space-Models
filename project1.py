import run1
import run2
import run3
import run4
import run5

#query = ["drill wood sharp"]
querylist = []

judge = True
query = raw_input("Please input your query:\n")
querylist.append(query)
print "\n"
print "Your query terms is " + query + "\n"
while judge:
	select = raw_input("To compute Term Frequency (TF) Weighting + Cosine Similarity : Press 1\nTo compute Term Frequency (TF) Weighting + Jaccard Similarity : Press 2\nTo compute TF-IDF Weighting + Cosine Similarity : Press 3\nTo compute Tf-IDF Weighting + Jaccard Similarity : Press 4\nTo compute Feedback Queries + TF-IDF Weighting + Jaccard Similarity : Press 5\nTo change query terms : Press 6 \nTo exit this program : Press 7\n")
	if select == '1':
		print "\n"
		run1.run1(querylist)
		print "\n"
	elif select == '2':
		print "\n"
		run2.run2(querylist)
		print "\n"
	elif select == '3':
		print "\n"
		run3.run3(querylist)
		print "\n"
	elif select == '4':
		print "\n"
		run4.run4(querylist)
		print "\n"
	elif select == '5':
		print "\n"
		run5.run5(querylist)
		print "\n"
	elif select == '6':
		print "\n"
		querylist = []
		query = raw_input("Please input your query:\n")
		querylist.append(query)
		print "Your query terms is " + query + "\n"
	elif select == '7':
		judge = False

