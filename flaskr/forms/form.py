from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.validators import ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed 

def check_length_ced(form, field):
    if len(field.data) != 11:
        raise ValidationError('Cedula debe contener 11 numeros')

class Login_form(FlaskForm):
    cedula_id = StringField('',validators=[InputRequired('Campo requerido'),
                                                 check_length_ced])
    num_carnet_id_pass = PasswordField('',
                                       validators=[InputRequired('Campo requerido')])
    # recaptcha = RecaptchaField('',validators=[InputRequired('No soy un robot')])
    submit = SubmitField('Enviar')
    
class Personal_info_form(FlaskForm):
    cedula_id = StringField('Cedula', validators=[InputRequired('Cedula')])
    num_carnet_id_pass = StringField('Numero de carnet', validators=[InputRequired('Numero carnet')])
    
    firstname = StringField('Nombres', validators=[InputRequired('Nombre requerido')])
    lastname = StringField('Apellidos', validators=[InputRequired('Apellido requerido')])
    email = StringField('Email', validators=[DataRequired()])
    celphone1 = StringField('Telefono', validators=[DataRequired()])
    celphone2 = StringField('Celular', validators=[DataRequired()])

    rank_list = [("",""),('Coronel','Coronel'),('Teniente Coronel','Teniente Coronel'),
                     ('Mayor','Mayor'),('Capitan','Capitan'),('Primer Teniente','Primer Teniente'),
                     ('Segundo Teniente','Segundo Teniente'),('Sargento Mayor','Sargento Mayor'),('Sargento','Sargento'),('Cabo','Cabo'),
                     ('Raso','Raso'),('Asimilado','Asimilado'),('Igualado','Igualado')]
    rank = SelectField('Su Rango',choices=rank_list, validators=[InputRequired('Rango requerido')])


    department_list = [("",""),('Direccion Regional Central del Distrito',
                                'Direccion Regional Central del Distrito'),
                               ('Direccion Regional Este','Direccion Regional Este')]
    direccion_workplace_police = SelectField(u'Direccion, P.N., a la que perteneces',choices=department_list, validators=[InputRequired('Direcion requerida')])

    work_unit = StringField('Unidad, P.N., a la que pertenece', 
                                             validators=[DataRequired()])
    
    birthday = StringField('Fecha de nacimiento',validators=[DataRequired()])
    provincia_location = StringField('Provincia', validators=[InputRequired('Provincia')])
    address_home_location = StringField('Direccion Calle/#', validators=[InputRequired('Direccion del lugar')])
    
    status_of_home_list = [("",""),('Propia','Propia'),('Con titulo','Con titulo'),
                      ('Sin titulo','Sin titulo'),('Con acto de venta','Con acto de venta'),('Otro estatus','Otro estatus')]
    status_of_home = SelectField(u'Estatus de la casa o terreno',choices=status_of_home_list, validators=[InputRequired('Estatus requerido')])
   
    documents_pdf = FileField('')
    images_home1 = FileField('')
    images_home2 = FileField('') 
   


