app_name = "team_tasks_manager"
app_title = "Team Tasks Manager"
app_publisher = "Rahul Sarkar"
app_description = "Task Management for teams"
app_email = "bluephoenix00995@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "team_tasks_manager",
# 		"logo": "/assets/team_tasks_manager/logo.png",
# 		"title": "Team Tasks Manager",
# 		"route": "/team_tasks_manager",
# 		"has_permission": "team_tasks_manager.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/team_tasks_manager/css/team_tasks_manager.css"
# app_include_js = "/assets/team_tasks_manager/js/team_tasks_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/team_tasks_manager/css/team_tasks_manager.css"
# web_include_js = "/assets/team_tasks_manager/js/team_tasks_manager.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "team_tasks_manager/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "team_tasks_manager/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "team_tasks_manager.utils.jinja_methods",
# 	"filters": "team_tasks_manager.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "team_tasks_manager.install.before_install"
# after_install = "team_tasks_manager.install.after_install"
# after_install = "team_tasks_manager.setup.setup_workflow"

# Uninstallation
# ------------

# before_uninstall = "team_tasks_manager.uninstall.before_uninstall"
# after_uninstall = "team_tasks_manager.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "team_tasks_manager.utils.before_app_install"
# after_app_install = "team_tasks_manager.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "team_tasks_manager.utils.before_app_uninstall"
# after_app_uninstall = "team_tasks_manager.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "team_tasks_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
# doc_events = {
#     "Task": {
#         "validate": "team_tasks_manager.team_tasks_manager.doctype.task.task.validate_team_member"
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"team_tasks_manager.tasks.all"
# 	],
# 	"daily": [
# 		"team_tasks_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"team_tasks_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"team_tasks_manager.tasks.weekly"
# 	],
# 	"monthly": [
# 		"team_tasks_manager.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "team_tasks_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "team_tasks_manager.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "team_tasks_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["team_tasks_manager.utils.before_request"]
# after_request = ["team_tasks_manager.utils.after_request"]

# Job Events
# ----------
# before_job = ["team_tasks_manager.utils.before_job"]
# after_job = ["team_tasks_manager.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"team_tasks_manager.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {"dt": "Workflow", "filters": [["name", "in", ["Task Workflow"]]]},
    {"dt": "Workflow State", "filters": [["name", "in", ["Open", "In Progress", "Completed", "Invalid"]]]},
    {"dt": "Workflow Action Master", "filters": [["name", "in", ["Open", "In Progress", "Completed", "Invalid"]]]},
    {"dt": "Role", "filters": [["name", "in", ["Team Member", "Team Manager"]]]},
    {"dt": "Custom DocPerm", "filters": [["parent", "in", ["Task"]]]},
    # {"dt": "Dashboard", "filters": [["name", "in", ["Team Tasks Overview"]]]},
    # {"dt": "Dashboard Chart", "filters": [["name", "in", ["Tasks per Team", "Task Status Distribution"]]]}
]
