from flask import Flask , render_template
import os


app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

path = "./static/" #path of your files

@app.route('/')
def index():
	b = list(os.walk(path))[0][2]
	return render_template("index.html" , b=b)

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=port ,debug = True , use_reloader=False)