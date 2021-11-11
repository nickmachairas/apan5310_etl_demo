# apan5310_etl_demo
ETL demo using Flask and SQLAlchemy


Initialize database (first time only)
```
flask db init
flask db migrate -m 'initialize database'
flask db upgrade
```

On the Ubuntu WSL we need to export the database connection string as an environment variable in order for ``run_etl.py`` to run properly.
```
export DATABASE_URL=postgresql://postgres:123@localhost:5432/etl_app
```
