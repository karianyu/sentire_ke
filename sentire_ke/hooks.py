app_name = "sentire_ke"
app_title = "Sentire Ke"
app_publisher = "karianyu"
app_description = "Sentire KE payroll Customization"
app_email = "karianyuapps@gmail.com"
app_license = "mit"

app_icon = "drag"
app_color = "grey"
app_license = "GNU General Public License (v3)"
required_apps = ["erpnext", "hrms"]

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [               
            ["is_system_generated", "=", 0],
            ["module", "=", "Sentire Ke"],
        ],
    },
    ]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sentire_ke",
# 		"logo": "/assets/sentire_ke/logo.png",
# 		"title": "Sentire Ke",
# 		"route": "/sentire_ke",
# 		"has_permission": "sentire_ke.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sentire_ke/css/sentire_ke.css"
# app_include_js = "/assets/sentire_ke/js/sentire_ke.js"

# include js, css files in header of web template
# web_include_css = "/assets/sentire_ke/css/sentire_ke.css"
# web_include_js = "/assets/sentire_ke/js/sentire_ke.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sentire_ke/public/scss/website"

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
# app_include_icons = "sentire_ke/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sentire_ke.utils.jinja_methods",
# 	"filters": "sentire_ke.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sentire_ke.install.before_install"
# after_install = "sentire_ke.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sentire_ke.uninstall.before_uninstall"
# after_uninstall = "sentire_ke.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sentire_ke.utils.before_app_install"
# after_app_install = "sentire_ke.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sentire_ke.utils.before_app_uninstall"
# after_app_uninstall = "sentire_ke.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sentire_ke.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Purchase Receipt": {
        "on_submit": "sentire_ke.sentire_ke.doctype.api.update_item_price_list.update_item_prices"
    },
    "Purchase Invoice": {
        "on_submit": "sentire_ke.sentire_ke.doctype.api.update_item_price_list.update_item_prices"
    },
    "Item": {
        "before_save": "sentire_ke.sentire_ke.utils.get_tims_hscode.validate_mandatory_hscode"
    },
    "Item Group": {
        "before_save": "sentire_ke.sentire_ke.utils.get_tims_hscode.validate_mandatory_hscode"
    },
    "Customer": {
        "before_save": "sentire_ke.sentire_ke.overrides.customer.validate_customer_kra"
    },
    "Sales Order": {
        "before_submit": "sentire_ke.sentire_ke.overrides.sales_doc.validate_customer_kra"
    },
    "Sales Invoice": {
        "before_submit": "sentire_ke.sentire_ke.overrides.sales_doc.validate_customer_kra"
    },
    "Job Card": {"before_submit": "sentire_ke.sentire_ke.overrides.job_card.before_submit"},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sentire_ke.tasks.all"
# 	],
# 	"daily": [
# 		"sentire_ke.tasks.daily"
# 	],
# 	"hourly": [
# 		"sentire_ke.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sentire_ke.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sentire_ke.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sentire_ke.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sentire_ke.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sentire_ke.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sentire_ke.utils.before_request"]
# after_request = ["sentire_ke.utils.after_request"]

# Job Events
# ----------
# before_job = ["sentire_ke.utils.before_job"]
# after_job = ["sentire_ke.utils.after_job"]

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
# 	"sentire_ke.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

