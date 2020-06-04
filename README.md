# Mynd
Mynd is a social networking website where users can share and view images according to topics.

# Packages Installation

* Mysql installation
```bash
echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install mysql-server-5.7
```

* Python packages installation
```bash
sudo apt-get update
sudo apt-get install python3.6
pip3 install Flask
pip3 install SQLAlchemy==1.2.5
pip3 install SQLAlchemy-ImageAttach
```