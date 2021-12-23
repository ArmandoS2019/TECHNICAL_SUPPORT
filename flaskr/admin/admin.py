from datetime import datetime
from flask import (Blueprint, request,
                   render_template,redirect, 
                   url_for, flash, Markup)

from flaskr.forms.form import Personal_info_form
from flaskr.models.models import User_tbl
from flaskr.models.models import db

admin_blueprint = Blueprint('admin', __name__)


# Personal_info = User_tbl(
#             cedula_id='form_info.cedula_id.data',
#             num_carnet_id_pass='form_info.num_carnet_id_pass.data',
#             firstname='form_info.firstname.data',
#             lastname='form_info.lastname.data',
#             birthday='form_info.birthday.data',
#             rank='form_info.rank.data',
#             email_address='form_info.email.data',
#             celphone='form_info.celphone2.data',
#             direccion_workplace_police='form_info.direccion_workplace_police.data',
#             work_unit='form_info.work_unit.data',
#             nivel_admin='0',
#             created_user_account='datetime.now()')

# db.session.add(Personal_info)
# db.session.commit()



@admin_blueprint.route("/admin", methods=['GET','POST'])
def admin():
    form_personal = Personal_info_form()

    if form_personal.validate_on_submit(): 
       flash(Markup(f'Paciente XXX ya se encuentra registrado.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
       return redirect(url_for('login.login'))
    
    return render_template('admin.html',form_personal=form_personal)