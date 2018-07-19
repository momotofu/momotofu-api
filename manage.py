from src.app import create_app
# from src.config import DevelopmentConfig as dev_config, Config as config
import sys
import os


def main(argv):
    if '--debug' or '-d' in argv:
        # run debug mode for development
        app = create_app()
    else:
        # run app for production
        app = create_app()

    PORT = os.environ['PORT'] if 'PORT' in os.environ.keys() else 5000

    app.run(host = '0.0.0.0', port=5000)

if __name__ == '__main__':
    main(sys.argv[1:])
