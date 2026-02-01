from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "campus_secret_key"

# --- COMMON ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/student', methods=['GET', 'POST'])
def student_login():
    return render_template('auth/student_login.html')

@app.route('/login/company', methods=['GET', 'POST'])
def company_login():
    return render_template('auth/company_login.html')




@app.route('/company/dashboard')
def company_dashboard():
    return render_template('company/dashboard.html')

@app.route('/company/post-job')
def post_job():
    return render_template('company/post_job.html')

@app.route('/company/applications')
def view_applications():
    return render_template('company/application.html')


@app.route('/student/dashboard')
def student_dashboard():
   
    return render_template('student/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

