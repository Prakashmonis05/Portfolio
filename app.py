import os

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'E-vote',
            'description': 'A web app to easly create and host the election in low to medium level enterprises.',
            'technologies': ['PHP', 'MYSQL', 'HTML', 'CSS', 'BOOTSTRAP','JAVASCRIPT'],
            'github': '#',
            'demo': 'https://evote.infinityfree.me',
            'images': [
                '/static/images/evote1.png',
                '/static/images/evote2.png',
                '/static/images/evote3.png',
                '/static/images/evote4.png',
                '/static/images/evote5.png'
            ]
        },
        {
            'title': 'AgriReach',
            'description': 'A unified platform for farmers where they can resolve the problems with AI and can see weather data and schemes provided by the government.',
            'technologies': ['Flask', 'SqlAlchemy', 'HTML', 'css','sqlite'],
            'github': 'https://github.com/Prakashmonis05/AgriReach.git',
            'demo': 'https://agrireach.onrender.com',
            'images': [
                '/static/images/agri1.png',
                '/static/images/agri2.png',
                '/static/images/agri3.png',
                '/static/images/agri4.png',
                '/static/images/agri5.png',
                '/static/images/agri6.png',
            ]
        },
        {
            'title': 'Expense Tracker',
            'description': 'A platform that helps its user to track their expenses and manage it',
            'technologies': ['Flask', 'SqlAlchemy', 'HTML', 'css', 'postgress'],
            'github': 'https://github.com/Prakashmonis05/Expense_Tracker_flask_app.git',
            'demo': 'https://expense-tracker-flask-app-1.onrender.com',
            'images': [
                 '/static/images/ex1.png',
                 '/static/images/ex2.png',
                 '/static/images/ex3.png'
            ]
        },
        {
            'title': 'Wordwander',
            'description': 'A E-commerce website that sells the books and have features of tracking the orders',
            'technologies': ['PHP', 'MySql', 'HTML', 'css', 'js'],
            'github': 'https://github.com/Prakashmonis05/WordWander.git',
            'demo': 'https://wordwander.wuaze.com',
            'images': [
                 '/static/images/word1.png',
                 '/static/images/word2.png',
                 '/static/images/word3.png',
                 '/static/images/word4.png',
            ]
        },
        {
            'title': 'Shop X',
            'description': 'A E-commerce platform developed with the help of my colloborators and i have done the frontend part',
            'technologies': ['Reactjs', 'Nodejs', 'Expressjs', 'MongoDB'],
            'github': 'https://github.com/Shashidharak89/E-COMMERCE-MERN',
            'demo': 'https://e-commerce-mern-beta.vercel.app/',
            'images': [
                 '/static/images/shop1.png',
                 '/static/images/shop2.png',
                 '/static/images/shop3.png',
                 '/static/images/shop4.png',
            ]
        },
        {
            'title': 'word wander ',
            'description': 'A Frontend based a book selling platform that is used to sells the books.',
            'technologies': ['HTML', 'CSS', 'Js'],
            'github': 'https://github.com/Prakashmonis05/WordWander-HTML-Version.git',
            'demo': 'https://prakashmonis05.github.io/WordWander-HTML-Version/',
            'images': [
                 '/static/images/wand1.png',
                 '/static/images/wand2.png',
                 '/static/images/wand3.png',
            ]
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/skills')
def skills():
    skills_data = {
        'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Bootstrap'],
        'Backend': ['Python', 'Flask','PHP' ],
        'Database': ['MySQL', 'PostgreSQL', 'MongoDB', 'Sqlite', 'SQLAlchemy'],
        'Data Science': ['Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'Matplotlib'],
        'Others': ['Problem Solving', 'Intermediate-DSA', 'System Design']
    }
    return render_template('skills.html', skills=skills_data)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/handles')
def handles():
    social_handles = [
        {'name': 'GitHub', 'url': 'https://github.com/prakashmonis05', 'icon': '💻'},
        {'name': 'LinkedIn', 'url': 'https://linkedin.com/in/prakashmonis005', 'icon': '💼'},
        {'name': 'Whatsapp', 'url': 'https://wa.me/918867252705', 'icon': '💬'},
        {'name': 'Email', 'url': 'mailto:prakashmonis06@gmail.com', 'icon': '📧'}
    ]
    return render_template('handles.html', handles=social_handles)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/certificates')
def certificates():
    certificates_list = [
        {
            'title': 'Python for beginners',
            'issuer': 'Simplilearn',
            'year': '2025',
            'description': 'A course offered by simplilearn for python beginners.',
            'image': '/static/images/python.jpg',
            'credential': 'https://simpli-web.app.link/e/yjds4trrpUb'
        },
        {
            'title': 'Javascript for beginners',
            'issuer': 'Simplilearn',
            'year': '2025',
            'description': 'A course offered by simplilearn for python beginners.',
            'image': '/static/images/javascript.jpg',
            'credential': 'https://simpli-web.app.link/e/Jp4GPVwrpUb'
        },
        {
            'title': 'Demystifying AI/ML roles: How to build a career in AI',
            'issuer': 'Scaler',
            'year': '2025',
            'description': 'A masterclass held by scaler.',
            'image': '/static/images/certificate3.png',
            'credential': '#'
        },
        {
            'title': 'what it takes to be a Data scientist at Microsoft',
            'issuer': 'scaler',
            'year': '2025',
            'description': 'A masterclass held by scaler.',
            'image': '/static/images/certificate2.png',
            'credential': 'https://udemy.com/certificate/XXXXX'
        },
        {
            'title': 'Fundamentals of Docker and Kubernetes',
            'issuer': 'Scaler',
            'year': '2025',
            'description': 'A masterclass held by scaler.',
            'image': '/static/images/certificate1.png',
            'credential': '#'
        }
    ]
    return render_template('certificates.html', certificates=certificates_list)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    