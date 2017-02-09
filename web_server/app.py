import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
import tornado.web
from http_handler.index_handler import IndexHandler
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

appHandlers=[
    (r'/',IndexHandler)
]

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers=appHandlers,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
