import string

from nltk.corpus import stopwords

class Glossary():
    '''
    This object acts as the database containing the list of phrases.
    The phrase list is constructed during initialization and then is able to
    be searched.
    '''
    def __init__(self):
        file_url = 'phrases.txt'
        words_list = [words[:-1] for words in open(file_url).readlines()]
        self.strip_punctuation = str.maketrans('', '', string.punctuation)
        #make a list of sets containing the defining words of each condition
        self.phrase_list = []
        for words in words_list:
            words = words.translate(self.strip_punctuation)
            words = (set([word for word in words.split(' ')
                          if word not in stopwords.words('english')]), words)
            if words[0]:
                self.phrase_list.append(words)

    def search(self, searchwords):
        '''
        Will search within phraselist to find any phrases which are a subset of
        the search words
        '''
        results = []
        searchwords = searchwords.translate(self.strip_punctuation)
        needles = set([word for word in searchwords.split(' ')
                       if word not in stopwords.words('english')])
        for phrase in self.phrase_list:
            if phrase[0] <= needles:
                print(phrase[0], needles)
                results.append(phrase[1])
        return results
