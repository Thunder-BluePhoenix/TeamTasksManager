# Copyright (c) 2024, Rahul Sarkar and Contributors
# See license.txt

# import frappe
# from frappe.tests.utils import FrappeTestCase


# class TestTask(FrappeTestCase):
# 	pass

import frappe
import unittest
import random

class TestTask(unittest.TestCase):

    def setUp(self):
        self.team_name = f"Development Team {random.randint(1000, 9999)}"

        self.team = frappe.get_doc({
            'doctype': 'Team',
            'team_name': self.team_name,
            
        }).insert()        

        self.task = frappe.get_doc({
            'doctype': 'Task',
            'task_name': f"Finished Backend API {random.randint(1000, 9999)}",
            'assigned_to': frappe.session.user,
            'due_date': '2024-12-31',
            'status': 'Open',
            'priority': 'High',
            'team': self.team.name
        }).insert()

    def tearDown(self):
        frappe.delete_doc('Task', self.task.name)
        frappe.delete_doc('Team', self.team.name)

    def test_task_creation(self):
        self.assertTrue(frappe.db.exists('Task', self.task.name))

    def test_task_assignment(self):
        self.assertEqual(self.task.assigned_to, frappe.session.user)

if __name__ == '__main__':
    unittest.main()



