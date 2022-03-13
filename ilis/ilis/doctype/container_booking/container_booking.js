// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Container Booking', {
	refresh: function(frm) {
		if(frm.doc.docstatus == 1){
			cur_frm.add_custom_button(__('Collect Container'), cur_frm.cscript.make_container, __('Create'));
		}
	},
	
});
