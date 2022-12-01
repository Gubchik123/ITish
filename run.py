from gevent.pywsgi import WSGIServer

import app.views
import app.extensions

from app import app


if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 5000), app)
    http_server.serve_forever()
