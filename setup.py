from setuptools import setup

setup(name='toutatis',
    version='0.0.1',
    description='OpenShift App',
    packages=['political_memory'],
    package_dir={'political_memory': '.'},
    author='Memopol Team',
    author_email='cortex@worlddomination.be',
    url='http://github.com/political-memory/toutatis/',
    install_requires=[
        'django-representatives-votes[api]>=0.0.13',
        'django-representatives[api]>=0.0.14',
        'django-crispy-forms>=1.6.0,<1.7.0',
        'django>=1.8,<1.9',
        'djangorestframework>=3.3.0,<3.4.0',
        'pytz==2015.7',
    ],
    extras_require={
        'testing': [
            'flake8',
            'pep8',
            'pytest',
            'pytest-django',
            'pytest-cov',
            'codecov',
        ]
    }
)
