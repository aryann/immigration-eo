import collections
import csv
import os

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
HOME_TEMPLATE = JINJA_ENVIRONMENT.get_template('index.html')
ABOUT_TEMPLATE = JINJA_ENVIRONMENT.get_template('about.html')
SIGNATURES_FILE = os.path.join(os.path.dirname(__file__), 'signatures.csv')

Signature = collections.namedtuple('Signature', ['name', 'company', 'title'])
SIGNATURES_PER_ROW = 3


class MainPage(webapp2.RequestHandler):

    def get(self):
      signatures = []
      num_signatories = 0
      with open(SIGNATURES_FILE) as f:
        reader = csv.reader(f)
        next(reader)  # Skips the header.
        curr = []
        for i, row in enumerate(reader):
          num_signatories += 1
          if i != 0 and i % SIGNATURES_PER_ROW == 0:
            signatures.append(curr)
            curr = []
          curr.append(Signature(name=row[0], company=row[1], title=row[2]))

      if not curr:
        signatures.append(curr)

      template_values = {
          'signatures': signatures,
          'num_signatories': '{:,}'.format(num_signatories),
      }
      self.response.write(HOME_TEMPLATE.render(template_values))


class AboutPage(webapp2.RequestHandler):

  def get(self):
    self.response.write(ABOUT_TEMPLATE.render())


app =  webapp2.WSGIApplication([
    ('/secretsecret', MainPage),
    ('/about', AboutPage),
], debug=False)
