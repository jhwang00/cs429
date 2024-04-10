from flask import Flask, render_template, url_for, request, jsonify
import main as main

app = Flask(__name__)

file = main.call_pickle("inv_index.pickle") #inv index with tf-idf

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        #query_data = request.get_json()
        #query_text = query_data['query']

        task_content = request.form['query']
        
        print(task_content)
        #return "hello"
        return render_template('index.html')
        
    else:
        return 'Hello'
        #return render_template('index.html')
    #return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
