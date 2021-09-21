from web import init_app
from config import Config

app = init_app()

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT)
