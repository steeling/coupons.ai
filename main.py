"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
from google.appengine.ext import ndb
import json
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class GenericItem(ndb.Model):
  pass

class Coupon(ndb.Model):
  pass

def default():
  print request.json
  return ''

def store_coupons():
  print request.json
  return ''

@app.route('/', methods=['POST'])
def dispatch():
  req = request.get_json(silent=True, force=True)

  action = dispatch_dict.get(request.json['result']['action'], default)
  return action()

dispatch_dict = {
  'store.coupons': store_coupons,
}



# Helper for us, not part of ai
@app.route('/create/generic/<item>', methods=['POST', 'GET'])
def create_generic(item):
  key = GenericItem(id=item).put()
  collect = []
  for coupon in request.form.get('coupons', []):
    collect.append(coupon(id=coupon, parent=key).put())
  ndb.put_multi(collect)
  return ''