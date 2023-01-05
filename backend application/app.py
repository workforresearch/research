#from turtle import home
from flask import Flask, render_template, request, jsonify

import logging
import pymongo
from flask_pymongo import PyMongo
from jaeger_client import Config
from opentracing_instrumentation.request_context import get_current_span, span_in_context
from prometheus_client import generate_latest
from time import perf_counter

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    with tracer.start_span('backend-metrics',child_of=get_current_span()) as span:
        span.set_tag('Metrics', 'backend-metrics')
        answer = generate_latest()
        with span_in_context(span):
            span.log_kv({'event': 'backend-metrics' , 'value': answer })
    return generate_latest()

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)    
    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )
    return config.initialize_tracer()

tracer = init_tracer('backend-app')



@app.route('/')
def homepage():
    with tracer.start_span('backend-app') as span:
        span.set_tag('Home', 'backend-app')
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    with tracer.start_span('my_api',child_of=get_current_span()) as span:
        span.set_tag('My_api', 'my_api')
        with span_in_context(span):
            span.log_kv({'event': 'my_api' , 'value': answer })
    return jsonify(repsonse=answer)

@app.route('/star', methods=['GET'])
def add_star():
    print(get_current_span())
    with tracer.start_span('my_star',child_of=get_current_span()) as span:
        span.set_tag('My_star','my_star')
        with span_in_context(span):
            span.log_kv({'event': 'my_star' , 'value': output })
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()
