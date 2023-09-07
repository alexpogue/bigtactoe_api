import bigtactoe
from flask import Flask

app = bigtactoe.create_app('config.py')

if __name__ == '__main__':
    app.run()
