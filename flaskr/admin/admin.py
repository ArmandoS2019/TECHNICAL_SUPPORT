from datetime import datetime
from flask import (Blueprint, request,
                   render_template,redirect, 
                   url_for, flash, Markup)
from flaskr.forms.form import Personal_info_form
from flaskr.models.models import User_tbl
from flaskr.models.models import db
# from flaskr import db

admin_blueprint = Blueprint('admin', __name__)

# newuser = User_tbl(cedula_id='22300998889')
# db.session.add(newuser)
# db.session.commit()

@admin_blueprint.route("/admin", methods=['GET','POST'  ])
def admin():
    form = Personal_info_form()
        # Personal_info = User_tbl(
        #     cedula_id=str(form.cedula_id.data).upper(),
        #     num_carnet_id_pass=form.med_center_icon.data,
        #     firstname=str(form.num_carnet_id_pass.data).upper(),
        #     lastname=form.lastname.data,
        #     birthday=form.birthday.data,
        #     rank=form.rank.data,
        #     email_address=form.email_address.data,
        #     celphone1=form.celphone1.data,
        #     celphone2=form.celphone2.data,
        #     direccion_workplace_police=form.direccion_workplace_police.data,
        #     work_unit=form.work_unit.data,
        #     nivel_admin='0',
        #     created_user_account=datetime.now())

        # db.session.add(Personal_info)
        # db.session.commit()
    return render_template('admin.html',form=form)