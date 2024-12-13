import time
from typing import Any
from app.settings import logger


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request) -> Any:
        if request.path == '/health/':
            response = self.get_response(request)
            if response.status_code != 200:
                logger.error(f'Health check failed: {response.content}')
                return response

        logger.info(f'Method: {request.method}; Path: {request.get_full_path()}; Body: {request.body}')
        t0 = time.perf_counter()
        response = self.get_response(request)
        logger.info(f"Time taken: {time.perf_counter() - t0:.2f}s")
        return response