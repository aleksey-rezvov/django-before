django-before, before django project
====================================

django-before - tools that are needed BEFORE any others in each django project.

subpather
---------
make_subpather - tool to calculate relative paths from root directory.

.. code-block:: python

    # at the beginning of settings.py
    from django_before import make_subpather

    # e.g. I have project structure where this file is here: project_root/src/django_project/settings/base.py
    # so root of my project is 4 levels higher:
    subroot = make_subpather(__file__, 4)

    # know I can handy get paths relative to root of the project:
    MEDIA_ROOT = subroot('static_content/media/')

    DIR_SAMPLE_IMAGES = subroot('src/crm/res/sample_images')

json settings reader
-------------------------
make_json_settings_reader - tool to read settings from json file (e.g. secret settings).

.. code-block:: python

    # create settings reader
    secrets = make_json_settings_reader(subroot('conf/secrets.json'))

    # use it for reading settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mydbname',
            'USER': 'mydbuser',
            'PASSWORD': secrets['DATABASE_PASSWORD'],
        }
    }

    SECRET_KEY = secrets['SECRET_KEY']


Data in json file must be represented as dict:

.. code-block:: json

    {
      "SECRET_KEY": "user123",
      "DATABASE_PASSWORD": "user123"
    }
