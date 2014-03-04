# -*- coding: utf-8 -*-
"""Installer for the testpyramidtemplate package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='testpyramidtemplate',
    version='0.1',
    description='testpyramidtemplate',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Torkel Lyng',
    author_email='torkel.lyng@gmail.com',
    keywords='Plone Travis-CI',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    paster_plugins=['pyramid'],
    install_requires=[
        'SQLAlchemy',
        'pyramid',
        'pyramid_debugtoolbar',
        'pyramid_tm',
        'transaction',
        'zope.sqlalchemy',
    ],
    extras_require={
        'test': [
            'coverage',
            'flake8',
            'nose',
            'nose-selecttests',
            'unittest2',
            'webtest',
        ],
        'development': [
            'pyramid_debugtoolbar',
            'Sphinx',
            'waitress',
        ],
    },
    entry_points="""\
    [paste.app_factory]
    main = testpyramidtemplate:main
    """,
)
