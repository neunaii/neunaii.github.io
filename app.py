from flask import Flask, request, render_template

app = Flask(__name__)


class User:
    def __init__(self, username):
        self.username = username

    def get_user_name(self):
        return self.username


def username_star_filter(value):
    return '⭐' + value + '⭐'


app.add_template_filter(username_star_filter)


@app.route('/')
@app.route('/<username>/')
def index(username=None):
    user0 = User('ak')
    user1 = {'username': 'ml'}
    return render_template("index.html", username=username, user1=user1, user0=user0)


@app.route('/for_loop/')
def for_loop():
    users = [{'name': 'ad', 'age': 12}, {'name': 'adwawd', 'age': 1212}]
    return render_template("for_loop.html", users=users)


# error when accessing /mad/
@app.route('/mad')
def ad(aw):
    return aw


@app.route('/book')
def book_page():
    page = request.args.get("page", default=0, type=int)
    return f"{page}"


if __name__ == '__main__':
    app.run(debug=True)
