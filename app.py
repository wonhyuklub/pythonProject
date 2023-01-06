from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.shm4bls.mongodb.net/cluster0?retryWrites=true&w=majority',tlsCAFile = ca)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
   name_receive = request.form['name_give']
   comment_receive = request.form['comment_give']


   doc = {
      'name': name_receive,
      'comment': comment_receive
   }

   db.homework.insert_one(doc)


   return jsonify({'msg': ' 응원완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():


   return jsonify({'msg': '응원완료'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

