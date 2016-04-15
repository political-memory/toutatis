[![Build Status](https://travis-ci.org/political-memory/toutatis.svg?branch=master)](https://travis-ci.org/political-memory/toutatis)
```
cd /tmp
virtualenv toutatis_example
source toutatis_example/bin/activate

git clone https://github.com/political-memory/toutatis.git
cd toutatis
./manage.py migrate
./manage.py runserver
bin/parltrack_update representatives
bin/parltrack_update dossiers
bin/parltrack_update votes
```
