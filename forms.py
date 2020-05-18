from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class searchForm (FlaskForm):
   search = StringField('search', validators=[DataRequired(), Length(min=2, max=40)])
   submit = SubmitField('Pretraga')