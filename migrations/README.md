## Generic single-database configuration. ##


### Steps to run migration ###
`export FLASK_ENV=development`

`python -m run/flask db init` 
or
`python -m run db init`

`python -m run/flask db migrate` 
or
`python -m run db migrate`

`python -m run/flask db upgrade`
or
`python -m run db upgrade`