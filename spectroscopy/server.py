#!/bin/python3

import random
import string
import os
import os.path
import cherrypy
from argparser import parser

RELATIVE_PATH = '/front/build'

args = parser.parse_args()


class StaticGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('.{}/index.html'.format(RELATIVE_PATH))


@cherrypy.expose
@cherrypy.tools.json_in()
@cherrypy.tools.json_out()
class SpectroscopyRest(object):

    def GET(self):
        return cherrypy.session.get('mystring')

    def POST(self):
        length = cherrypy.request.json['length']
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    print(os.path.abspath(os.getcwd()))
    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd() + RELATIVE_PATH),
            'tools.staticdir.dir': ''
        },
        '/api': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    webapp = StaticGenerator()
    webapp.api = SpectroscopyRest()
    cherrypy.quickstart(webapp, '/', conf)
