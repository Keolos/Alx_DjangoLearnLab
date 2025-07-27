from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    """
    Middleware that enforces Content Security Policy (CSP) headers
    using the CSP_* settings defined in settings.py.
    """

    def process_response(self, request, response):
        csp_policies = {
            "default-src": settings.CSP_DEFAULT_SRC,
            "style-src": settings.CSP_STYLE_SRC,
            "script-src": settings.CSP_SCRIPT_SRC,
        }
        csp_header = "; ".join([f"{k} {v}" for k, v in csp_policies.items()])

        response["Content-Security-Policy"] = csp_header
        return response
