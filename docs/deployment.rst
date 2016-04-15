Deployment on OpenShift
~~~~~~~~~~~~~~~~~~~~~~~

OpenShift is an Open-Source Platform-as-a-Service software by Red Hat. It is
also available in its hosted version known as "OpenShift Online" and the first
three websites ("gears") are free.

Clone the repository
====================

You should fork the project on github and use the fork's clone url. For the
sake of the demo, we'll use the main repository URL::

    $ git clone https://github.com/political-memory/toutot.git
    Cloning into 'toutatis'...
    remote: Counting objects: 666, done.
    remote: Total 666 (delta 0), reused 0 (delta 0), pack-reused 665
    Receiving objects: 100% (666/666), 91.12 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (260/260), done.
    Checking connectivity... done.

    $ cd toutatis/

Create your own branch, ie::

    $ git checkout -b yourbranch origin/master
    Branch yourbranch set up to track remote branch pr from origin.
    Switched to a new branch 'yourbranch'

Create an app on OpenShift
==========================

To deploy the website, use a command like::

    $ rhc app-create \
        python-2.7 \
        http://cartreflect-claytondev.rhcloud.com/reflect?github=jpic/openshift-cron-cartridge \
        postgresql-9.2 \
        -a yourtoutatis \
        -e OPENSHIFT_PYTHON_WSGI_APPLICATION=toutatis/wsgi.py \
        --from-code https://github.com/political-memory/toutatis.git \
        --no-git

This should create an app on openshift. Other commands would deploy it at once
but in this tutorial we're going to see how to manage it partly manually for
development.

Add the git remote created by OpenShift
=======================================

Add the git remote openshift created for you, you can see it with
``rhc app-show``, ie.::

    $ rhc app-show -a yourtoutatis
    [snip]
    Git URL:         ssh://569f5cf500045f6a1839a0a4@yourtoutatis-yourdomain.rhcloud.com/~/git/yourtoutatis.git/
    Initial Git URL: https://github.com/political-memory/political_memory.git
    SSH:             569f5cf500045f6a1839a0a4@yourtoutatis-yourdomain.rhcloud.com
    [snip]

Then, add it to your git remotes::

    $ git remote add oo_yourtoutatis ssh://569f5cf500045f6a1839a0a4@yourtoutatis-yourdomain.rhcloud.com/~/git/yourtoutatis.git/

Activate OpenShift's git post-recieve hook
==========================================

Activate OpenShift's post-receive hook on your branch::

    $ rhc app-configure -a yourtoutatis --deployment-branch yourbranch

Deploy your branch
==================

OpenShift will deploy when it receives commits on the deployment branch, to
deploy just do::

    $ git push oo_yourtoutatis yourbranch

If something goes wrong and you want to retry, use the ``rhc app-deploy``
command, ie::

    $ rhc app-deploy yourbranch -a yourtoutatis

Data provisionning
==================

To fill up the representatives database table, either wait for the cron script
to be executed, either do it manually::

    $ rhc ssh -a yourtoutatis 'cd app-root/repo/ && bin/update_all'

OpenShift is fun, login with ssh and look around if you're curious, you'll be
able to recreate your app without much effort if you break it anyway.
