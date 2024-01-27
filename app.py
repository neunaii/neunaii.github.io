from flask import Flask

app = Flask(__name__)


@app.route('/pop/<int:i>')
def hello_world(i):
    return 'ad %d' % i


# error when accessing /mad/
@app.route('/mad')
def ad(aw):
    return aw


if __name__ == '__main__':
    app.run(debug=True)
