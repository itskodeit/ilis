// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Container Booking', {
	refresh: function(frm) {
		if(frm.doc.docstatus == 1){
			cur_frm.add_custom_button(__('Container Release'), function(){
				frappe.model.open_mapped_doc({
					method: "ilis.ilis.doctype.container_booking.container_booking.make_container_release",
					frm: cur_frm
				})
			}, __('Create'));
			
		}
	},
	
});

cur_frm.cscript['Make Container Release'] = function() {
	frappe.model.open_mapped_doc({
		method: "ilis.ilis.doctype.container_booking.container_booking.make_container_release",
		frm: cur_frm
	})
}

/*if(!doc.auto_repeat) {
				cur_frm.add_custom_button(__('Subscription'), function() {
					erpnext.utils.make_subscription(doc.doctype, doc.name)
				}, __('Create'))
			}*/

/*if(frm.doc.docstatus == 1){
			cur_frm.add_custom_button(__('Collect Container'), function(){
				cur_frm.cscript.make_container_release }, __('Create'));
			
}*/