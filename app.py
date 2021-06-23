from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['host.docker.internal:9200'])

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
        index="ecommercereviews",
        size=100,
        body={
            "query": {
                "query_string": {
                    "query": search_term

                }
            }
        }
    
        
    )

    return render_template('results.html', res=res , search_term=search_term )

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)
