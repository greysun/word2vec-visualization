# word2vec-visualization
Word Vectors Visualization in Tree Form

Authors: Phi Van Thuy and Taishi Ikeda

- Two types of distances: Cosine distance and Euclidean distance
- Totally 8 different models for the English and the Japanese data
- Run simple HTTP server: python -m SimpleHTTPServer 8888

- Main files and folders:
	+ backend<br>
		+ HiraganaTimes_English<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in English; skip-gram (slower, better for infrequent words) vs CBOW (fast)
		+ HiraganaTimes_Japanese<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in Japanese; skip-gram (slower, better for infrequent words) vs CBOW (fast)
	+ frontend<br>
		+ data<br>
			contain all data for searching word and vizualize them: "data_cosine.json" and "data_euclidean.json" are the databases. The flare-format data is created from the database when running the web page.
		+ js<br>
			contain D3.js library (visualization javascript library)
		+ word2vec_tree_final.html<br>
			the main web page

- Convert the word2vec models to the JSON files
To visualize your own data, 
