import pickle, nltk, os, jsonify
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocessLC(text): # Lowercase, tokenize
    corp = text.lower().split()
    return corp

def preprocessStem(text): # Stemming
    stemmer = nltk.stem.LancasterStemmer()
    text = text
    stemmedWord = []
    for w in text:
        stemmedWord.append(stemmer.stem(w))
    return stemmedWord

def preprocessStop(text): # Stopwords
    stop_words = set(stopwords.words('english'))
    removal_list = list(stop_words) + ['lt','rt']
    filtered_text = [w for w in text if not w.lower() in removal_list]
    return filtered_text

def cleanText(text): # Preprocessing
    clean_text = preprocessLC(text)
    clean_text = preprocessStop(preprocessStem(clean_text))
    return clean_text
    
def create_inv(data): # Create inverted index with tf-idf score
    # Data given as list of 'url' and 'data' dictionary
    # [{'url', 'data'}]
    data = [d['data'] for d in data]

    # Get tf-idf score of a vocabulary for each document
    inverted_index = {}
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data)
    scores = X.toarray()
    voca = vectorizer.vocabulary_
    sorted_voca = {k: v for k, v in sorted(voca.items(), key=lambda item: item[1])}

    # Save tf-dif score in inverted index
    for doc_id, doc_vector in enumerate(scores):
        for term_id, score in enumerate(doc_vector):
            if score != 0:
                term = [key for key, value in sorted_voca.items() if value == term_id][0]
                if term not in inverted_index:
                    inverted_index[term] = []
                inverted_index[term].append((doc_id, score))
    return inverted_index, scores
# Chatgpt

def write_pickle(data, file_name): # Write pickle file
    with open(file_name, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def call_pickle(file_name): # Read pickle file
    with open(file_name, 'rb') as handle:
        b = pickle.load(handle)
    return b

def query_return(query, top_k):
    clean_query = cleanText(query) # Preprocess query

    if clean_query == []: # If not valid, not in voca, or typed nothing
        response = {'Not a valid query try other you typed': query}
        return response
    
    inv_ind = call_pickle("inv_index.pickle") # Get inverted index
    get_url = call_pickle("save_url.pickle") # Get url of sites

    voca_query = [ele for ele in clean_query if ele in inv_ind] # Query vocabulary

    # Get inverted index which has at least 1 query word
    inv_ind_query = {ele: inv_ind[ele] for ele in voca_query if ele in inv_ind}

    # Getting score
    tf_query = {}
    for ele in voca_query:
        tf_query[ele] = clean_query.count(ele)
    mul_tf_inv = {term: [(doc_id, tf_query[term] * idf) for doc_id, idf in postings] for term, postings in inv_ind_query.items()}
    # Get score and save score of each document in doc_scores
    doc_scores = {}
    for _, postings in mul_tf_inv.items():
        for doc_id, score in postings:
            if doc_id in doc_scores:
                doc_scores[doc_id] += score
            else:
                doc_scores[doc_id] = score
    
    # Sort by score and get top k result
    sorted_doc_scores = [k for k, _ in sorted(doc_scores.items(), key=lambda item: item[1], reverse=True)]
    top_k_res = sorted_doc_scores[:top_k]
    result = [get_url[i] for i in top_k_res if 0<=i<len(get_url)]
    return result

def main():
    data = [] # [[{url, text}]] 

    # Read all html file in directory
    directory ='/Users/user/Desktop/cs 429/hw/project/project_scrapy/'
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            fname = os.path.join(directory,filename)
            with open(fname, 'r') as f:
                soup = BeautifulSoup(f.read(),'html.parser')
                text = soup.get_text()
                data.append({'url':'https://en.wikipedia.org/wiki/'+filename[:-5], 'data':text})

    # Preprocess text
    for i in range(len(data)):
        data[i]['data'] = ' '.join(cleanText(data[i]['data']))
    
    # Make inverted index and save as pickle file
    inv_index, _ = create_inv(data)
    file_name = 'inv_index.pickle'
    write_pickle(inv_index, file_name)

    # Save url and save as pickle file
    file_name3 = 'save_url.pickle'
    data_url = []
    for i in range(len(data)):
        data_url.append(data[i]['url'])
    write_pickle(data_url,file_name3)
#https://stackoverflow.com/questions/48401550/how-do-i-read-all-html-files-in-a-directory-recursively

#main()