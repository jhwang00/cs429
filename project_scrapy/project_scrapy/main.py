import pickle, nltk, os
#import json
#import sklearn
#import nltk
#nltk.download('stopwords')
#from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocessLC(text): #lowercase, tokenize
    corp = text.lower().split()
    return corp

def preprocessStem(text): #stemming
    stemmer = nltk.stem.LancasterStemmer()
    text = text
    stemmedWord = []
    for w in text:
        stemmedWord.append(stemmer.stem(w))
    return stemmedWord

def preprocessStop(text): #stopwords
    stop_words = set(stopwords.words('english'))
    removal_list = list(stop_words) + ['lt','rt']
    filtered_text = [w for w in text if not w.lower() in removal_list]
    return filtered_text

def cleanText(text):
    clean_text = preprocessLC(text)
    clean_text = preprocessStop(preprocessStem(clean_text))
    return clean_text
    
def create_inv(data):
    data = [d['data'] for d in data]

    inverted_index = {}
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data)

    scores = X.toarray()
    voca = vectorizer.vocabulary_
    sorted_voca = {k: v for k, v in sorted(voca.items(), key=lambda item: item[1])}

    # Iterate over each document (row) in X
    for doc_id, doc_vector in enumerate(scores):
        # Iterate over each term (column) in the document vector
        for term_id, score in enumerate(doc_vector):
            # If the term has a non-zero score in the document
            if score != 0:
                # Get the term from the Y mapping
                term = [key for key, value in sorted_voca.items() if value == term_id][0]
                # If the term is not already in the inverted index, add it
                if term not in inverted_index:
                    inverted_index[term] = []
                # Append the document ID and score tuple to the inverted index entry for the term
                inverted_index[term].append((doc_id, score))
    return inverted_index, scores
#chatgpt

def write_pickle(data, file_name):
    with open(file_name, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def call_pickle(file_name):
    with open(file_name, 'rb') as handle:
        b = pickle.load(handle)
    return b


def main():
    data = [] # [[{url, text}]] 
    directory ='/Users/user/Desktop/cs 429/hw/project/project_scrapy/'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            fname = os.path.join(directory,filename)
            with open(fname, 'r') as f:
                soup = BeautifulSoup(f.read(),'html.parser')
                text = soup.get_text()
                data.append({'url':'https://en.wikipedia.org/wiki/'+filename[:-5], 'data':text})

    for i in range(len(data)):
        data[i]['data'] = ' '.join(cleanText(data[i]['data']))
    
    inv_index, scores = create_inv(data)
    file_name = 'inv_index.pickle'
    write_pickle(inv_index, file_name)

    cos_similarity = cosine_similarity(scores)
    file_name2 = 'cosine_similarity.pickle'
    write_pickle(cos_similarity, file_name2)
    #pik = call_pickle(file_name)
    #print(pik)

#main()

#https://stackoverflow.com/questions/48401550/how-do-i-read-all-html-files-in-a-directory-recursively