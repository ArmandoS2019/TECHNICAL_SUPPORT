from flask import (Blueprint,
                   render_template,redirect, 
                   url_for, flash, Markup, request, send_from_directory)

from datetime import datetime

from flask_login import (login_user, 
                         login_required, 
                         current_user, 
                         logout_user, 
                         fresh_login_required)

from werkzeug.security import generate_password_hash
from flaskr.forms.form import Personal_info_form
from flaskr.models.models import User_tbl, Personalinfo_tbl
from flaskr.models.models import db

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/main", methods=['GET','POST'])
@login_required
def main():
    form_personal = Personal_info_form()

    form_personal.work_unit.data='HELLO WORK STATION'
    if request.method == 'POST':
       f = request.files.get('file')
       print(f)
       
    return render_template('dropzone.html')
   #                         form_personal=form_personal)
   #  if form_personal.validate_on_submit(): 
      
      # Personal_info = User_tbl(
      #    cedula_id=form_personal.cedula_id.data,
      #    num_carnet_id_pass=generate_password_hash(form_personal.num_carnet_id_pass.data),
      #    firstname=form_personal.firstname.data,
      #    lastname=form_personal.lastname.data,
      #    birthday=form_personal.birthday.data,
      #    rank=form_personal.rank.data,
      #    email_address=form_personal.email.data,
      #    celphone=form_personal.celphone2.data,
      #    direccion_workplace_police=form_personal.direccion_workplace_police.data,
      #    work_unit=form_personal.work_unit.data,
      #    nivel_admin='0',
      #    created_user_account=datetime.now())
      
      #    #    Personalinfo = Personalinfo_tbl(
      #    # my_user_id = current_user.id,
      #    # provincia_location = form_document(form_personal.provincia_location.data),
      #    # address_home_location = form_document.address_home_location.data,
      #    # status_of_home = form_document.status_of_home.data,
      #    # documents_pdf = form_document.documents_pdf.data,
      #    # images_home1 = form_document.images_home1.data,
      #    # images_home2 = form_document.images_home2.data,
      #    # created_personal_info = datetime.now())

      # db.session.add(Personal_info)
      # db.session.commit()
   #    flash(Markup('''Registro exitoso. 
   #                       <button type="button" class="btn-close"
   #                       data-bs-dismiss="alert" aria-label="Close"></button>
   #                          '''), "success")
   #    return redirect(url_for('main.main'))       
   #  return render_template('main.html',
   #                         form_personal=form_personal)