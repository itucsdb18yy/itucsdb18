from flask import Flask, render_template
from datetime import datetime
import views
from database import Database
from movie import Movie

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)
    app.add_url_rule("/movies/<int:movie_key>", view_func=views.movie_page)

    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five", year=1972))
    db.add_movie(Movie("The Shining"))
    app.config["db"] = db

    return app

app = create_app()
port = app.config.get()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)