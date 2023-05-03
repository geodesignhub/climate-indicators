import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    serviceurl = "http://local.test:8000/api/v1/"



apisettings = {
  "serviceurl": "http://local.test:8000/api/v1/",
  # "serviceurl": "https://www.geodesignhub.com/api/v1/",
}
