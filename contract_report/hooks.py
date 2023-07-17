from . import __version__ as app_version

app_name = "contract_report"
app_title = "Contract Report"
app_publisher = "Tech Ventures"
app_description = "this is installation report"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "safdar211@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/contract_report/images/Tech.png"

# Includes in <head>
# ------------------
app_include_css = "/assets/contract_report/css/contract_report.css"
website_context = {
	"favicon": 	"/assets/contract_report/images/Tech.png",
	"splash_image": "/assets/contract_report/images/Tech.png"
}
# include js, css files in header of desk.html
# app_include_css = "/assets/contract_report/css/contract_report.css"
# app_include_js = "/assets/contract_report/js/contract_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/contract_report/css/contract_report.css"
# web_include_js = "/assets/contract_report/js/contract_report.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "contract_report/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "contract_report.utils.jinja_methods",
#	"filters": "contract_report.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "contract_report.install.before_install"
# after_install = "contract_report.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "contract_report.uninstall.before_uninstall"
# after_uninstall = "contract_report.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "contract_report.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"contract_report.tasks.all"
#	],
#	"daily": [
#		"contract_report.tasks.daily"
#	],
#	"hourly": [
#		"contract_report.tasks.hourly"
#	],
#	"weekly": [
#		"contract_report.tasks.weekly"
#	],
#	"monthly": [
#		"contract_report.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "contract_report.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "contract_report.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "contract_report.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["contract_report.utils.before_request"]
# after_request = ["contract_report.utils.after_request"]

# Job Events
# ----------
# before_job = ["contract_report.utils.before_job"]
# after_job = ["contract_report.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"contract_report.auth.validate"
# ]
