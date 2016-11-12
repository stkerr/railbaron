from payoffdata import payoffs

import flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def indexpage():
    cities = payoffs.keys()
    cities.sort()

    info = {}
    info['cities'] = cities

    return flask.render_template('index.html', info=info)

@app.route("/<start>/<end>")
def destinationpage(start=None, end=None):
    error = None
    try:
        cities = payoffs.keys()
        cities.sort()

        start_index = cities.index(start)
        end_index = cities.index(end)
        payoff = payoffs[cities[start_index]][end_index]

        print 'start is: %s' % start
        print 'end is: %s' %  end
        print 'payoff is: %s' % payoff

        info = {}
        info['cities'] = cities
        info['start'] = start
        info['end'] = end
        info['payoff'] = payoff
        
        return flask.render_template('index.html', info=info)
    except Exception as e:
        import sys,os
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
        return 'Invalid choices.'

if __name__ == "__main__":
    app.run()
