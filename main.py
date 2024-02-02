

from flask import Flask,render_template
import json
import requests


#creates a flask app
app=Flask(__name__)

#defines a route to execute the homepage function
@app.route("/")
def homepage():
    meme_pic,subreddit,author=fetch_memes()
    return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit,author=author)


#method to fetch the meme from the subreddit using the already defined api in the github
def fetch_memes():
   
   #name of the subreddit to fetch memes from
    sr="/ProgrammerHumor"
    #url of the API
    url="https://meme-api.com/gimme"+sr
    #converts(deserialize) the document into python object and stores it into response variable
    response=json.loads(requests.request("GET",url).text)
    #getting the image of the meme
    meme_large=response["preview"][-2]
    #getting the name of the subreddit
    subreddit=response["subreddit"]
    #getting the author of the meme
    author=response["author"]
    return meme_large,subreddit,author



if __name__=="__main__":
    app.run(debug=True)

