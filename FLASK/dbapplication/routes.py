from flask import render_template, request, jsonify
from models import Person

def register_routes(app, db):

    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == 'GET':
            # Fetch all people from the database to display on the page
            people = Person.query.all()
            return render_template('index.html', people=people)

        elif request.method == 'POST':
            # Get form input values
            name = request.form.get("name")
            age = int(request.form.get("age"))
            job = request.form.get("job")

            # Create and save a new Person record in the database
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()

            # Fetch updated list of people after adding a new person
            people = Person.query.all()
            return render_template('index.html', people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        # Delete the person with the given pid from the database
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()

        # Fetch updated list after deletion
        people = Person.query.all()
        return render_template('index.html', people=people)
     
    @app.route('/details/<pid>')
    def details(pid):
        # Retrieve a specific person by pid for the details view
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('details.html', person=person)
