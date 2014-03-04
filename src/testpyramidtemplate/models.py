# -*- coding: utf-8 -*-
"""Define models."""

from pyramid.security import Allow
from pyramid.security import Everyone
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    """A class representing a User."""

    __tablename__ = 'users'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    username = Column(
        String,
        unique=True,
        nullable=False,
    )
    email = Column(
        String,
        unique=True,
        nullable=True,
    )
    fullname = Column(
        Unicode(200),
        nullable=True,
    )

    @classmethod
    def get(self, username):
        """Get a User by username."""
        session = DBSession()
        result = session.query(User).filter_by(username=username)
        if result.count() < 1:
            return None

        return result.one()

    @classmethod
    def get_all(class_, order_by='fullname', filter_by=None):
        """Return all users.

        filter_by: dict -> {'name': 'foo'}

        By default, order by User.fullname.
        """
        User = class_
        q = DBSession.query(User)
        q = q.order_by(getattr(User, order_by))
        if filter_by:
            q = q.filter(filter_by)
        return q


class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
    ]

    def __init__(self, request):
        pass  # pragma: no cover
