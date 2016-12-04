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


class Evacuspot(webapp2.RequestHandler):
    def get(self, spot_id):
        self.response.write('This is the Evacuspot. '
            'The Evacuspot id is %s' % spot_id)
        


app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/api/evacuspots', Evacuspots),
    (r'/api/evacuspots/(\d+)', Evacuspot),
], debug=True)



