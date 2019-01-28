from app import abc

@abc.route('/')
@abc.route('/abc')
def home():
    return "Hello World!"

@abc.route('/index')
def index():
    return "Index Page!"
