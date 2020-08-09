"""
Usage:
    server.py PORT
"""

from docopt import docopt

args = docopt(__doc__)

from aiohttp import web
from hello_world.app import app

web.run_app(app, port = int(args['PORT']))
