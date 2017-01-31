import collections
import csv
import os

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
TEMPLATE = JINJA_ENVIRONMENT.get_template(os.path.join('templates', 'index.html'))
SIGNATURES_FILE = os.path.join(os.path.dirname(__file__), 'signatures.csv')

Signature = collections.namedtuple('Signature', ['name', 'company', 'title'])
SIGNATURES_PER_ROW = 3


class MainPage(webapp2.RequestHandler):

    def get(self):
      signatures = []
      with open(SIGNATURES_FILE) as f:
        reader = csv.reader(f)
        next(reader)  # Skips the header.
        curr = []
        for i, row in enumerate(reader):
          if i != 0 and i % SIGNATURES_PER_ROW == 0:
            signatures.append(curr)
            curr = []
          curr.append(Signature(name=row[0], company=row[1], title=row[2]))

      if not curr:
        signatures.append(curr)

      template_values = {
          'signatures': signatures,
      }
      self.response.write(TEMPLATE.render(template_values))


app =  webapp2.WSGIApplication([
    ('/secretsecret', MainPage),
], debug=False)
