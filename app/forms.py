from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class SubmitData(Form):
    name = TextField('name', validators = [Required()])
    email = TextField('email', validators = [Required()])

