from datetime import datetime
from flask import (Blueprint, request,
                   render_template,redirect, 
                   url_for, flash, Markup)

from flask_login import (login_user, 
                         login_required, 
                         current_user, 
                         logout_user, 
                         fresh_login_required)

from werkzeug.security import generate_password_hash
from flaskr.forms.form import Personal_info_form
from flaskr.models.models import User_tbl
from flaskr.models.models import db

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route("/admin", methods=['GET','POST'])
def admin():
    form_personal = Personal_info_form()

    if form_personal.validate_on_submit(): 
       
      Personal_info = User_tbl(
         cedula_id=form_personal.cedula_id.data,
         num_carnet_id_pass=generate_password_hash(form_personal.num_carnet_id_pass.data),
         firstname=form_personal.firstname.data,
         lastname=form_personal.lastname.data,
         birthday=form_personal.birthday.data,
         rank=form_personal.rank.data,
         email_address=form_personal.email.data,
         celphone=form_personal.celphone2.data,
         direccion_workplace_police=form_personal.direccion_workplace_police.data,
         work_unit=form_personal.work_unit.data,
         nivel_admin='0',
         created_user_account=datetime.now())

      db.session.add(Personal_info)
      db.session.commit()
      flash(Markup('''Registro exitoso. 
                         <button type="button" class="btn-close"
                         data-bs-dismiss="alert" aria-label="Close"></button>
                            '''), "success")
      return redirect(url_for('admin.admin'))
    
    return render_template('admin.html',form_personal=form_personal)
  
  
@admin_blueprint.route("/logout", methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    # session.clear()
    return redirect(url_for('login.login'))
