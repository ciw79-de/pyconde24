from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import webbrowser


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))


class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.path = "/slides.html"
        return super().do_GET(self)


class SlideRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_response()
        print(self.path)
        file_name = "/home/christian/git/pyconde24/slides" + self.path
        with open(file_name, "rb") as file:
            self.wfile.write(file.read())


def run(server_class=HTTPServer, handler_class=SlideRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


print("Starting web server on port 8000")
# TODO: Open this after the web server is started - maybe in a thread
webbrowser.open("http://localhost:8000/slides.html", new=2)
run()
print("Stopping web server")
