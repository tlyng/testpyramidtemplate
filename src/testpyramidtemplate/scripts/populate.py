# -*- coding: utf-8 -*-
"""Populate an empty DB."""

from testpyramidtemplate.models import Base
from testpyramidtemplate.models import DBSession
from testpyramidtemplate.models import User
from sqlalchemy import engine_from_config

import os
import sys
import transaction


def main(argv=sys.argv):

    # TODO: check for DB existance etc.? this fails if run more than once
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        sys.stdout.write('DATABASE_URL not set, using default SQLite db.')
        db_url = 'sqlite:///./testpyramidtemplate-app.db'

    settings = {'sqlalchemy.url': db_url}
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        test_user = User(
            username='one',
            email='one@bar.com',
            fullname=u'Test User',
        )
        DBSession.add(test_user)

    sys.stdout.write('DB populated with dummy data: {0}'.format(db_url))


if __name__ == '__main__':
    main()
