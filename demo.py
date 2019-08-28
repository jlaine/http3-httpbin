import httpbin

from wsgi import WsgiToAsgi

app = WsgiToAsgi(httpbin.app)
