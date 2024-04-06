from datetime import datetime, UTC
from prometheus_client import Gauge
from urllib.request import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RPSMiddleware(BaseHTTPMiddleware):

    """Since prometheus doesn't track requests-per-seconds
        RPSMiddleware can be used to calculates it on the fly
        Nota that the metric is not acurate when few requests arive and the
        time interval between requests is large"""

    def __init__(self, app):
        super().__init__(app)
        self.start_time = datetime.now(UTC)
        self.request_count = 0
        self.rps_counter = Gauge('requests_per_second', 'Requests per second')

    async def dispatch(self, request: Request, call_next):
        self.request_count += 1
        if (datetime.now(UTC) - self.start_time).seconds >= 1:
            self.rps_counter.set(self.request_count)
            self.request_count = 0
            self.start_time = datetime.now(UTC)
        response = await call_next(request)
        return response
