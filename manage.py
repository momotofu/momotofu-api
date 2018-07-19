from src.app import create_app
import sys
import os


def main(argv):
    if '--debug' or '-d' in argv:
        # run debug mode for development
        from src.config import DevelopmentConfig as dev_config
        app = create_app(config=dev_config)
    else:
        # run app for production
        from src.config import Config as config
        app = create_app(config=config)

    PORT = os.environ['PORT'] if 'PORT' in os.environ.keys() else 5000

    app.run(host = '0.0.0.0', port=5000)

if __name__ == '__main__':
    main(sys.argv[1:])
