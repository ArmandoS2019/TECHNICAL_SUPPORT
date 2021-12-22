from flask import (Blueprint,
                   render_template,request)

from flaskr.forms.form import Personal_info_form

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/main", methods=['GET','POST'])
def main():
    form = Personal_info_form()
    # if current_user.is_authenticated:
    #     return redirect(url_for('main'))
    if form.validate_on_submit():
        pass
        # email = Userdb.query.filter_by(email_address=form.email.data).first()
        
        # if not email or check_password_hash(email.password,form.password.data)==False:
        #     flash("Usuario o Contraseña incorrecto")          
        #     return redirect(url_for('login'))
        # else:
        #     # session.permanent = form.admin_or_user.data
        #     login_user(email, remember=True)
            
        #     return redirect(url_for('main'))
    else:
        return render_template('main.html') 