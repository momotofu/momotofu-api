from src.app import create_app
from src.utils.utils import get_cli_args
import os

args = get_cli_args()

if 'dev' in args.keys():
    app = create_app('dev')
else:
    app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run()
