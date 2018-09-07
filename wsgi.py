from src.app import create_app
import os

if os.getenv('FLASK_CONFIG'):
    app = create_app(os.getenv('FLASK_CONFIG'))
else:
    from src.utils.utils import get_cli_args
    args = get_cli_args()
    if 'dev' in args.keys():
        app = create_app('dev')

if __name__ == '__main__':
    app.run()
