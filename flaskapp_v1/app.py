from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'role': 'Backend Engineer',
        'locution': 'Bangalore',
        'salary': '₹ 20,00,000'
    },
    {
        'id': 2,
        'role': 'Data Scientist',
        'locution': 'Tanny Road',
        'salary': '₹ 3,70,000'
    },
    {
        'id': 3,
        'role': 'Frontend Developer',
        'locution': 'Hyderabad',
        'salary': '₹ 12,00,000'
    },
    {
        'id': 4,
        'role': 'DevOps Engineer',
        'locution': 'Pune',
        'salary': '₹ 15,50,000'
    },
    {
        'id': 5,
        'role': 'UI/UX Designer',
        'locution': 'Remote',
        'salary': '₹ 9,80,000'
    },
    {
        'id': 6,
        'role': 'Cybersecurity Analyst',
        'locution': 'Delhi',
        'salary': '₹ 13,20,000'
    },
    {
        'id': 7,
        'role': 'Mobile App Developer',
        'locution': 'Mumbai',
        'salary': '₹ 11,00,000'
    },
]

@app.route("/")
def sayhello():
    return render_template('demo.html', job=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
