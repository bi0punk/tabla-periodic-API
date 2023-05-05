from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

class Database:
   def __init__(self, app):
      self.app = app
   
   def get_db(self):
      try:
         db = getattr(self.app, '_database', None)
         if db is None:
            db = self.app._database = sqlite3.connect(DATABASE)
         return db
      except:
         print("Database not found, Please create the .db file")
      
   def close_db(self):
      try: 
         db = getattr(self.app, '_database', None)
         if db is not None:
            db.close()
      except:
         print("Ah ocurrido un error en el proceso")

class Post:
   def __init__(self, title, content):
      self.title = title
      self.content = content
   
   def save(self):
      db = Database(app).get_db()
      cursor = db.cursor()
      cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (self.title, self.content))
      db.commit()

   @staticmethod
   def get_latest_post():
      db = Database(app).get_db()
      cursor = db.cursor()
      cursor.execute('SELECT * FROM posts ORDER BY id DESC LIMIT 1')
      post = cursor.fetchone()
      return post

@app.route('/posts', methods=['POST'])
def create_post():
   data = request.get_json()
   title = data['title']
   content = data['content']
   post = Post(title, content)
   post.save()
   latest_post = Post.get_latest_post()
   return jsonify({'post': latest_post})

if __name__ == '__main__':
   app.config['DEBUG'] = True
   app.config['SECRET_KEY'] = 'supersecretkey'
   db = Database(app)
   app.teardown_appcontext(db.close_db)
   app.run()
