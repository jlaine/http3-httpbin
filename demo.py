import httpbin
from asgiref.wsgi import WsgiToAsgi

app = WsgiToAsgi(httpbin.app)
