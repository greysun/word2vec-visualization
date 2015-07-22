# word2vec-visualization
Word vectors visualization

- Run server: python -m SimpleHTTPServer 8888

- Main files and folders:
	+ frontend/js<br>
		D3.js library folder (visualization javascript library)
	+ frontend/data/tree.json<br>
		currently it is a sample dataset obtained from word2vec
	+ frontend/tree.html<br>
		web page display
	+ backend/word2vec_gensim_create_json_tree.py<br>
		script for creating flare-format data (require 'gensim' to excute)
	+ backend/HiraganaTimes_English<br>
		implementation of the continuous bag-of-words and skip-gram architectures for computing vector representations of words in English; skip-gram (slower, better for infrequent words) vs CBOW (fast)
