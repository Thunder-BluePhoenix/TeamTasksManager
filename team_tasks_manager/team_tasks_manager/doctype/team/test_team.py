# Copyright (c) 2024, Rahul Sarkar and Contributors
# See license.txt

# import frappe
# from frappe.tests.utils import FrappeTestCase


# class TestTeam(FrappeTestCase):
# 	pass

import frappe
import unittest
import random

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team_name = f"Development Team {random.randint(1000, 9999)}"
        
        self.team = frappe.get_doc({
            'doctype': 'Team',
            'team_name': self.team_name,
            'description': 'Team responsible for development',
            'team_members': []
        }).insert()

    def tearDown(self):
        frappe.delete_doc('Team', self.team.name)

    def test_team_creation(self):
        self.assertTrue(frappe.db.exists('Team', self.team.name))

    def test_team_name_unique(self):
        with self.assertRaises(frappe.DuplicateEntryError):
            duplicate_team = frappe.get_doc({
                'doctype': 'Team',
                'team_name': self.team_name
            }).insert()

if __name__ == '__main__':
    unittest.main()
