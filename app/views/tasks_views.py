from app import app
from flask import flash, render_template, request, redirect, send_file
from flask_login import login_required, current_user, login_user, logout_user
from app.models import Company, UserModel, Transaction, Task, Product, db
import datetime
from sqlalchemy import desc


# /// TASKS //////////////////

@app.route('/tasks', methods=['POST', 'GET'])
@login_required
def tasks():
    if not current_user.is_authenticated:
        return redirect('/company_register')
    company_id = current_user.company_id
    print(company_id)
    if request.method == 'POST':
        description = request.form['description']

        if request.form['date'] == "":
            date = datetime.date.today()
        else:
            date = request.form['date']
        if request.form['amount'] == "":
            amount = 1
        else:
            amount = request.form['amount']
        user_name = current_user.user_name

        task = Task(amount=amount, description=description, date=date, user_name=user_name, company_id=company_id)
        db.session.add(task)
        db.session.commit()

    user_name = current_user.user_name
    tasks = db.session.query(Task).filter_by(company_id=company_id).order_by(desc(Task.date), desc(Task.id)).all()
    return render_template('tasks.html', tasks=tasks, user_name=user_name)


@app.route('/task_edit/<int:id>', methods=['POST', 'GET'])
@login_required
def task_edit(id):
    if not current_user.is_authenticated:
        return redirect('/company_register')
    company_id = current_user.company_id

    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        date = request.form['date']
        user_name = request.form['user_name']
        task = Task.query.filter_by(id=id).one()
        task.amount = amount
        task.description = description
        task.date = date
        task.user_name = user_name
        db.session.add(task)
        db.session.commit()
        flash("Changing completed")


    else:
        task = Task.query.filter_by(id=id).first()
        amount = task.amount
        description = task.description
        date = task.date
        user_name = task.user_name
        return render_template('task.html',
                               amount=amount,
                               description=description,
                               date=date,
                               user_name=user_name,
                               id=id,
                               )

    # tasks = db.session.query(Task).filter_by(company_id=company_id).all()
    return redirect('/tasks')


@app.route('/task_copy', methods=['POST', 'GET'])
@login_required
def task_copy():
    if not current_user.is_authenticated:
        return redirect('/company_register')
    company_id = current_user.company_id

    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        date = datetime.date.today()
        user_name = request.form['user_name']
        task = Task(amount=amount, description=description, date=date, user_name=user_name, company_id=company_id)
        db.session.add(task)
        db.session.commit()

        flash("Changing completed")

    return redirect('/tasks')


@app.route('/task_search', methods=['POST', 'GET'])
@login_required
def task_search():
    if not current_user.is_authenticated:
        return redirect('/company_register')
    company_id = current_user.company_id

    if request.method == 'POST':
        search = request.form['search']
        tasks = db.session.query(Task).filter(Task.description.like('%' + search.lower() + '%')).order_by(
            desc(Task.date), desc(Task.id)).all()
        return render_template('tasks.html', tasks=tasks)

    return redirect('/tasks')


@app.route('/task_delete/<int:id>', methods=['POST', 'GET'])
@login_required
def task_delete(id):
    flash("Запись удалена")
    task = Task.query.filter_by(id=id).one()
    db.session.delete(task)
    db.session.commit()

    return redirect('/tasks')
