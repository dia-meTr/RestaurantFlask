import logging
from app import app

if __name__ == '__main__':
    open('app.log', 'a').close()
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(debug=True)
