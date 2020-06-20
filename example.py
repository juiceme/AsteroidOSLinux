#! /usr/bin/env python3

import argparse
import asteroid
import asteroid.app
from asteroid.module import *

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", "--interactive",
    action="store_true",
    help="Drop to IPython shell instead of GLib event loop"
)
parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="More verbose output"
)

args = parser.parse_args()

ADDRESS = "20:70:02:A0:1F:AC"
OWM_KEY = ""
OWM_LOCATION = ""

app = asteroid.app.App(ADDRESS, verbose=args.verbose)

app.register_module(ReconnectModule(timeout_base=10))
app.register_module(TimeSyncModule())
app.register_module(JModule())
app.register_module(NotifyModule())
app.register_module(OWMModule(api_key=OWM_KEY, location=OWM_LOCATION))
app.register_module(MPDModule())

if args.interactive:
    import IPython
    IPython.embed()
else:
    app.run()
