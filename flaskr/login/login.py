from flask import (Blueprint, request,current_app,
                   render_template,redirect, 
                   url_for, flash, Markup)
from flask_login import (login_user, 
                         login_required, 
                         current_user, 
                         logout_user, 
                         fresh_login_required)

from flaskr.forms.form import Login_form
from flaskr import login_manager
from flaskr.models.models import User_tbl
from werkzeug.security import check_password_hash

# import socket    
# import getpass


@login_manager.user_loader
def load_user(user_id):
    return User_tbl.query.get(int(user_id))



login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/")
def index():
    form_login = Login_form()
    return render_template('login.html', form_login=form_login)

#NEW AGE

@login_blueprint.route("/login", methods=['GET','POST'])
def login():
    form_login = Login_form()
    if current_user.is_authenticated:
        flash(Markup('''Ya te encuentras autenticado. 
                    <button type="button" class="btn-close"
                    data-bs-dismiss="alert" aria-label="Close"></button>
                    '''), "success")
        return redirect(url_for('main.main'))
    
    if form_login.validate_on_submit(): 
        # print(current_app.url_map)
        email_address = User_tbl.query.filter_by(email_address=form_login.email_address.data).first()
        print(email_address.email_address)
        print(email_address)
        print(email_address)
        # if True:
        #     flash(Markup('Cedula o Numero de carnet incorrecto.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "danger")
        if not email_address or check_password_hash(email_address.password,form_login.password.data)==False:
            # if not email or email.password and form.password.data==False:
            flash(Markup('''Email o contraseña incorrecto. 
                         <button type="button" class="btn-close"
                         data-bs-dismiss="alert" aria-label="Close"></button>
                            '''), "danger")
            return redirect(url_for('login.login'))
        else:
            # session.permanent = form.admin_or_user.data
            login_user(email_address, remember=True)
            flash(Markup(f'''Bienvenido {current_user.firstname}.  <button type="button" class="btn-close"
                         data-bs-dismiss="alert" aria-label="Close"></button>'''), "warning")
            return redirect(url_for('main.main'))
    return render_template('login.html',form_login=form_login)