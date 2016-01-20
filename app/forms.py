from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])	# check that the field is not empty
    remember_me = BooleanField('remember_me', default=False)

# Forms are used when we carry data. (submit button do not carry any data
