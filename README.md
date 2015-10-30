# OLD MASTER

this is the master branch as i got it from @psycojoker

For dev:

    git clone git@github.com:Psycojoker/toutatis.git
    git clone git@github.com:Psycojoker/django-parltrack-meps.git
    git clone git@github.com:Psycojoker/django-parltrack-votes.git

    cd toutatis
    ln -s ../django-parltrack-meps/parltrack_meps/ .
    ln -s ../django-parltrack-votes/parltrack_votes/ .

    virtualenv ve
    source ve/bin/activate

    pip install -r requirements-dev.txt

    python manage.py syncdb
    python manage.py update_meps
    python manage.py import_ep_votes_data
