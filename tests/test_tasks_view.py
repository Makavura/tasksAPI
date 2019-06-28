import json
import unittest
from run import app

from app.views.tasks_view import *


class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

        self.data = {
            "title": "prank",
            "description": "mayengz"
        }

    def test_create_task(self):
        res = self.client.post(
           "/taskMS/api/v1/tasks",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 500)  # test for server error
        self.assertNotEqual(res.status_code, 400)  # test for bad request
        self.assertNotEqual(res.status_code, 403)  # test for forbidden

    def test_create_task_message(self):
        res = self.client.post(
            "/taskMS/api/v1/tasks",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertIn("task created successfully", str(res.data))

    def test_get_tasks(self):
        res = self.client.get(
            "/taskMS/api/v1/tasks",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_task(self, id):
        res = self.client.get(
            "/taskMS/api/v1/tasks/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def teardown(self):
        self.app_context.pop()

    def test_if_requested_task_is_in_tasks(self):
        res = self.client.get(
            "/taskMS/api/v1/tasks",
            headers={"content-type": "application/json"}
        )
        self.assertIn('{"id":"1","title":"prank","description":"mayengz"}',str(res.data))
