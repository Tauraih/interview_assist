from django.utils.deprecation import MiddlewareMixin


class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Adding WebSocket and Google Fonts to the CSP
        csp_policy = (
            "default-src 'self'; "
            # "connect-src 'self' ws://localhost:8101 wss://derivapp.maputsa.co.za ws://derivapp.maputsa.co.za wss://ws.derivws.com; "  # Include your WebSocket server
            "style-src 'self' 'unsafe-inline' data: https://cdn.jsdelivr.net https://unpkg.com https://fonts.googleapis.com; "
            "font-src 'self' data: https://fonts.gstatic.com; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://unpkg.com https://fonts.googleapis.com; "
            "img-src 'self' https://trusted-images-source.com data: https://some-cdn.com; "
        )
        response['Content-Security-Policy'] = csp_policy
        return response