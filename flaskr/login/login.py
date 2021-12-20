from flask import (Blueprint, request,
                   render_template,redirect, 
                   url_for, flash, Markup)

from flaskr.forms.form import Login_form
# import socket    
# import getpass

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/")
def index():
    return render_template('login.html')

#NEW AGE

@login_blueprint.route("/")
@login_blueprint.route("/login", methods=['GET','POST'])
def login():
    form = Login_form()
    # if current_user.is_authenticated:
    #     return redirect(url_for('main'))
    if request.method == "POST" and form.validate_on_submit(): 
        #TODO: CHECK HASH PASSSWORD HAS PROBLEM ....................999999999999999999
        if True:
            flash(Markup('Usuario o Contraseña incorrecto.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "danger")
        # if not email or check_password_hash(email.password,form.password.data)==False:
        #     # if not email or email.password and form.password.data==False:
        #     flash(Markup('Usuario o Contraseña incorrecto.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "danger")
        #     return redirect(url_for('login'))
        else:
            # session.permanent = form.admin_or_user.data
            # login_user(email, remember=True)
            current_user = 'PRUEBA ARMANDO'
            flash(Markup(f'Bienvenido {current_user}.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "warning")
            return redirect(url_for('base'))
        
    return render_template('login.html',form=form)