import flask
import os
import gevent
import time 
import random
import math

from gevent.pywsgi import WSGIServer

app = flask.Flask(__name__)

def event():
    while True:
        rand = math.floor(random.random() * 90000)
        if rand == 1:
            ts = time.gmtime()
            yield "data: " + time.strftime("%H-%M-%S", ts) + "\n\n"

@app.route('/sservant', methods=['GET', 'POST'])
def stream():
    """SSE (Server Side Events), for an EventSource. Send
    the event of a new message.

    See Also:
        event()

    """
    print("Received connection. Starting event listener")
    return flask.Response(flask.stream_with_context(event()), mimetype="text/event-stream", headers={'X-Accel-Buffering': 'no'})


if __name__ == '__main__':
   WSGIServer(('', 5000), app).serve_forever()
   #app.threaded = True
   #app.debug = False
   #app.run()


