from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, SubmitField

class TextoVoz(FlaskForm):

    text = TextAreaField("", validators=[DataRequired()])

    submit = SubmitField("Enviar")