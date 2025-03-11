from flask import Blueprint , render_template, redirect, request

supply_app = Blueprint('supply_app', __name__, url_prefix='/supply')

supplies = []
sno = 1

@supply_app.route("/list")
def index():
    return render_template("supply/list.html", supplies=supplies)

@supply_app.route("/add", methods=['post'])
def write():
    global sno
    name = request.form.get('name')
    new_supply = {'sno':sno, 'name':name, 'count':1}
    supplies.append(new_supply)
    sno+=1
    return redirect("/supply/list")

@supply_app.route("/inc", methods=['post'])
def inc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            s['count']=s['count']+1
    return redirect("/supply/list")

@supply_app.route("/dec", methods=['post'])
def desc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno and s['count']>1:
            s['count']=s['count']-1
    return redirect("/supply/list")


@supply_app.route("/delete", methods=['post'])
def delete() :
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            supplies.remove(s)
    return redirect("/supply/list")

