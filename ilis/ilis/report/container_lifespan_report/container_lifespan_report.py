# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, today, date_diff


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		row['container_number'] = d.container_number
		row['release_date'] = d.release_date
		
		var_today = getdate(nowdate())
		row['status_days'] = date_diff(var_today, d.release_date)
		
		# Think of adding a warning if status days > 25
		row['status'] = "Expired" if int(row['status_days']) >= 30 else "Active"
		

		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"container_number",
			"label": "Container Number",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"release_date",
			"label": "Release Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"status_days",
			"label": "Status Days",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"status",
			"label": "Container Status",
			"fieldtype": "Data",
			'width': 150
		},
	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select ta.container_number, ta.release_date

		from `tabContainer` ta 
		where ta.release_date BETWEEN %(from_date)s AND %(to_date)s
		order by ta.release_date
		"""+ where, where_filter, as_dict=1)
	return data
