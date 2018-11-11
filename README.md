##### Clone repository  

    git clone https://github.com/locvx1234/backup-mgmt

##### Install Mysql 

    sudo apt install mysql-server
    sudo mysql_secure_installation
    
##### Install requirements

    sudo apt install libmysqlclient-dev
    pip3 install -r requirements.txt

##### Run the code
    cd backup-mgmt
    python manage.py runserver 0.0.0.0:80
    
##### Behold!
Go to http://localhost:80/

##### Tempale

[Gentelella](https://github.com/puikinsh/gentelella)

#### Build with Docker

	git clone https://github.com/locvx1234/backup-mgmt
	docker build .
	docker-compose up


