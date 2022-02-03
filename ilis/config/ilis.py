from frappe import _


def get_data():
	return [
		{
			"module_name": "ilis",
			"label": _("Import & Export"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Booking",
					"route": "#List/Booking",
					"description": _("Import & Export File."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Abble",
					"route": "#List/Abble",
					"description": _("Import & Export File."),
					"onboard": 1,
				},
				
			]
		},
		{
			"module_name": "ilis",
			"label": _("Reports"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sample Report 1",
					"doctype": "Abble"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Container Lifespan Report",
					"doctype": "Container"
				},
				
			]
		}
	]
