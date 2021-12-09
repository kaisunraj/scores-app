from waitress import serve
import scores_flask

if __name__ == "__main__":
    serve(scores_flask.app)
