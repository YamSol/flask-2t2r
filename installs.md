# Requisites
- Docker,
	- `yay -S docker`
	- `sudo systemctl enable docker && sudo systemctl start docker`
- Dbeaver
	- `yay -S dbeaver`

# Mongodb
- pull Mongodb image:
	- `docker pull mongodb/mongodb-community-server`
- install image:
	- `docker run --name mongo -d mongodb/mongodb-community-server:latest`
- start image:
	- `sudo docker start mongo`
- connect to shell:
	- `docker exec -it mongo mongosh`
- descobrir ip da imagem:
	- `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb`

# MariaDB
- pull image:
	- `docker pull mariadb`
- install image:
	- `docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD="mariadb" mariadb:latest`
- start image:
	- `docker start mariadb`
- OBS: use dbeaver 

# MySQL
- pull image:
	- `docker pull container-registry.oracle.com/mysql/community-server`
- install image:
	- `docker run --name mysql container-registry.oracle.com/mysql/community-server:latest`
- get generated root password:
	- `docker logs mysql 2>&1 | grep GENERATED`
- shell connect:
	- `docker exec -it mysql mysql -uroot -p`
	- Create new user:
		- `CREATE USER '<user-name>'@'localhost' IDENTIFIED BY '<password>';`
		- `GRANT ALL PRIVILEGES ON *.* TO '<user-name>'@'localhost' WITH GRANT OPTION;`
		- `FLUSH PRIVILEGES;`
		

- find ip address:
	- `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql`
- SQL queries:
	```sql
	create table tasks ( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(255), checked bool );
	```