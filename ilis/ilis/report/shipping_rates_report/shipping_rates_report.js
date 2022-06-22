// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt
/* eslint-disable */

var aday = new Date();
var to_date = aday.toISOString().split('T')[0];
aday.setDate(aday.getDate() - 30);
var from_date = aday.toISOString().split('T')[0];
var cur_report = null;


frappe.query_reports["Shipping Rates Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": from_date,
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": to_date
		},
/*		{
			"fieldname":"booking_no",
			"label": __("Booking Number"),
			"fieldtype": "Data",
			"width": "100"
		},
		{
			"fieldname":"container_no",
			"label": __("Container"),
			"fieldtype": "Data",
			"width": "100"
		},*/
	]
};
