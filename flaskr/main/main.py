from flask import (Blueprint,
                   render_template,redirect, 
                   url_for, flash, Markup, request, send_from_directory)

from datetime import datetime
from flask_login import (login_user, 
                         login_required, 
                         current_user, 
                         logout_user, 
                         fresh_login_required)

from flaskr.forms.form import Technicalsupport_form
from flaskr.models.models import Technicalsupport_tbl
from flaskr.models.models import db

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/main", methods=['GET','POST'])
@login_required
def main():
    technical_form = Technicalsupport_form()

    if technical_form.validate_on_submit(): 
       
      Support_info = Technicalsupport_tbl(
         firstname_lastname=technical_form.firstname_lastname.data,
         direction_support=technical_form.direction_support.data,
         work_unit_support=technical_form.work_unit_support.data,
         phone_support=technical_form.phone_support.data,
         type_of_support=technical_form.type_of_support.data,
         comment_support=technical_form.comment_support.data,
         image_support1=technical_form.image_support1.data,
         image_support2=technical_form.image_support2.data,
         created_technical_support=datetime.now())

      db.session.add(Support_info)
      db.session.commit()
      flash(Markup('''Registro exitoso. 
                         <button type="button" class="btn-close"
                         data-bs-dismiss="alert" aria-label="Close"></button>
                            '''), "success")
      return redirect(url_for('main.main'))      
    return render_template('main.html',
                           technical_form=technical_form)