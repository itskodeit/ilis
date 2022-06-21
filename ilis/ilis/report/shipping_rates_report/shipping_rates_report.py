# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		
		row['shipping_line'] = d.shipping_line
		row['port_of_loading'] = d.port_of_loading
		row['destination'] = d.destination
		row['rate'] = d.rate
		row['valid'] = d.valid
		row['last_updated_on'] = d.modified
		row['last_updated_by'] = d.modified_by		


		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"shipping_line",
			"label": "Shipping Line",
			"fieldtype": "Link",
			"options": "Shipping Line",
			'width': 150
		},
		{
			"fieldname":"port_of_loading",
			"label": "From ",
			"fieldtype": "Link",
			"options": "Port",
			'width': 150
		},
		{
			"fieldname":"destination",
			"label": "Destination",
			"fieldtype": "Link",
			"options": "Port",
			"width": 120,
		},
		
		{
			"fieldname":"rate",
			"label": "Rate ($)",
			"fieldtype": "Currency",
			'width': 150
		},
		{
			"fieldname":"valid",
			"label": "Valid Till",
			"fieldtype": "Date",
			'width': 150
		},
		{
			"fieldname":"last_updated_on",
			"label": "Last Updated On",
			"fieldtype": "Date",
			'width': 150
		},
				{
			"fieldname":"last_updated_by",
			"label": "Last Updated By",
			"fieldtype": "Data",
			'width': 200
		},

	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select
		ta.shipping_line, ta.port_of_loading, ta.destination, ta.rate, ta.valid,
		ta.modified_by, ta.modified
		
		from `tabShipping Rate` ta
		where ta.modified BETWEEN %(from_date)s AND %(to_date)s
		AND ta.docstatus !=2
		order by ta.modified
		"""+ where, where_filter, as_dict=1)
	return data
