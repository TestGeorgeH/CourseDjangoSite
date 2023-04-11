# CourseDjangoSite

This is a test project, created for practicing the Django framework

This project uses postgresql and redis databases.
Install them using names form ./store/.env or add your names and passwords to the file.

Also stripe is being used for paying. Configure it likewise,
and create and enable all ot their servicies.

After that install Python3, Pip3 and Pipenv and run:

```
pipenv install
pipenv shell
./store/manage.py runserver
```
If you face some problems with psycopg2,
try installing psycopg2-binary with pip3, and after that reinstalling psycopg2.

If that doesn't work ither, try manualy installing prerequsisites for psycopg2
like this:

```
sudo apt install libpq-dev python3-dev
```
