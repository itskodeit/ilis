// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Container Release', {
	refresh: function(frm) {
		console.log(frm);
		/*frm.set_value("demmurage_count", frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.release_date, frm.doc.free_days), to_date));
		refresh_field(frm.doc.demmurage_count);*/
	},

	release_date: function(frm) {
		$.each(frm.doc.containers_released || [], function(i, d) {
			if(!d.release_date) d.release_date = frm.doc.release_date;
		});
		refresh_field("containers_released");

		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		console.log("here");
		frm.set_value("demmurage_count", frappe.datetime.get_day_diff( 
			frappe.datetime.add_days(frm.doc.release_date, parseInt(frm.doc.free_days)), to_date));
		refresh_field(frm.doc.demmurage_count);
	},

	free_days: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		
		frm.set_value("demmurage_count", frappe.datetime.get_day_diff( 
			frappe.datetime.add_days(frm.doc.release_date, parseInt(frm.doc.free_days)), to_date));
		refresh_field(frm.doc.demmurage_count);
	},

	cfs_arrival_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("cfs_storage_days", frappe.datetime.get_day_diff( 
				frappe.datetime.add_days(frm.doc.cfs_arrival_date, parseInt(frm.doc.free_days_empty)), to_date));
		refresh_field(frm.doc.cfs_storage_days);
	},
	free_days_empty: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("cfs_storage_days", frappe.datetime.get_day_diff( 
				frappe.datetime.add_days(frm.doc.cfs_arrival_date, parseInt(frm.doc.free_days_empty)), to_date));
		refresh_field(frm.doc.cfs_storage_days);
	},

	stuffing_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("stuffed_counter", 
			frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.stuffing_date, frm.doc.free_days_stuffed), to_date));
		refresh_field(frm.doc.stuffed_counter);
	},
	free_days_stuffed: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("stuffed_counter", 
			frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.stuffing_date, frm.doc.free_days_stuffed), to_date));
		refresh_field(frm.doc.stuffed_counter);
	},


});

frappe.ui.form.on("Container Export", {
	container_number: function(frm,cdt,cdn) {
		var row = locals[cdt][cdn];
		if (frm.doc.release_date) {
			row.release_date = frm.doc.release_date;
			refresh_field("release_date", cdn, "containers_released");
		} else {
			frm.script_manager.copy_from_first_row("containers_released", row, ["release_date"]);
		}
	},
	release_date: function(frm, cdt, cdn) {
		if(!frm.doc.release_date) {
			erpnext.utils.copy_value_in_all_rows(frm.doc, cdt, cdn, "containers_released", "release_date");
		}
	}
});