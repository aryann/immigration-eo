import collections
import csv
import httplib
import logging
import os

import jinja2
import webapp2

from google.appengine.api import urlfetch

import models

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

NUM_SIGNATURES_URL = (
    'https://docs.google.com/spreadsheets/d/'
    '17jz1v4DusIRhtQYhkvelHq1oJlsFSBat5aSb0cHNQ2k/'
    'pub?gid=1523619827&single=true&output=csv')
NUM_SIGNATURES_FALLBACK = 4700  # We have at least this many signatures.
SIGNATURE_COUNT_FETCH_DEADLINE_SECS = 5


def get_signatures_from_file():
  """Returns Signature objects from a CSV file, and groups them into triplets,
  so we can display three signatures per row.

  For now this is unused.
  """
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

  return signatures


class MainPage(webapp2.RequestHandler):

    def get(self):
      template_values = {
          'num_signatures': '{:,}'.format(models.SignatureCount.get_count()),
      }
      self.response.write(HOME_TEMPLATE.render(template_values))


class AboutPage(webapp2.RequestHandler):

  def get(self):
    template_values = {
        'num_signatures': '{:,}'.format(models.SignatureCount.get_count()),
    }
    self.response.write(ABOUT_TEMPLATE.render(template_values))


class UpdateSignatureCount(webapp2.RequestHandler):

  def get_num_signatures(self):
    num_signatures = NUM_SIGNATURES_FALLBACK
    try:
      result = urlfetch.fetch(
          NUM_SIGNATURES_URL, deadline=SIGNATURE_COUNT_FETCH_DEADLINE_SECS)
      if result.status_code == httplib.OK:
        try:
          num_signatures = int(result.content)
        except ValueError:
          logging.error('Could not parse contents as int: %s', result.content)
    except urlfetch.Error as e:
      logging.error('Could not fetch number of signatures: %s', e)
    return num_signatures

  def get(self):
    latest_count = self.get_num_signatures()
    models.SignatureCount.update(latest_count)


app =  webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage),
    ('/tasks/update_signature_count', UpdateSignatureCount),
], debug=False)
