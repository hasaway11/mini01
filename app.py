from flask import Flask, render_template
from contact_view import contact_app
from finance_view import finance_app
from supply_view import supply_app
from todo_view import todo_app

app = Flask(__name__)

app.register_blueprint(todo_app)
app.register_blueprint(contact_app)
app.register_blueprint(finance_app)
app.register_blueprint(supply_app)

@app.route("/")
def index():
  return render_template("index.html")
app.run(debug=True)
