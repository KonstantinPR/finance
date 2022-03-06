from flask import Flask, render_template, request, redirect
from flask_login import login_required, current_user, login_user, logout_user
from models import Company, UserModel, Post, Task, db, login
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'xyz'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)
login.login_view = 'login'


@app.before_first_request
def create_all():
    db.create_all()


@app.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    if not current_user.is_authenticated:
        return redirect('/company_register')
    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        if request.form['date'] == "": date = datetime.date.today()
        if request.form['user_name'] == "":
            user_name = current_user.user_name
        else:
            user_name = request.form['user_name']

        post = Post(amount=amount, description=description, date=date, user_name=user_name)
        db.session.add(post)
        db.session.commit()

    user_name = current_user.user_name
    posts = db.session.query(Post).all()
    print(posts)
    return render_template('blog.html', posts=posts, user_name=user_name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        company_name = request.form['company_name']
        user_name = request.form['user_name']
        password = request.form['password']

        company_id = Company.query.filter_by(company_name=company_name).first()
        print(company_id.id)

        if check_password_hash(company_id.password_hash, password):
            user = UserModel.query.filter_by(user_name=user_name, company_id=company_id.id).first()

        if user is not None:
            login_user(user)
            return redirect('/blog')

    return render_template('login.html')


@app.route('/company_register', methods=['POST', 'GET'])
def company_register():
    if request.method == 'POST':
        company_name = request.form['company_name']
        password = request.form['password']

        if Company.query.filter_by(company_name=company_name).first():
            return ('Email already Present')

        company = Company(company_name=company_name)
        company.set_password(password)
        db.session.add(company)
        db.session.commit()

        return redirect('/login')
    return render_template('company_register.html')


@app.route('/user_register', methods=['POST', 'GET'])
def user_register():
    if request.method == 'POST':

        company_name = request.form['company_name']
        password = request.form['password']
        password_hash = generate_password_hash(password)
        print(password_hash)
        user_name = request.form['user_name']

        company = Company.query.filter_by(company_name=company_name).first()
        if check_password_hash(company.password_hash, password):
            company_id = company.id
        else:
            print("No such company")

        if UserModel.query.filter_by(user_name=user_name).first():
            return ('User_name already Present')

        user = UserModel(user_name=user_name, company_id=company_id)
        db.session.add(user)
        db.session.commit()
        return redirect('/blog')

    return render_template('user_register.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/blog')


if __name__ == '__main__':
    app.run(host="localhost", port=8001, debug=True)
