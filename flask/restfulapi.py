from flask import Flask
from flask_restful import Api,Resource,reqparse
app=Flask(__name__)
api=Api(app)
books=[
    {"id":1,"title":"Python for begineers","author":"john doe"},
    {"id":2,"title":"Flask wed development","author":"jane smith"}
]
parser=reqparse.RequestParser()
parser.add_argument("title")
parser.add_argument("author")
class Books(Resource):
    def get(self):
        return books
    def post(self):
        args=parser.parse_args()
        book={
            "id":len(books) + 1,
            "title":args["title"],
            "author":args["author"]
        }
        books.append(book)
        return book,201
class Book(Resource):
    def get(self,book_id):
        for book in books:
            if book["id"]==book_id:
                return book
        return{"message":"Book not found"},404
    def put(self,book_id):
        args=parser.parse_args()
        for book in books:
            if book["id"]==book_id:
                book["title"]=args["title"]
                book["author"]=args["author"]
                return book
        return {"message":"Book not found"},404
    def delete(self,book_id):
        for book in books:
            if book["id"]==book_id:
                books.remove(book)
                return {"message":"Book deleted"}
        return {"message":"Book not found"},404
api.add_resource(Books,"/books")
api.add_resource(Book,'/books/<int:book_id>')
if __name__=="__main__":
    app.run(debug=True)



