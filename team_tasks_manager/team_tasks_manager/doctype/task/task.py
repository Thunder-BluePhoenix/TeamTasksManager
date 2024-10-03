# Copyright (c) 2024, Rahul Sarkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Task(Document):
    def after_insert(self):
        self.send_assignment_email()

    def send_assignment_email(self):
        subject = f"New Task Assigned: {self.task_name}"
        message = f"You have been assigned a new task:\n\nTask: {self.task_name}\nDue Date: {self.due_date}\nPriority: {self.priority}\n\nPlease log in to the system to view more details."
        
        frappe.sendmail(
            recipients=[self.assigned_to],
            subject=subject,
            message=message
        )



@frappe.whitelist()
def get_user_teams():
    user = frappe.session.user
    if user == "Guest":
        return []

    # Query the Team Members child table to get the teams the user is part of
    teams = frappe.db.sql("""
        SELECT parent AS team_name
        FROM `tabTeam Members`
        WHERE team_members = %s
    """, (user,), as_dict=True)

    # Return the list of team names
    return [team['team_name'] for team in teams]


