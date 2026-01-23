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
        'description': 'A secure election management web app that helps organizations create, manage, and conduct elections with controlled access, smooth voting flow, and instant result visibility — built for low to mid-scale enterprise use.',
        'technologies': ['PHP', 'MYSQL', 'HTML', 'CSS', 'BOOTSTRAP', 'JAVASCRIPT'],
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
        'description': 'An AI-powered support platform for farmers that provides smart problem resolution, real-time weather insights, and easy access to government schemes — designed to improve decision-making and productivity.',
        'technologies': ['Flask', 'SqlAlchemy', 'HTML', 'css', 'sqlite'],
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
        'description': 'A personal finance tracker that allows users to record expenses, categorize spending, and monitor budgets with a clean dashboard — helping users stay in control of money with clarity and consistency.',
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
        'title': 'WordWander',
        'description': 'A full-featured book e-commerce platform with product browsing, order tracking, and smooth customer flow — built to simulate real-world online shopping with practical backend logic.',
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
        'description': 'A MERN-based e-commerce application developed collaboratively, where I delivered the frontend experience — building responsive UI components, product flow screens, and user-friendly navigation.',
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
        'title': 'WordWander (Frontend Version)',
        'description': 'A lightweight frontend-only book selling UI built using HTML, CSS, and JavaScript — focused on clean design, responsive layout, and smooth user interaction.',
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
        'title': 'Python for Beginners',
        'issuer': 'Simplilearn',
        'year': '2025',
        'description': 'Completed foundational Python training covering core syntax, functions, loops, and real-world problem solving — strengthening programming fundamentals for backend development and automation.',
        'image': '/static/images/python.jpg',
        'credential': 'https://simpli-web.app.link/e/yjds4trrpUb'
    },
    {
        'title': 'JavaScript for Beginners',
        'issuer': 'Simplilearn',
        'year': '2025',
        'description': 'Built strong JavaScript fundamentals including DOM manipulation, events, and interactive web logic — enabling dynamic frontend development and clean UI behavior.',
        'image': '/static/images/javascript.jpg',
        'credential': 'https://simpli-web.app.link/e/Jp4GPVwrpUb'
    },
    {
        'title': 'Demystifying AI/ML Roles: How to Build a Career in AI',
        'issuer': 'Scaler',
        'year': '2025',
        'description': 'Attended an industry-focused masterclass on AI/ML career paths, required skill sets, and real-world role expectations — gaining clarity on roadmap and learning strategy.',
        'image': '/static/images/certificate3.png',
        'credential': '#'
    },
    {
        'title': 'What It Takes to Be a Data Scientist at Microsoft',
        'issuer': 'Scaler',
        'year': '2025',
        'description': 'Learned practical insights into data science workflows, business problem framing, and model-building mindset used in top product companies — with focus on impact-driven analytics.',
        'image': '/static/images/certificate2.png',
        'credential': 'https://udemy.com/certificate/XXXXX'
    },
    {
        'title': 'Fundamentals of Docker and Kubernetes',
        'issuer': 'Scaler',
        'year': '2025',
        'description': 'Covered containerization and orchestration basics including Docker images, containers, and Kubernetes concepts — improving deployment understanding and DevOps fundamentals.',
        'image': '/static/images/certificate1.png',
        'credential': '#'
    }
]

    return render_template('certificates.html', certificates=certificates_list)
@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    