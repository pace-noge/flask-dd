import time

from datadog import initialize, statsd

options = {
    "statsd_host": "127.0.0.1",
    "statsd_port": 8125
}


initialize(**options)

while(1):
    statsd.increment("example_metric.increment", tags=["environment:flask_dd"])
    statsd.decrement("example_metric.decrement", tags=["environment:flask_dd"])
    time.sleep(10)