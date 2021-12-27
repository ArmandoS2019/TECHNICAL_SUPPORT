import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    UPLOADED_PATH = os.path.join(basedir,'main.main')
    
    
    
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LcBfrUdAAAAANBJCjhns5jsss2x-G9AdK83e29H'
    RECAPTCHA_PRIVATE_KEY = '6LcBfrUdAAAAAH4mXEMRSXmIPC4e0C2B0DhXReS8'
    RECAPTCHA_OPTIONS = {'theme':'black'}

    SECRET_KEY = 'kaadfadfafafdafafadddddadfadadfaffddddddd'    
    # REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/medical_db"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/inspection_db"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@127.0.0.1/technical_supportdb'
    # SQLALCHEMY_POOL_SIZE = 30
    # SQLALCHEMY_MAX_OVERFLOW = 20
    # SQLALCHEMY_POOL_TIMEOUT = 300

    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  
 
    #********MY PATHS ROUTES ------------****************************
    
    PATH_PDF_PRESCRIPTION = "C:/Users/Pc/Documents/MEDICAL CONSULT/app/pdf_report/pdf_prescription_folder/"
    PATH_PDF_INDICATIONS = "C:/Users/Pc/Documents/MEDICAL CONSULT/app/pdf_report/pdf_indication_folder/"
                             
    
    IMAGE_UPLOADS = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/img_database'
    IMAGE_UPLOADS_PROFILE = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/profile'
    SAVED_GRAPH_PNG = "C:/Users/UserGP/Documents/PROC_INSP/app/saved_graph"
   
    ALLOWED_IMAGE_EXTENSIONS = ['JPG','JPEG', 'PNG', 'GIF']
    MAX_IMAGE_FILESIZE = 1024 * 1024
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
