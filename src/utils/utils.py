import random, string, json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model import Base


def get_cli_args():
    """
    Returns a dictionary of arguments passed to through the CLI.
    """
    import re
    import sys

    args = {}

    for arg in sys.argv[1:]:
      var = re.search('\-\-(.*)\=', arg)
      var = variable.group(1)
      value = re.search('\=(.*)', arg)
      value = value.group(1)
      args[variable] = value
    return args


def allowed_file(filename, config):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']


def get_rand_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits +
        string.ascii_lowercase) for x in range(32))


def get_session(db_path):
    """
    returns an sqlalchemy session.
    """

    engine = create_engine(db_path)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    return session

def get_credentials_for(subject, provider):
    """
    Returns a dictionary with credentials for the provider.
    """

    from flask import current_app as app

    return json.loads(open(app.config['CREDENTIALS_PATH'],
        'r').read())[subject][provider]
