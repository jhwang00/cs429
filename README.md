## Abstract:
This project aims to develop a web document (Wikipedia) retrieval system using Python with libraries such as Scrapy, Scikit-Learn, Flask, nltk, beautiful soup etc. The primary objectives include implementing a Scrapy-based crawler for web document retrieval, a Scikit-Learn-based indexer for constructing an inverted index, and a Flask-based processor for handling free text queries. Next steps involve optimizing system performance and exploring optional features like concurrent crawling, distributed crawling, vector embedding representation, and semantic search capabilities.

## Overview:
The solution entails the development of a web document retrieval system leveraging existing libraries and frameworks. Relevant literature "Introduction to Information Retrieval" is used to design and implement these components. The proposed system comprises a Scrapy-based crawler for content extraction, a Scikit-Learn-based indexer for indexing, and a Flask-based processor for query handling.

## Design:
The system capabilities include web document crawling using seed URL and restricting max pages and max depth and save as html file, indexing to save inverted index with tf-idf score and url of the site in pickle file, and query processing to handle user's free text query and retrive site. 

## Architecture:
#### Web crawling (spiders/mycrawler.py)
Initialize start url in start_urls and can customize max page and max depth on custom_settings. After running it, it downloads and saves as html file with link as file name. 
#### Indexing (main.py)
It recursively reads every html file in directory. 
Then does preprocessing steps (lowercasing, stemming then stopword removal).
And creates inverted index with tf-idf score and saves it as pickle file. 
#### Query processing (app.py, req.py)
You can set how many results to return by controlling top_k variable in app.py. The query_return function in main.py is used to process query using cosine similarity. After running app.py, can type query in the terminal and retrieve top k sites.

## Operation:
After running app.py, run req.py. Then you can type query to retreive results.
To operate the system, users can run web crawling sessions by providing seed URLs/domains and specifying maximum pages and depth. 
The Scrapy-based crawler handles content retrieval and stores web documents in HTML format. The indexer component constructs an inverted index with TF-IDF score and saves it in pickle file. 
Users can submit free text queries to the Flask-based processor, which returns top-K ranked results based on cosine similarity scores.

## Conclusion:
According to test cases, the project is quite successful. Web crawling part did not retrieve exact amount of pages but got close to it. Indexing part successfully saved inverted index with tf-idf score and url in pickle format. Query processing returned resonable sites. However, it is expected that more accurate measurements will be needed.

## Data Sources:
https://www.wikipedia.org/ \
https://en.wikipedia.org/wiki/List_of_common_misconceptions

## Test Cases:
#### Web crawling
1. max page: \
input: 5, 10, 50, 100 \
output: 3, 8, 52, 98 \
Not precise but close to max page

#### Indexing
2. test.py test1() \
number of url:       3, 8, 52, 98 \
returned url number: 3, 8, 52, 98 \
start url correctly downloaded 

3. test.py test2() \
inverted index with tf-idf score saved correctly 

#### Query processing
4. Search: viral disease fever \
Response from server: \
[ \
    "https://en.wikipedia.org/wiki/Yellow_fever", \
    "https://en.wikipedia.org/wiki/Bourbon_virus", \
    "https://en.wikipedia.org/wiki/Emerging_infectious_disease", \
    "https://en.wikipedia.org/wiki/Duplodnaviria", \
    "https://en.wikipedia.org/wiki/Susceptible_individual", \
    "https://en.wikipedia.org/wiki/Malaria", \
    "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Jersey", \
    "https://en.wikipedia.org/wiki/Caucasian_Iberia", \
    "https://en.wikipedia.org/wiki/List_of_common_misconceptions", \
    "https://en.wikipedia.org/wiki/Osroene" \
] \
The result looks reasonable

5. Search: west central Europe Matterhorn \
Response from server: \
[ \
    "https://en.wikipedia.org/wiki/Marshall_Plan", \
    "https://en.wikipedia.org/wiki/Switzerland", \
    "https://en.wikipedia.org/wiki/Leadership_of_Communist_Kyrgyzstan", \
    "https://en.wikipedia.org/wiki/Battle_of_South_Guangxi", \
    "https://en.wikipedia.org/wiki/List_of_wards_of_Zimbabwe", \        
    "https://en.wikipedia.org/wiki/Nazi_Germany", \
    "https://en.wikipedia.org/wiki/Census_in_Transnistria", \
    "https://en.wikipedia.org/wiki/Cilicia", \
    "https://en.wikipedia.org/wiki/Federated_state", \
    "https://en.wikipedia.org/wiki/Cappadocia" \
] \
Expected Switzerland to show first but in second place.

## Source code
#### Listings
1. Crawler: \
spiders/mycrawler.py 
2. Indexer: \
main.py 
3. Processor: \
app.py \
req.py 
4. Test: \
test.py 

#### Documentation
Scrape file by typing "scrapy crawl my crawler" in terminal. \
Run main.py to save inverted index and url. \
Run flasks by app.py and run req.py for query input. 

#### Dependencies
beautifulSoup 4.12.3 \
flask 3.0.2 \
nltk 3.8.1 \
python 3.11.9 \
scipy 1.12.0 \
scrapy 2.11.1

## Bibliography:
Johansson, Christer. "How do I read all html-files in a directory recursively?," Stack Overflow, January 23, 2018, https://stackoverflow.com/questions/48401550/how-do-i-read-all-html-files-in-a-directory-recursively \
Manning, Christopher D., Raghavan, P., and Schütze, Hinrich.
"Introduction to Information Retrieval". online. Cambridge: Cambridge University Press, 2008.https://nlp.stanford.edu/IR-book/. \
NeuralNine, "Coding Web Crawler in Python with Scrapy," YouTube Video, November 23, 2022, https://www.youtube.com/watch?v=m_3gjHGxIJc&ab_channel=NeuralNine.
