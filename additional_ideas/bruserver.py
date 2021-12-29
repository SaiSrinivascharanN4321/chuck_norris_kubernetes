from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import pickle
from storageserver import storageserver
import random


jokes = pickle.load(open("jokes.dat", "rb"))
i = random.randint(0, 5)


class hellohandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith(''):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>'
            output += jokes[i]['value']
            output += '</h1>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        # self.send_response(200)
        #self.send_header('content-type', 'text/html')
        # self.end_headers()
        # self.wfile.write('mandelbrot_img.png'.encode())


def main():
    PORT = 8080
    server = HTTPServer(('', PORT), hellohandler)
    print('server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
