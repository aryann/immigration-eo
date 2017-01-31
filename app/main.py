import os

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
TEMPLATE = JINJA_ENVIRONMENT.get_template(os.path.join('templates', 'index.html'))


class MainPage(webapp2.RequestHandler):

    def get(self):
      template_values = {
      }
      self.response.write(TEMPLATE.render(template_values))


app =  webapp2.WSGIApplication([
    ('/', MainPage),
], debug=False)
