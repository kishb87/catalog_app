apt-get -qqy update
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
apt-get -qqy install psql
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
pip install flask-login
pip install flask-script
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install WTForms-Alchemy



vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd

