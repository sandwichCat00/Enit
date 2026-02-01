from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "campus_secret_key"

# --- COMMON ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')






# @app.route('/login/student', methods=['GET', 'POST'])
# def student_login():
#     if request.method == 'POST':
#         print("DEBUG: Student Login Button Clicked!") 
#         return render_template('student/dashboard_stud.html')
#     return render_template('auth/student_login.html')


@app.route('/login/student', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        print("DEBUG: Student Login Button Clicked!") 
        # FIX: Do not render the HTML here. Redirect to the function that prepares the data.
        return redirect(url_for('student_dashboard'))
        
    # Matches: templates/auth/student_login.html
    return render_template('auth/student_login.html')





@app.route('/login/company', methods=['GET', 'POST'])
def company_login():
    if request.method == 'POST':
        print("DEBUG: Company Login Button Clicked!") 
        return render_template('company/dashboard_comp.html')
    return render_template('auth/company_login.html')




@app.route('/company/dashboard_comp')
def company_dashboard():
    return render_template('company/dashboard_comp.html')

@app.route('/company/post-job')
def post_job():
    return render_template('company/post_job.html')

@app.route('/company/applications')
def view_applications():
    return render_template('company/application.html')


@app.route('/student/dashboard')
def student_dashboard():
    # 1. Create dummy data (later this will come from your database)
    student_data = {
        'name': 'Rahul Sharma',
        'branch': 'Computer Science',
        'cgpa': 8.5
    }

    return render_template('student/dashboard_stud.html', student=student_data)

if __name__ == '__main__':
    app.run(debug=True)

