import unittest

class TestAcademicTaskTracker(unittest.TestCase):

    def test_add_task(self):
        task = {
            "course": "PF",
            "type": "Assignment",
            "status": "Pending"
        }

        self.assertEqual(task["course"], "PF")
        self.assertEqual(task["type"], "Assignment")
        self.assertEqual(task["status"], "Pending")


    def test_update_status(self):
        task = {
            "course": "PF",
            "status": "Pending"
        }

        task["status"] = "Completed"

        self.assertEqual(task["status"], "Completed")


    def test_delete_task(self):
        tasks = ["PF", "OOP", "DB"]

        tasks.remove("PF")

        self.assertNotIn("PF", tasks)


if __name__ == "__main__":
    unittest.main()