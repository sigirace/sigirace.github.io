import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')

class Model():
    def __init__(self, df):
        self.df = df
        self.corpus = []
        self.model = None
        self.stemmer = PorterStemmer()
        self.stopwords_set  = set(stopwords.words('english'))

    def preprocess(self):

        for i in range(len(self.df)):
            text = self.df['text'].iloc[i].lower()
            text = text.translate(str.maketrans('','',string.punctuation)).split()
            text = [self.stemmer.stem(word) for word in text if word not in self.stopwords_set]
            text = ' '.join(text)
            self.corpus.append(text)
            self.vectorizer = CountVectorizer()
        
        self.df['label_num'] = self.df.apply(lambda x: 1 if x['label'] == 'spam' else 0, axis=1)
    
    def train(self):
        self.preprocess()

        X = self.vectorizer.fit_transform(self.corpus).toarray()
        y = self.df.label_num

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        mnb = MultinomialNB()

        mnb.fit(X_train, y_train)
        self.model = mnb
        score = mnb.score(X_test, y_test)
        print("모델 성능: ", score)
    
    def chekc(self, mail_text):
        email_text = mail_text.lower().translate(str.maketrans('','',string.punctuation)).split()
        email_text = [self.stemmer.stem(word) for word in email_text if word not in self.stopwords_set]
        email_text = ' '.join(email_text)

        email_corpus = [email_text]

        X_email = self.vectorizer.transform(email_corpus)

        result = self.model.predict(X_email)
        
        if result[0] == 1:
            print("스팸입니다.")
            return True
        else:
            print("스팸이 아닙니다.")
            return False
