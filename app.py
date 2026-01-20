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
            'title': 'E-commerce Platform',
            'description': 'A full-stack e-commerce solution with payment integration, user authentication, and admin dashboard.',
            'technologies': ['Flask', 'SQLAlchemy', 'Bootstrap', 'Stripe'],
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Data Analytics Dashboard',
            'description': 'Real-time data visualization dashboard for business metrics and KPIs with interactive charts.',
            'technologies': ['Python', 'Plotly', 'Pandas', 'React'],
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Machine Learning Model',
            'description': 'Predictive analytics model for customer churn with 95% accuracy using ensemble methods.',
            'technologies': ['Python', 'Scikit-learn', 'TensorFlow', 'Flask API'],
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Social Media App',
            'description': 'Full-featured social platform with real-time messaging, posts, and user interactions.',
            'technologies': ['Django', 'PostgreSQL', 'WebSocket', 'Redis'],
            'github': '#',
            'demo': '#'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/skills')
def skills():
    skills_data = {
        'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Bootstrap', 'Tailwind CSS'],
        'Backend': ['Python', 'Flask', 'Django', 'Node.js', 'REST API', 'GraphQL'],
        'Database': ['MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLAlchemy'],
        'DevOps': ['Git', 'Docker', 'AWS', 'CI/CD', 'Linux', 'Nginx'],
        'Data Science': ['Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'Matplotlib'],
        'Others': ['Agile', 'Problem Solving', 'DSA', 'System Design']
    }
    return render_template('skills.html', skills=skills_data)

@app.route('/resume')
def resume():
    experience = [
        {
            'title': 'Senior Full Stack Developer',
            'company': 'Tech Corp',
            'period': '2023 - Present',
            'description': 'Leading development of scalable web applications and mentoring junior developers.'
        },
        {
            'title': 'Full Stack Developer',
            'company': 'Digital Solutions Inc',
            'period': '2021 - 2023',
            'description': 'Developed and maintained multiple client projects using Flask and React.'
        }
    ]
    education = [
        {
            'degree': 'B.Tech in Computer Science',
            'institution': 'University Name',
            'period': '2017 - 2021',
            'description': 'Graduated with First Class Honours'
        }
    ]
    return render_template('resume.html', experience=experience, education=education)

@app.route('/handles')
def handles():
    social_handles = [
        {'name': 'GitHub', 'url': 'https://github.com/yourusername', 'icon': '💻'},
        {'name': 'LinkedIn', 'url': 'https://linkedin.com/in/yourusername', 'icon': '💼'},
        {'name': 'Twitter', 'url': 'https://twitter.com/yourusername', 'icon': '🐦'},
        {'name': 'Email', 'url': 'mailto:your.email@example.com', 'icon': '📧'}
    ]
    return render_template('handles.html', handles=social_handles)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would send email or save to database
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')
@app.route('/certificates')
def certificates():
    certificates_list = [
        {
            'title': 'Python for Everybody',
            'issuer': 'Coursera',
            'year': '2024',
            'description': 'Comprehensive Python programming certification covering basics to advanced concepts.',
            'image': '/static/certificates/python.jpg',
            'credential': 'https://coursera.org/verify/XXXXX'
        },
        {
            'title': 'Full Stack Web Development',
            'issuer': 'Udemy',
            'year': '2023',
            'description': 'Hands-on full stack development using Flask, React, and databases.',
            'image': '/static/certificates/fullstack.jpg',
            'credential': 'https://udemy.com/certificate/XXXXX'
        },
        {
            'title': 'Data Science & Machine Learning',
            'issuer': 'IBM',
            'year': '2023',
            'description': 'Data analysis, visualization, and ML models using Python.',
            'image': '/static/certificates/datascience.jpg',
            'credential': '#'
        }
    ]
    return render_template('certificates.html', certificates=certificates_list)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)