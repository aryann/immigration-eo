import logging

from google.appengine.ext import ndb

_SIGNATURE_COUNT_KEY = 'SignatureCount'


class SignatureCount(ndb.Model):
  time_updated = ndb.DateTimeProperty(auto_now=True)
  count = ndb.IntegerProperty()

  @classmethod
  @ndb.transactional
  def update(cls, latest_count):
    entity = cls.get_or_insert(_SIGNATURE_COUNT_KEY, count=latest_count)
    logging.info('Latest number of signatures: %d; current count: %d',
                 latest_count, entity.count)
    if latest_count > entity.count:
      entity.count = latest_count
      entity.put()
      logging.info('Number of signatures will be updated.')
    else:
      logging.info('No need to update number of signatures.')

  @classmethod
  def get_count(cls):
    entity =ndb.Key(cls, _SIGNATURE_COUNT_KEY).get()
    if entity:
      return entity.count
    else:
      logging.error(
          "We don't have a signature count yet. Invoke the "
          'tasks/update_signature_count endpoint manually if you are '
          'developing locally.')
      return 0
