from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ExamForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    date = DateField('Exam Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Exam')