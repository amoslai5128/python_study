from flask import Flask, render_template
from flask import redirect
from flask import request
import localDB;

from questions import Form
from questions import FormPage
from questions import TextQuestion
from questions import DropdownQuestion


class PageOne(Form):
    name = TextQuestion()
    email = TextQuestion(input_type="email", required="True")


class PageTwo(Form):
    country = DropdownQuestion(choices_by_url={"value_name": "name",
        "url": "https://restcountries.eu/rest/v2/all"})
    birthdate = TextQuestion(input_type="date")


class Profile(Form):
    page_one = FormPage(PageOne, title="Identification Information")
    page_two = FormPage(PageTwo, title="Additional Information")


app = Flask(__name__)

@app.route("/", methods=("GET",))
def form():
    form = Profile()
    formHTML = form.render_html() 
    return render_template('index.html', form=formHTML)

@app.route("/", methods=("POST",))
def post(): 
    form_data = request.get_json()
    # Here, we would save to a database or something
    localDB.saveFormToDB(form_data)
    return redirect("/thanks")

@app.route("/thanks")
def thanks():
    abcResult = localDB.queryFormResult('sdbas@sbab.com')
    return "Thanks for your information. </ br><span>{}</span>".format(abcResult)

if __name__ == "__main__":
    app.run()
 
