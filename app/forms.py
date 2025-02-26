from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class SurveyForm(FlaskForm):
    patient_id = StringField("Kindly Enter Patient ID", validators=[DataRequired(), Length(max=50)])
    patient_name = StringField("Kindly Enter Patient Name", validators=[DataRequired(), Length(max=100)])
    age_group = SelectField(
        "Select your Age Group",
        choices=[
            ("0-18", "0-18"),
            ("19-35", "19-35"),
            ("36-60", "36-60"),
            ("60+", "60+")
        ],
        validators=[DataRequired()]
    )
    contact_number = StringField("Provide your Contact Number", validators=[DataRequired(), Length(max=15)])
    hospital_name = SelectField(
        "Select Hospital",
        choices=[
            ("Park", "Park"),
            ("Fortis", "Fortis"),
            ("Maxx", "Maxx")
        ],
        validators=[DataRequired()]
    )
    department_name = SelectField(
        "Select Department",
        choices=[
            ("Oncology", "Oncology"),
            ("Cardio", "Cardio"),
            ("Common Disease", "Common Disease"),
            ("Ortho", "Ortho")
        ],
        validators=[DataRequired()]
    )
    interaction_rating = IntegerField(
        "On the scale of 1 to 10, how would you rate the hospital interaction?",
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    cleanliness_rating = IntegerField(
        "How much would you rate the hospital cleanliness (1-10)?",
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    emergency_preparedness_rating = IntegerField(
        "How much would you rate the emergency preparedness (1-10)?",
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    transparency_rating = IntegerField(
        "How much transparency did you feel in hospital services (1-10)?",
        validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    insurance_company = SelectField(
        "Among the given insurance providers, select your company:",
        choices=[
            ("LIC", "LIC"),
            ("Reliance Life Insurance", "Reliance Life Insurance"),
            ("Bajaj Allianz", "Bajaj Allianz"),
            ("Star Health", "Star Health"),
            ("Birla SunLife", "Birla SunLife")
        ],
        validators=[DataRequired()]
    )
    satisfaction_level = IntegerField(
        "Overall Satisfaction Level",
        validators=[DataRequired(), NumberRange(min=1, max=10)]

    )
    submit = SubmitField("Submit Feedback")