import webapp2
import os
import mimetypes
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))


class Evacuspots (webapp2.RequestHandler):
    def get (self):
        self.response.headers["Content-Type"]="application/json"
        path = os.path.join(os.path.dirname(__file__),'evacuspots.geojson')
        self.response.out.write(template.render(path,{}))
        


app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/api/evacuspots', Evacuspots),
], debug=True)



