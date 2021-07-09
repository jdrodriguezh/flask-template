import unittest
from flask import Flask
from app.main.routes import main_api
from app import create_app

test_app = create_app()
test_app.register_blueprint(main_api, name="test_main_api")


class TestMainBlueprint(unittest.TestCase):
  def setUp(self):
      # happens before each test
      self.app = test_app.test_client()

  def tearDown(self):
      # happens after each test
      return

  def test_home_route(self):
    resp = self.app.get("/")
    self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
  unittest.main()
