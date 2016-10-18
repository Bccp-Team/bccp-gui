"""
Usage:
    bccp_gui --host=ip --port=p --bccp=srv
"""

from docopt import docopt
from flask import Flask

app = Flask(__name__)

from bccp_gui import views
from bccp_gui import namespace
from bccp_gui import batch
from bccp_gui import run
from bccp_gui import runner
from bccp_gui import api

import bccp_gui

def main():
    args = docopt(__doc__)
    api.start_api(args['--bccp'])
    bccp_gui.app.run(host=args['--host'], port=int(args['--port']))

if __name__ == "__main__":
    main()
