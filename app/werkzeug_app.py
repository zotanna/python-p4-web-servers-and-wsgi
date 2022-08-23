#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=4000,
        application=application
    )
