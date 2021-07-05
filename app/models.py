from app import db


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


class EmployeesModel(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    salary = db.Column(db.Float())
    position = db.Column(db.String())

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def __repr__(self):
        return f"<Employee {self.name}>"
