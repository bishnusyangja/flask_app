 
import sys
import os
from os.path import dirname
from urls import get_flask_app

root_path = dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root_path))

app = get_flask_app()


if __name__ == '__main__':
   app.run(debug=True)
