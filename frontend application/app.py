from flask import Flask, render_template, request
from jaeger_client import Config
import logging
import time
from opentracing_instrumentation.request_context import get_current_span, span_in_context

from prometheus_client import generate_latest,Summary,Counter,start_http_server,Gauge

app = Flask(__name__)

c = Counter('my_failures', 'This is 400 or 500 errors processing')

with c.count_exceptions():
    c.inc()

g = Gauge('my_inprogress_requests', 'Description of gauge')

with g.track_inprogress():
    g.inc()

s = Summary('request_processing_seconds','Time spent processing request')

with s.time():
    s.observe(100)
    
smry = Summary('request_latency_seconds', 'Description of summary')

with smry.time():
    smry.observe(100)


@app.route('/metrics')
def metrics():
    with tracer.start_span('frontend-metrics',child_of=get_current_span()) as span:
        span.set_tag('Metrics', 'frontend-metrics')
        answer = generate_latest()
        with span_in_context(span):
            span.log_kv({'event': 'frontend-metric' , 'value': answer })
    return answer

#request_latency_seconds
#Description of summary

# Create a metric to track time spent and requests made.
#REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

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
    
#@REQUEST_TIME.time()
@app.route('/')
def homepage():
    with tracer.start_span('frontend') as span:
        span.set_tag('Frontend', 'fronttime.sleepend')
    return render_template("main.html")
    
tracer = init_tracer('frontend')


if __name__ == "__main__":
    app.run()
