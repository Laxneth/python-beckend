from app import db  

# Define the Person model which maps to the 'people' table in the database
class Person(db.Model):
    __tablename__ = 'people'  # Set the table name explicitly to 'people'
    
    # Primary key column (unique identifier for each person)
    pid = db.Column(db.Integer, primary_key=True)
    
    # Name column - cannot be null
    name = db.Column(db.Text, nullable=False)
    
    # Age column - can be null
    age = db.Column(db.Integer)
    
    # Job column - can be null
    job = db.Column(db.Text)
    
    # String representation of the object, useful for debugging
    def __repr__(self):
        return f'Person with name {self.name} and age {self.age}'
