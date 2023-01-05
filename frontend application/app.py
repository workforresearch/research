from flask import Flask, render_template, request
from jaeger_client import Config
import logging
import time
from opentracing_instrumentation.request_context import get_current_span, span_in_context

from prometheus_client import generate_latest

metric=0
home=0


app = Flask(__name__)

@app.route('/metrics')
def metrics():
    start = time.perf_counter()
    with tracer.start_span('frontend-metrics',child_of=get_current_span()) as span:
        span.set_tag('Metrics', 'frontend-metrics')
        answer = generate_latest()
        with span_in_context(span):
            span.log_kv({'event': 'my_api' , 'value': answer })
    end = time.perf_counter()
    metric = end-start
    latency='#TYPE process_metric_latency guage process_metric_latency '+str(metric)
    answer = generate_latest()+latency.encode('utf-8')
    return answer

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


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


@app.route('/')
def homepage():
    start = time.perf_counter()
    with tracer.start_span('frontend') as span:
        span.set_tag('Frontend', 'frontend')
    end = time.perf_counter()
    home = end-start
    print(home)
    return render_template("main.html")

tracer = init_tracer('frontend')


if __name__ == "__main__":
    app.run()
