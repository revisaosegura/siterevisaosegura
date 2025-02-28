from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == "revisaosegura.com.br":
            return HttpResponsePermanentRedirect("https://www.revisaosegura.com.br" + request.get_full_path())
        return self.get_response(request)
