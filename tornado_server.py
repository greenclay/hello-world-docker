import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web
import tornado.websocket
import logging

import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render('templates/index.html')
        self.write('hello world')

class Application(tornado.web.Application):
    def __init__(self):
        # debug = (tornado.options.options.environment == "dev")

        # if get_env_variable('edyzaapi_env') == 'development':
        #     debug = True
        # elif get_env_variable('edyzaapi_env') == 'production':
        #     debug = False
        debug = True
        app_settings = {
            'debug': debug,
            # 'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        }
        # static_path = os.path.join(os.path.dirname(__file__), 'static')
        handlers = [
            (r'/', IndexHandler),
            ]

        tornado.web.Application.__init__(self, handlers, **app_settings)

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Enviroment variable not found: Set the %s environment variable" % var_name
        raise KeyError(error_msg)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    port = int(os.environ.get('PORT', 80))
    tornado.options.parse_command_line()
    logging.info('starting tornado server on port: ' + str(port))
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()
