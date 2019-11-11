"""Entry point for our twitoff flask app"""

from .app import create_app

#APP is a global variable
APP = create_app()

#run this in termianl with set FLASK_APP=TWITOFF:APP flask run
