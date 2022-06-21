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
		row['container_release'] = d.name
		row['booking_number'] = d.booking_number
		row['shipping_line'] = d.shipping_line
		row['container_number'] = d.container_number

		row['release_date'] = d.release_date
		row['free_days'] = d.free_days
		row['demmurage_count']= d.demmurage_count

		row['cfs_arrival_date'] = d.cfs_arrival_date
		row['free_days_empty'] = d.free_days_empty
		row['cfs_storage_days']= d.cfs_storage_days

		var_today = getdate(nowdate())
		row['status_days'] = date_diff(var_today, d.release_date)
		
		# Think of adding a warning if status days > 25
		if d.demmurage_count>0 and d.cfs_storage_days>0:
			row['status'] = "Active"
		elif d.demmurage_count < 0 and d.cfs_storage_days < 0:
			row['status'] = "Expired"
		elif d.demmurage_count < 0:
			row['status'] = "Demurrage Expired"
		else:
			row['status'] = "Storage Expired"

		# Status after stuffing, conditions to think about
		# Demurrage Expired & Stuffed Active

		#row['status'] = "Expired" if int(row['status_days']) >= 30 else "Active"
		

		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"container_release",
			"label": "Container Release",
			"fieldtype": "Link",
			"options": "Container Release",
			'width': 150
		},
		{
			"fieldname":"booking_number",
			"label": "Booking Number",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"shipping_line",
			"label": "Shipping Line",
			"fieldtype": "Data",
			'width': 150
		},
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
			"width": 150,
		},
		{
			"fieldname":"free_days",
			"label": "Free Days Given",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"demmurage_count",
			"label": "Remaining Free Demmurage Days",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"cfs_arrival_date",
			"label": "CFS Arrival Date",
			"fieldtype": "Date",
			"width": 150,
		},
		{
			"fieldname":"free_days_empty",
			"label": "Free Days Empty",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"cfs_storage_days",
			"label": "Remaining Free Days",
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

	if filters.booking_no:
		where += ' AND '
		where += 'tr.booking_number LIKE %(booking_no)s'
		
		where_filter.update({"booking_no": filters.booking_no})

	if filters.container_no:
		where += ' AND '
		where += 'tce.container_number LIKE %(container_no)s'
		
		where_filter.update({"container_no": filters.container_no})

	data = frappe.db.sql("""select tce.container_number,
		tr.booking_number, tr.release_date, tr.cfs_storage_days,
		tr.demmurage_count, tr.cfs_arrival_date, tr.name, tr.shipping_line, tr.free_days,
		tr.free_days_stuffed, tr.stuffing_date, tr.free_days_empty

		from `tabContainer Collected` tce
		LEFT JOIN
			`tabContainer Release` tr ON tce.parent = tr.name
		where tr.release_date BETWEEN %(from_date)s AND %(to_date)s
		"""+ where +
		""" order by tr.release_date
		""", where_filter, as_dict=1)
	return data
