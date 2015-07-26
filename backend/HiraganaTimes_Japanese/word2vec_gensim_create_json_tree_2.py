#Phi Van Thuy
#http://radimrehurek.com/gensim/models/word2vec.html
#http://radimrehurek.com/2013/09/deep-learning-with-word2vec-and-gensim/
#import gensim
from gensim.models import word2vec

#Pre-trained model
#model_path = "/cl/work/thuy-ph/word2vec/GoogleNews-vectors-negative300.bin"
model_path = "/Users/cl-lab/Dropbox/Master program at NAIST/Project Practice/HiraganaTimes_English/model_skipgram.bin"

print "Loading model..."
model = word2vec.Word2Vec.load_word2vec_format(model_path, binary=True)  # C binary format
print "Loading model: Done"

print "Writing..."

#print model.vocab.items()[i]

top = 10

f = open('tree.json','w')

f.write("{\n\n")

root = "university"

f.write("\"name\": \"" + root + "\",\n")
f.write("\"children\": [\n")

nearest_words = model.most_similar(positive=[root], negative=[], topn=top)
#number_nearest_words = len(nearest_words)

for i in range(0, top):
	f.write("{")

	f.write("\"name\": \"" + nearest_words[i][0].encode("utf-8") + "\",\n") #Before loop 1

	############ Loop 1
	f.write("\"children\": [\n")

	nearest_words_1 = model.most_similar(positive=[nearest_words[i][0]], negative=[], topn=top)

	for i1 in range(0, top):
		f.write("{")

		f.write("\"name\": \"" + nearest_words_1[i1][0].encode("utf-8") + "\",\n") #Before loop 2
		############ Loop 2
		f.write("\"children\": [\n")

		nearest_words_2 = model.most_similar(positive=[nearest_words_1[i1][0]], negative=[], topn=top)

		for i2 in range(0, top):
			f.write("{")

			f.write("\"name\": \"" + nearest_words_2[i2][0].encode("utf-8") + "\",\n") #Before loop 3
			############ Loop 3
			f.write("\"children\": [\n")

			nearest_words_3 = model.most_similar(positive=[nearest_words_2[i2][0]], negative=[], topn=top)

			for i3 in range(0, top):
				f.write("{")

				f.write("\"name\": \"" + nearest_words_3[i3][0].encode("utf-8") + "\",\n") #Before loop 4
				############ Loop 4
				f.write("\"children\": [\n")

				nearest_words_4 = model.most_similar(positive=[nearest_words_3[i3][0]], negative=[], topn=top)

				for i4 in range(0, top):
					f.write("{")

					f.write("\"name\": \"" + nearest_words_4[i4][0].encode("utf-8") + "\"") #Before loop ?
					# If this is the final layer --> modify (delete ",\n")

					if i4 != top - 1:
						f.write("},\n")
					else:
						f.write("}\n")
				
				f.write("]\n")
				############ End Loop 4

				if i3 != top - 1:
					f.write("},\n")
				else:
					f.write("}\n")
			
			f.write("]\n")
			############ End Loop 3

			if i2 != top - 1:
				f.write("},\n")
			else:
				f.write("}\n")
		
		f.write("]\n")
		############ End Loop 2	

		if i1 != top - 1:
			f.write("},\n")
		else:
			f.write("}\n")
	
	f.write("]\n")
	############ End Loop 1



	if i != top - 1:
		f.write("},\n")
	else:
		f.write("}\n")

f.write("]\n")



f.write("\n}\n")
f.close()

print "Finish!"
