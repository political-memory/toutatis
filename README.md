```
cd /tmp
virtualenv toutatis_example
source toutatis_example/bin/activate

git clone https://github.com/political-memory/toutatis.git
cd toutatis
cp toutatis/config.json.sample toutatis/config.json
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
