
# web_app/__init__.py

from flask import Flask

#from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    #app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)

    @app.route("/")
    def hello():
        print("VISITED THE HELLO PAGE")
        return "Hello World!"

    @app.route("/about")
    def about():
        print("VISITED THE ABOUT PAGE")
        return "About Me!"

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
