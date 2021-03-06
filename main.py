import data_manager
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all-mentors-by-name')
def mentor_names():
    mentor_names = data_manager.get_all_mentors_names()
    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/mentors-from-Miskolc-by-nickname')
def mentor_nicknames():
    mentor_names = data_manager.get_mentors_nicknames('Miskolc')
    return render_template('nicknames.html', mentor_names=mentor_names)


@app.route('/Carol-phonenumber')
def carol_fullname():
    applicant_names = data_manager.get_full_name()
    return render_template('carol_hat.html', applicant_names=applicant_names)


@app.route('/hat-owner-by-email')
def name_by_email():
    applicant_names = data_manager.get_full_name_with_email()
    return render_template('name_by_email.html', applicant_names=applicant_names)


@app.route('/add-new-applicant', methods=['GET', 'POST'])
def add_new_applicant():
    if request.method == 'GET':
        return render_template('new_applicant.html')
    elif request.method == 'POST':
        return render_template('index.html')
        # first_name = request.form['first_name']
        # last_name = request.form['last_name']
        # phone_number = request.form['phone_number']
        # email = request.form['email']
        # application_code = 54823
        # return redirect('new_applicant_details.html',
        #                        first_name=first_name,
        #                        last_name=last_name,
        #                        phone_number=phone_number,
        #                        email=email,
        #                        application_code=application_code
        #                        )
        # try:
        #     add_new_applicant(cursor, first_name, last_name, phone_number, email, application_code)
        #     new_name =  display_new_applicant(first_name)
        #     return redirect('new_applicant_details.html', new_name=new_name)
        # except:
        #     return "issue???"


if __name__ == '__main__':
    app.run(debug=True)


