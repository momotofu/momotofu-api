from src.app import create_app
from src.utils.utils import get_cli_args
import os

args = get_cli_args()

app = create_app(os.getenv('FLASK_CONFIG') or 'dev')

if __name__ == '__main__':
    app.run()
