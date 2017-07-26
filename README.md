# TOKEN

Method: POST

URL: http://127.0.0.1:8000/api-auth/login/

Header:
~~~~
Accept application/json

Content-Type application/json
~~~~

Body:
~~~~
{
  "email": "durmusyasar3@gmail.com",
  "password": "doit2017"
}
~~~~

Sample Request:
~~~~
  curl --request POST \
  --url http://127.0.0.1:8000/api-auth/login/ \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{
    "email": "durmusyasar3@gmail.com",
    "password": "doit2017"
  }'
~~~~

Response:
~~~~
{
  "auth_token": "91f4def1bee0d16730aef26879de74d10b7cad96"
}
~~~~

# TASKS

Method: GET

URL: http://127.0.0.1:8000/api/v1/tasks/

Header:
~~~~
Authorization TOKEN 91f4def1bee0d16730aef26879de74d10b7cad96
~~~~

Sample Request:
~~~~
curl --request GET \
 --url http://127.0.0.1:8000/api/v1/tasks/ \
 --header 'authorization: Token 91f4def1bee0d16730aef26879de74d10b7cad96'
~~~~

Response:
~~~~
[
   {
       "id": 1,
       "user": 1,
       "title": "sdfghjk"
   }
]
~~~~

# TASKS DETAIL

Method: GET

URL: http://127.0.0.1:8000/api/v1/tasks/1

Header: 
~~~~
Authorization TOKEN 5f9675e15afff2a957e481dbec0a47339ac2f4ea
~~~~

Sample Request:
~~~~
curl --request GET \
 --url http://127.0.0.1:8000/api/v1/tasks/1 \
 --header 'authorization: Token 5f9675e15afff2a957e481dbec0a47339ac2f4ea'
~~~~

Response:
~~~~
{
   "id": 1,
   "user": 1,
   "title": "adsafa",
   "description": "afasfasfasfas",
   "reminders": [
       {
           "id": 1,
           "date": "2017-07-25T16:27:18Z"
       }
   ]
}
~~~~

# DEPLOYMENT

Uzak Sunucuya Bağlanma:
~~~~
ssh root@207.154.223.187
~~~~

## Ngnix

* ### Installation
  ~~~~
  sudo apt-get update
  sudo apt-gey install ngnix
  ~~~~

* ### Status
  ~~~~
  systemctl status ngnix
  ~~~~

* ### Documentation
  ~~~~
  https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04
  ~~~~

## Supervisor:
* ### Installation
  ~~~~
  sudo apt-get install supervisor
  ~~~~

* ### Restart
  ~~~~
  service supervisor restart
  ~~~~

* ### Documantation
  ~~~~
  https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps
  ~~~~

## Python
  ~~~~
  sudo apt-get install python-pip
  ~~~~

## Virtualenv
  ~~~~
  sudo apt-get install virtualenv
  ~~~~

## Add New User
  ~~~~
  adduser apps
  ~~~~

## Yeni User' a Geçiş Yapmak için:
  ~~~~
  su - apps
  ~~~~

## Oluşturulan User ' a sudo yetkisi vermek için:
  ~~~~
  sudo usermod -a -G apps
  ~~~~

## Yedeklemeler, konfigürasyon, uygulama patlarsa eğer nedenlerini görebileceğimiz ve kaynak kodlarının bulunacağı dizinler
~~~~
  doit
    * backup
    * conf
      * gunicorn.sock
      * gunicorn start
    * log
      * gunicorn_supervisor.log
      * nginx-access.log
      * nginx-error.log
    * web
      * env
      * source
        * Proje Dosyaları
        * requirements
~~~~

## web dosyasının içerisine virtualenv kurulup aktif edilir:
  ~~~~
  virtualenv -p python3 env
  source env/bin/activate
  ~~~~

## 4096 Bitlik ve RSA ile şifrelenmiş SSH Key' ini oluşturmak içim
  ~~~~
  ssh-keygen -t rsa -b 4096 -C "digitalocean-doit-apps"
  ~~~~

## Postgresql Veri Tabanı
  ~~~~
  sudo apt-get install postgresql postgresql-contrib
  ~~~~

* ### postgresql terminaline girip Database oluşturduk, ardından kullanıcı oluşturup yetkilerini verdik:
  ~~~~
  postgres@doit:~$ psql
  postgres=# CREATE DATABASE doitdb;
  postgres=# CREATE USER doit WITH PASSWORD '-';
  postgres=# GRANT ALL PRIVILEGES ON DATABASE doitdb to doit;
  postgres=# \q
  postgres@doit:~$ exit
  ~~~~

Oluşturduğumuz database bilgilerini projemizdeki settings.py dosyası içerisindeki DATABASES içerisine kaydettik.

## Django,Psycopg2,Gunicorn ,Django Rest Framework ve Djoser
  ~~~~
  pip install Django
  pip install djangorestframework
  pip install djoser
  pip install psycopg2
  pip install gunicorn
  ~~~~












