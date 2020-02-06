from flask import Flask, render_template

app = Flask (__name__)

post_list = ["Eine Reise nach Japan", "Walfischen in Alaska", "Mal was ganz anderes"]

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/posts")
def posts():
    return render_template ("posts.html", posts=post_list)



if __name__=="__main__":
            app.run()