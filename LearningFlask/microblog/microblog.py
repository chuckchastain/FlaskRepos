#import os
from AppDir import app, db    # Imports the code from AppDir/__init__.py
from AppDir.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
#if __name__ == '__main__':
#    HOST = os.environ.get('SERVER_HOST', 'localhost')

 #   try:
  #      PORT = int(os.environ.get('SERVER_PORT', '5555'))
  #  except ValueError:
  #      PORT = 5555

  #  app.run(HOST, PORT)