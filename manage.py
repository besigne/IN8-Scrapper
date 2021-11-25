from flask import Flask
from services import routes
app = Flask(__name__)

app.add_url_rule('/', view_func=routes.index)

