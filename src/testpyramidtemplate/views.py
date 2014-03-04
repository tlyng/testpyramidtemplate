# -*- coding: utf-8 -*-
"""Application's views."""

from pyramid.renderers import get_renderer
from pyramid.view import view_config


def main_template():
    return get_renderer('testpyramidtemplate:templates/main_template.pt').implementation()


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    """The home page."""
    return {
        'main': main_template(),
        'name': 'testpyramidtemplate',
    }
