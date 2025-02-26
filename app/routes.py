from flask import Blueprint, render_template, redirect, url_for
from .forms import SurveyForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

main_bp = Blueprint('main', __name__)

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key("17oD8q47t7MRAJ0RMV4SnAmcokt4ZB-ytUZ7Mpqi_ox4").sheet1

@main_bp.route("/", methods=["GET", "POST"])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        # Add timestamp in requested format
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Collect data from form
        data = [
            timestamp,
            form.patient_id.data,
            form.patient_name.data,
            form.age_group.data,
            form.contact_number.data,
            form.hospital_name.data,
            form.department_name.data,
            form.interaction_rating.data,
            form.cleanliness_rating.data,
            form.emergency_preparedness_rating.data,
            form.transparency_rating.data,
            form.insurance_company.data,
            form.satisfaction_level.data,
        ]
        
        # Append data to Google Sheet
        sheet.append_row(data)
        return redirect(url_for(".success"))

    return render_template("index.html", form=form)

@main_bp.route("/success")
def success():
    return render_template("success.html")

@main_bp.route("/dashboard")
def dashboard():
    return redirect("https://lookerstudio.google.com/u/0/reporting/3150ed17-47e8-417f-9e38-d7c89ac44cee/page/vZ7jD?s=j4g2CqzS878")
