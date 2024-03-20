from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)

app.secret_key = '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'

class CallMeForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    phone = StringField('Phone Number', validators=[InputRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=50)])
    message = TextAreaField('Message')  # Added message field
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    form = CallMeForm()
    if form.validate_on_submit():
        # Process the form data (e.g., send email, store in database)
        # Implement your logic here
        return 'Thank you! We will get back to you soon.'
    return render_template('chatbot.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
