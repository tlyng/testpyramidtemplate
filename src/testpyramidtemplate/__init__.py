# -*- coding: utf-8 -*-
"""Initializer."""

from testpyramidtemplate.models import DBSession
from testpyramidtemplate.models import RootFactory
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import notfound_view_config
from sqlalchemy import engine_from_config


@notfound_view_config()
def notfound(request):
    return render_to_response('templates/404.pt', {})


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    session_factory = UnencryptedCookieSessionFactoryConfig(
        settings.get('session.secret', 'secret'),
    )

    authentication_policy = AuthTktAuthenticationPolicy(
        secret=settings.get('authtkt.secret', 'secret'),
        hashalg='sha512',
    )
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        root_factory=RootFactory,
        authentication_policy=authentication_policy,
        authorization_policy=authorization_policy,
        session_factory=session_factory,
    )

    # routing
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
