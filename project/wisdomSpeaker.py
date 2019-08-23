from config import get_env
from app import create_app

app=create_app()

if __name__ == '__main__':
	app.run()