from flask import Blueprint , render_template, redirect, request
import datetime as dt

contact_app = Blueprint('contact_app', __name__, url_prefix='/contact')

contacts = []
cno = 1

@contact_app.route("/list")
def index():
    return render_template("contact/list.html", contacts=contacts)

@contact_app.route("/write", methods=['post'])
def write():
    global cno
    name = request.form.get('name')
    tel = request.form.get('tel')
    address = request.form.get('address')
    new_contact = {'cno':cno, 'name':name, 'tel':tel, 'address':address}
    contacts.append(new_contact)
    cno+=1
    return redirect("/contact/list")

@contact_app.route("/delete", methods=['post'])
def delete() :
    cno = int(request.form.get('cno'))
    for contact in contacts:
        if contact['cno']==cno:
            contacts.remove(contact)
    return redirect("/contact/list")