import string
from nltk.corpus import stopwords

class TextPreProcessor():
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    
    """
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
    
    def process(self, mess):
        nopunc = [char for char in mess if char not in string.punctuation]
        
        nopunc = ''.join(nopunc)
        
        return [word for word in nopunc.split() if word.lower() in stopwords.words('english')]