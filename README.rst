Running httpbin over HTTP/3
===========================

This document explains how to run `httpbin` over HTTP/3 using `aioquic`_ and `hypercorn`_.

You will need Python 3.7 or better.

Install requirements:

.. code-block:: console

  python3 -m venv venv
  source venv/bin/activate
  pip install asgiref httpbin hypercorn[h3]

Run the server:

.. code-block:: console

  hypercorn --bind [::]:4433 --quic-bind [::]:4433 --certfile ssl_cert.pem --keyfile ssl_key.pem demo:app

.. _aioquic: https://github.com/aiortc/aioquic
.. _hypercorn: https://pgjones.gitlab.io/hypercorn/
