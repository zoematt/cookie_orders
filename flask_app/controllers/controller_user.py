from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_user import Cookie_orders


@app.route('/')
def cookie_order():

    return render_template('cookie_orders.html', cookies = Cookie_orders.get_all())

@app.route('/new_order')
def new_order():

    return render_template('new_order.html')

@app.route('/create', methods=['POST'])
def create_val():
    if not Cookie_orders.user_validate(request.form):
        return redirect('/new_order')
    Cookie_orders.create(request.form)
    return redirect("/")



@app.route('/process', methods=['POST'])
def create():
    Cookie_orders.create(request.form)
    return redirect('/')

@app.route('/getone_user/<int:user_id>')
def getone_user(user_id):
    data={"id": user_id}
    cookies = Cookie_orders.get_one(data)
    return render_template('show_user.html', cookies=cookies)

@app.route('/change', methods=['POST'])
def cookie_user():
    if not Cookie_orders.user_validate(request.form):
        return redirect(f'/edit/{request.form["id"]}/cookies')
    Cookie_orders.edit_cookie(request.form)
    return redirect('/')

@app.route('/edit/<int:id>/cookies')
def getone_cookie(id):
    data= {
        "id": id
    }
    results= Cookie_orders.get_one(data)
    return render_template('change_order.html', cookies=results)




