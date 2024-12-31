from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


class SSOTokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from rest_framework_simplejwt.tokens import UntypedToken
        token = request.headers.get('Authorization')
        if token:
            try:
                UntypedToken(token)
            except AuthenticationFailed:
                return Response({'error': 'Invalid token'}, status=400)
        response = self.get_response(request)
        return response
