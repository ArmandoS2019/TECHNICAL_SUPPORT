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
    cellphone = StringField('Celular', validators=[DataRequired()])
    birthday = StringField('Fecha de nacimiento', validators=[DataRequired()])
    
    rank_list = [("",""),('Coronel','Coronel'),('Teniente Coronel','Teniente Coronel'),
                     ('Mayor','Mayor'),('Capitan','Capitan'),('Primer Teniente','Primer Teniente'),
                     ('Segundo Teniente','Segundo Teniente'),('Sargento Mayor','Sargento Mayor'),('Sargento','Sargento'),('Cabo','Cabo'),
                     ('Raso','Raso'),('Asimilado','Asimilado'),('Igualado','Igualado')]
    rank = SelectField('Su Rango',choices=rank_list, validators=[InputRequired('Rango requerido')])


    department_list = [("",""),('Inspectoria General, P.N.',
                                'Direccion Regional Central del Distrito'),
                               ('Direccion Regional Este','Direccion Regional Este')]
    direccion_workplace_police = SelectField(u'Direccion, P.N., a la que perteneces',choices=department_list, validators=[InputRequired('Direcion requerida')])

    work_unit_list = [("",""),('Estadistica y Monitoreo Inspectoria General, P.N.')]
    work_unit = SelectField(u'Unidad, P.N., a la que perteneces',choices=department_list, validators=[InputRequired('Direcion requerida')])
   
class Technicalsupport_form(FlaskForm):
   
    firstname_lastname = StringField('Nombre de quien solicito el soporte', 
                                     validators=[InputRequired('Nombre de quien solicito el soporte')])

    direction_support_list = [("",""),('Direccion Regional Central del Distrito',
                                'Direccion Regional Central del Distrito'),
                               ('Direccion Regional Este','Direccion Regional Este')]
    direction_support = SelectField(u'Direccion, P.N., donde realizó el soporte',
                                choices=direction_support_list, 
                                validators=[InputRequired('Direcion requerida')])

    work_unit_support = StringField('Unidad, P.N., donde realizó el soporte', 
                                validators=[DataRequired()])
    
    type_of_support_list = [("",""),('Seguridad de usuario','Seguridad de usuario'),
                               ('Entrenamiento de usuario','Entrenamiento de usuario'),
                               ('Instalacion de software o hardware','Instalacion de software o hardware'),
                               ('Configuracion de software','Configuracion de software')]
    type_of_support = SelectField(u'Tipo de soporte',
                                choices=type_of_support_list, 
                                validators=[InputRequired('Campo requerido')])
    
    comment_support = StringField('Comentarios del soporte',validators=[DataRequired('Campo requerido')])

    image_support1 = FileField('')
    image_support2 = FileField('') 
   


