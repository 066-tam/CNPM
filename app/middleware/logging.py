import time, logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
logger = logging.getLogger("ims")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({time.time()-start:.3f}s)")
        return response
