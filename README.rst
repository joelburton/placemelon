Placemelon
==========

.. image:: http://placemelon.com/600/400

A FPO image site using delicious, delicious melon photos.

A straightforward Flask app.

Requirements:

- Memcache server

- Python 2

Installation
------------

::

  $ git clone https://github.com/joelburton/placemelon.git placemelon.com
  $ cd placemelon.com
  $ virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

It can be run from the command line, but it is NOT intended for that -- in fact when done so,
it runs in Flask debug mode, which is **highly insecure**.

Instead, it is meant to be run under a WSGI server, like gunicorn or uWSGI.

::

  $ sudo ln -s /path/to/here/conf/uwsgi/* /etc/uwsgi/apps-enabled/
  $ sudo ln -s /path/to/here/conf/nginx/* /etc/nginx/sites-enabled/
  $ sudo /etc/init.d/nginx/reload
  $ sudo /etc/init.d/uwsgi/reload

This can be restarted with::

  $ touch touch-to-reload

Credit
------

Thanks to my briliant and hard-working colleague, Mel Melitpolski, for his
unrelenting enthusiasm and support in this project.
