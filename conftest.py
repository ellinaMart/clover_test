import pytest
from fixture.application import Application
import json
import os

fixture = None

@pytest.fixture(scope = "session")
def app(request):
  global fixture
  with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
    config  = json.load(config_file)
  if fixture is None:
    fixture = Application(browser="firefox", base_url = config['baseUrl'])
  request.addfinalizer(fixture.destroy)
  return fixture

