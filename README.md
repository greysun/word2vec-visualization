# word2vec-visualization
Word vectors visualization

Authors: Phi Van Thuy and Taishi Ikeda

- Run server: python -m SimpleHTTPServer 8888

- Main files and folders:
	+ backend<br>
		+ HiraganaTimes_English<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in English; skip-gram (slower, better for infrequent words) vs CBOW (fast)
		+ HiraganaTimes_Japanese<br>
			implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in Japanese; skip-gram (slower, better for infrequent words) vs CBOW (fast)
		+ word2vec_gensim_create_json_tree.py<br>
			script for creating flare-format data (require 'gensim' to excute)
	+ frontend<br>
		+ data<br>
			contain all data for searching word and vizualize them: "out.json" is the database, and "tree.json" is the flare-format data for vizualizing words on the web page
		+ js<br>
			contain D3.js library (visualization javascript library)
		+ word2vec_tree.html<br>
			the main web page


