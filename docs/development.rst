Local development tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial drives through a local installation of the project for
development on Linux. This tutorial should not describe how to setup and
maintain an instance of Memopol in production, for reference see
:file:`.openshift/action_hooks/deploy`.

Make a virtual environment
==========================

For the sake of the tutorial, we'll do this in the temporary directory, but you
could do it anywhere::

    $ cd /tmp

Create a python virtual environment::

    $ virtualenv toutatis_env
    Using real prefix '/usr'
    New python executable in toutatis_env/bin/python2
    Also creating executable in toutatis_env/bin/python
    Installing setuptools, pip, wheel...done.

Don't forget to activate it **in every shell session**::

    $ source toutatis_env/bin/activate

Clone the repository
====================

You should fork the project on github and use the fork's clone url. For the
sake of the demo, we'll use the main repository URL::

    $ git clone https://github.com/political-memory/toutatis.git
    Cloning into 'toutatis'...
    remote: Counting objects: 2516, done.
    remote: Compressing objects: 100% (109/109), done.
    remote: Total 2516 (delta 44), reused 0 (delta 0), pack-reused 2402
    Receiving objects: 100% (2516/2516), 4.40 MiB | 79.00 KiB/s, done.
    Resolving deltas: 100% (1103/1103), done.
    Checking connectivity... done.

And enter the directory::

    $ cd toutatis/

Create your own branch, ie::

    $ git checkout -b yourbranch origin/master
    Branch yourbranch set up to track remote branch pr from origin.
    Switched to a new branch 'yourbranch'

Install Python dependencies
===========================

Then, install the package for development::

    $ pip install -e .
    Obtaining file:///tmp/toutatis
    Collecting django (from political-memory==0.0.1)
      Using cached Django-1.9-py2.py3-none-any.whl

    [output snipped for readability]

    Installing collected packages: django, sqlparse, django-debug-toolbar, django-pdb, six, django-extensions, werkzeug, south, pygments, markdown, hamlpy, django-coffeescript, ijson, python-dateutil, pytz, political-memory
      Running setup.py develop for political-memory
    Successfully installed django-1.9 django-coffeescript-0.7.2 django-debug-toolbar-1.4 django-extensions-1.5.9 django-pdb-0.4.2 hamlpy-0.82.2 ijson-2.2 markdown-2.6.5 political-memory pygments-2.0.2 python-dateutil-2.4.2 pytz-2015.7 six-1.10.0 south-1.0.2 sqlparse-0.1.18 werkzeug-0.11.2

Activate ``DJANGO_DEBUG``
=========================

``DEBUG`` is disabled by default, the development server won't run properly by
default thnen, to enable it export the ``DJANGO_DEBUG`` variable in the current
shell::

    $ export DJANGO_DEBUG=True

Run the development server
==========================

Run the development server::

    $ ./manage.py runserver

    Performing system checks...

    System check identified no issues (0 silenced).
    December 09, 2015 - 21:26:47
    Django version 1.8.7, using settings 'toutatis.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    [09/Dec/2015 21:26:48] "GET / HTTP/1.1" 200 13294

The website is running on ``http://127.0.0.1:8000/``.

Database migrations
===================

The repo comes with a pre-configured SQLite db with sample data so that you can
start hacking right away. However, if you were to use a local postgresql
database ie. with this sort of environment::

    export DJANGO_DATABASE_DEFAULT_NAME=toutatis
    export DJANGO_DATABASE_DEFAULT_USER=postgres
    export DJANGO_DATABASE_DEFAULT_ENGINE=django.db.backends.postgresql_psycopg2
    export DJANGO_DEBUG=1
    export DJANGO_SETTINGS_MODULE=toutatis.settings

Then you could run database migrations::

    $ ./manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: django_filters, staticfiles, datetimewidget, autocomplete_light, messages, adminplus, compressor, humanize, django_extensions, constance, bootstrap3
      Apply all migrations: legislature, votes, database, admin, positions, sessions, representatives, auth, contenttypes, representatives_votes, taggit
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
      Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK

    [output snipped for readability]

      Applying taggit.0002_auto_20150616_2121... OK

Provision with data
===================

Or actual data (takes a while)::

    $ bin/update_all
