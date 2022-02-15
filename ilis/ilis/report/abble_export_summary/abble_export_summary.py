# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, today, date_diff, add_days


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		row['bl_number'] = d.bl_number
		row['client'] = d.client
		row['reference_number'] = d.reference_number
		row['transporter'] = d.transporter
		row['drivers_name'] = d.drivers_name
		row['license_number'] = d.license_number


		row['truck'] = d.truck
		row['trailer'] = d.trailer	
		row['loading_place'] = d.loading_place
		row['loading_date'] = d.loading_date
		row['cargo'] = d.cargo
		row['package'] = d.package
		row['amount_per_container'] = d.amount_per_container
		row['laoding_tons'] = d.laoding_tons

		row['nakonde_arrival'] = d.nakonde_arrival
		row['gate_pass_nakonde'] = d.gate_pass_nakonde
		row['tunduma_arrival'] = d.tunduma_arrival
		row['tunduma_departure_date'] = d.tunduma_departure_date

		row['cfs'] = d.cfs
		row['arrival_date'] = d.arrival_date
		row['gate_in_date'] = d.gate_in_date
		row['carry_in_date'] = d.carry_in_date
		row['start_offloading'] = d.start_offloading
		row['end_offloading'] = d.end_offloading

		row['booking_number'] = d.booking_number
		row['shipping_line'] = d.shipping_line
		row['exporter'] = d.exporter
		row['consignee'] = d.consignee
		row['destination'] = d.destination
		row['depot'] = d.depot
		row['stuffing_date'] = d.stuffing_date
		row['yard_departure'] = d.yard_departure
		row['port_charges_date'] = d.port_charges_date
		row['shipping_instruction_date'] = d.shipping_instruction_date

		row['release_date'] = d.release_date
		row['expiry_date'] = add_days(d.release_date, 30)		
		var_today = getdate(nowdate())
		row['free_days'] = date_diff(add_days(d.release_date, 30), var_today)

		row['cfs_arrival_date'] = d.cfs_arrival_date
		row['cfs_expiry_date'] = add_days(d.cfs_arrival_date, 20)
		row['cfs_free_days'] = date_diff(add_days(d.cfs_arrival_date, 20), var_today)
		
		row['cfs'] = d.file_status
		row['file_status'] = d.file_status

		row['container_number'] = d.container_number
		row['pcs'] = d.pcs
		row['aficd_total'] = d.aficd_total
		row['with_container'] = d.with_container
		row['vgm'] = d.vgm
		row['after_balance'] = d.after_balance
		row['scanner_report_confirmation_date'] = d.scanner_report_confirmation_date

		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"bl_number",
			"label": "Bl Number",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"client",
			"label": "Client",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"reference_number",
			"label": "Client Reference No",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"consignee",
			"label": "Consignee",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"container_number",
			"label": "CNT No",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"consignee",
			"label": "Balance",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"consignee",
			"label": "TARE",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"cargo",
			"label": "Cargo",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"stuffing_date",
			"label": "Stuffing Status",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cargo",
			"label": "Custom Release",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"cargo",
			"label": "Loading Permission",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"port_charges_date",
			"label": "Port Charges",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cargo",
			"label": "EBS Received Date",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"shipping_instruction_date",
			"label": "SI Cut-off",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cargo",
			"label": "TICTS Delivery Date",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"vgm",
			"label": "VGM",
			"fieldtype": "float",
			"width": 100,
		},
		{
			"fieldname":"scanner_report_confirmation_date",
			"label": "Scanner Report Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"scanner_report_confirmation_date",
			"label": "Scanner Report Check Person",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"release_date",
			"label": "Container Pickup Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"expiry_date",
			"label": "Container Expiry Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"free_days",
			"label": "Free Days Remaining",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"fieldname":"cfs_arrival_date",
			"label": "Container Gatein CFS",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cfs_expiry_date",
			"label": "Container CFS Expiry",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname":"cfs_free_days",
			"label": "Container CFS Free Days Remaining",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"cfs",
			"label": "CFS ",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname":"file_status",
			"label": "Status",
			"fieldtype": "Data",
			"width": 120,
		},
		# {
		# 	"fieldname":"transporter",
		# 	"label": "Transporter",
		# 	"fieldtype": "Data",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"drivers_name",
		# 	"label": "Driver ",
		# 	"fieldtype": "Data",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"license_number",
		# 	"label": "Driver's License",
		# 	"fieldtype": "Data",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"truck",
		# 	"label": "Truck",
		# 	"fieldtype": "Data",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"trailer",
		# 	"label": "Trailer",
		# 	"fieldtype": "Data",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"loading_place",
		# 	"label": "Loading Place",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"loading_date",
		# 	"label": "Loading Date",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"package",
		# 	"label": "Package",
		# 	"fieldtype": "float",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"amount_per_container",
		# 	"label": "Amount per Conatiner",
		# 	"fieldtype": "float",
		# 	'width': 150
		# },
		# {
		# 	"fieldname":"laoding_tons",
		# 	"label": "Loading Tons",
		# 	"fieldtype": "float",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"nakonde_arrival",
		# 	"label": "Nakonde Arrival",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"gate_pass_nakonde",
		# 	"label": "Gate Pass Nakonde",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"tunduma_arrival",
		# 	"label": "Tunduma Arrival",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"tunduma_departure_date",
		# 	"label": "Tunduma Departure",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"arrival_date",
		# 	"label": "ICD Arrival",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"gate_in_date",
		# 	"label": "Get in Date",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"carry_in_date",
		# 	"label": "Carry in Date ",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"start_offloading",
		# 	"label": "Start offLoading Date",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"end_offloading",
		# 	"label": "End Offloading",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"booking_number",
		# 	"label": "Booking Number",
		# 	"fieldtype": "Link",
		# 	"options": 'Container Release',
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"shipping_line",
		# 	"label": "Shipping Line",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"container_number",
		# 	"label": "Container",
		# 	"fieldtype": "Link",
		# 	"options": "Container",
		# 	'width': 200
		# },
		# {
		# 	"fieldname":"exporter",
		# 	"label": "Exporter",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"exporter",
		# 	"label": "Exporter",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		
		# {
		# 	"fieldname":"destination",
		# 	"label": "Destination",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"depot",
		# 	"label": "Depot",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"yard_departure",
		# 	"label": "ICD Departure",
		# 	"fieldtype": "Date",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"pcs",
		# 	"label": "Pcs per Container",
		# 	"fieldtype": "Data",
		# 	"width": 120,
		# },
		# {
		# 	"fieldname":"aficd_total",
		# 	"label": "AFICD Total(Tons)",
		# 	"fieldtype": "float",
		# 	"width": 120,
		# },
	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select tce.container_number,tce.release_date, 
		ta.bl_number, ta.client, ta.reference_number, ta.transporter, ta.file_status,
		ta.drivers_name, ta.license_number, ta.truck, ta.trailer, ta.loading_place,
		ta.loading_date, ta.cargo, ta.package, ta.amount_per_container, ta.laoding_tons,
		ta.nakonde_arrival, ta.gate_pass_nakonde, ta.tunduma_arrival, ta.tunduma_departure_date,
		ta.cfs, ta.arrival_date, ta.gate_in_date, ta.carry_in_date, ta.start_offloading,
		ta.end_offloading, ta.booking_number, ta.exporter, ta.consignee, ta.destination,
		ta.depot, ta.yard_departure, ta.stuffing_date, ta.port_charges_date,
		ta.pcs, ta.aficd_total, ta.with_container, ta.vgm, ta.shipping_instruction_date,
		ta.after_balance, ta.scanner_report_confirmation_date, tcr.shipping_line,
		tcr.cfs_arrival_date

		from `tabContainer Export` tce
		LEFT JOIN 
			`tabAbble` ta ON tce.parent = ta.name
		LEFT JOIN 
			`tabContainer Release` tcr ON ta.booking_number = tcr.name
		where ta.loading_date BETWEEN %(from_date)s AND %(to_date)s
		order by ta.loading_date
		"""+ where, where_filter, as_dict=1)
	return data
