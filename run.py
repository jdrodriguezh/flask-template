from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

# To run migrations with flask we need 3 commands
# flask db init -> this will add migrations folder to our project, needs to be ran only once
# flask db migrate -m "Some message" -> generates a migration script, the message is optional
# flask db upgrade -> applies the migration to the database

# migrations folder needs to be uploaded to our repository

# whenever our models change, we need to repeate migrate and upgrade command

# If db init leads to "KeyError: 'migrate'" this is probably because there's no FLASK_APP env variable set
# try -> set FLASK_APP = run.py or $env:FLASK_APP = "run.py" on windows powershell

if __name__ == '__main__':
    app.run()
