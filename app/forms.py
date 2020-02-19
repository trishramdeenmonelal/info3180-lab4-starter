#from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from app import app
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])