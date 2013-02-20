# Haginator

## How to deploy to Heroku

1. Add Heroku repos on remote : `git remote add heroku git@heroku.com:haginator.git`
2. Push to Heroku : `git push heroku master`
3. Sync DB on HerokuPostgres : `heroku run python manage.py syncdb`
4. Load fixture : `heroku run python manage.py loaddata initial_data_fixture.json`

