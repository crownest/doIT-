# Development


## Required Packages

**Pip**
```bash
apt-get update
apt-get python-pip
```

**Virtualenv**
```bash
apt-get update
apt-get virtualenv
```


## Steps for running the project

**Create project and change directory**
```bash
mkdir doit-backend
cd doit-backend
```

**Create virtualenv with python3**
```bash
virtualenv -p python3 env
```

**Make active virtualenv**
```bash
source env/bin/activate
```

**Get source code**
```bash
git clone https://github.com/crownest/doit-backend.git source (Use HTTPS)
git clone git@github.com:crownest/doit-backend.git source     (Use SSH)
```

**Change directory and branch**
```bash
cd source
git checkout staging
```

**Create required files**
```bash
cp doit/settings/local-dist.py doit/settings/local.py
touch doit/settings/secrets.py
```

Note: Please ask secret credentials from admin.

**Install requirements**
```bash
pip install -r requirements/staging.txt
pip install -r requirements/extra.txt
```

**Create database**
```bash
./manage.py migrate
```

**Load initial data**
```bash
./manage.py loaddata fixtures/initial_data.json
```

**Run project**
```bash
./manage.py runserver 0.0.0.0:8000 (http://127.0.0.1:8000)
```

**Run tests**
```bash
./manage.py test doit.apps
./manage.py test doit.apps -v 2
./manage.py test doit.apps --verbosity=2
```

Note: Verbosity level (-v or --verbosity); 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
