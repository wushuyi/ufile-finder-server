from meinheld import server
from minimal import app
def hello_world(environ, start_response):
    status = '200 OK'
    res = b"Hello world!"
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(res)))]
    start_response(status, response_headers)
    return [res]

server.listen(("0.0.0.0", 5000))
server.run(app)