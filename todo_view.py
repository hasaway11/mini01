from flask import Blueprint , render_template, redirect, request
import datetime as dt

todo_app = Blueprint('todo_app', __name__, url_prefix='/todo')

todos = []
tno = 1

@todo_app.route("/list")
def index():
    return render_template("todo/list.html", todos=todos)

@todo_app.route("/write", methods=['post'])
def write():
    global tno
    title = request.form.get('title')
    date = dt.datetime.now().strftime('%Y-%m-%d')
    new_todo = {'tno':tno, 'title':title, 'date':date, 'finish':False}
    todos.append(new_todo)
    tno+=1
    return redirect("/todo/list")

@todo_app.route("/finish", methods=['post'])
def finish():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todo['finish']=True
    return redirect("/todo/list")


@todo_app.route("/delete", methods=['post'])
def delete() :
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todos.remove(todo)
    return redirect("/todo/list")
