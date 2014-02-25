from flask import render_template, flash, redirect
from forms import SubmitData
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/forms', methods = ['GET', 'POST'])
def submit_data():
    form = SubmitData()
    if form.validate_on_submit():
        flash('Thanks, ' + form.name.data + '  -  ' + form.email.data)
        return redirect('/')
    return render_template('forms.html', title='Submit Data', form=form)