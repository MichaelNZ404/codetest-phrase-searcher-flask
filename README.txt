Specification:
See spec.txt

Installation:
1) create virtual env and pip install from requirements.txt
2) open your python interpreter, import nltk and download the nltk stopwords by running: nltk.download('stopwords')
3) set the FLASK_APP env variable and run the server with: 'export FLASK_APP=service.py; flask run --port=8080'
4) visit 'http://127.0.0.1:8080' in your browser. Provide the get parameter text to search the phrases eg: 'http://127.0.0.1:8080/?text=mood%20disorder%20depressive'
5) tests can be run from the root directory with 'python -m pytest'

Implementation decisions:

Phrases are stored in memory as a list of sets. This allows us to filter out duplicate terms and insure all key words of the phrase are hit by the search term.
This does not perform particularly well at scale, instead of being able to reduce our search space with each token, we instead need to check each set in the list individually.

Perhaps a better data structure would be to build a token: sets hash map where each token in the phrase points to the entire phrase. so for phrases of length 3, we do 3 hash table lookups, then check each set for other matching tokens, rather than looking through an entire list.
In an industry setting, a indexed database table would do a lot of this heavy lifting for us.

I used NLTK stop word filtering which prevents searches being rejected due to slightly different phrasing. If I was to chose how to present this information, I would have returned results that matched all n tokens, followed by results that matched n-1, down to only 1 keyword matching.
This allows us to get results like 'back of throat' from the wording 'rear of throat' where back and rear are ignored. This example could also be improved with a synonym list.

It's worth noting that NLTK really slows down how quickly the model loads. If the plan was to continue to store the phrases in files, it would be worth preprocessing these to remove stop words for an efficiency bonus. 
