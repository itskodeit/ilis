// Copyright (c) 2022, Ikode-IT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Abble', {
	refresh: function(frm) {
		frm.add_custom_button(__("Get Containers"), function() {
            show_sinv_dialog(frm);
        })

        frm.fields_dict["export_container"].grid.add_custom_button(__('Get Containers'), 
			function() {
				//frappe.msgprint(__("GetCo"));
				show_sinv_dialog(frm);
        });
        //frm.fields_dict["export_container"].grid.grid_buttons.find('.btn-custom').removeClass('btn-default').addClass('btn-primary');


	},

	setup: function(frm){
		frm.set_query("container_number", "containers_on_truck", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','status','=', 'Available'],
				]
			}
		});

		frm.set_query("container_number", "export_container", function(doc, cdt, cdn){
			let row = locals[cdt] [cdn]
			return {
				filters: [
					['Container','status','=', 'Available'],
					//['Container Release','booking_number','=', doc.booking_number],
				]
			}
		});
	},

	stuffing_date: function(frm) {
		var aday = new Date();
		var to_date = aday.toISOString().split('T')[0];
		frm.set_value("storage_days", frappe.datetime.get_day_diff( frappe.datetime.add_days(frm.doc.stuffing_date, 20), to_date));
		//frm.set_value("storage_days", frappe.datetime.get_day_diff( to_date , frm.doc.stuffing_date));
		refresh_field(frm.doc.storage_days);
	},
});


function show_sinv_dialog(frm) {
   frappe.prompt([
      {'fieldname': 'booking_number', 'fieldtype': 'Link', 'label': 'Container Release', 'reqd': 1, 'options': 'Container Release'}  
   ],
   function(booking_number){
      console.log(booking_number.booking_number);
      get_items_from_sinv(booking_number.booking_number);
   },
   'Get Containers from Release',
   'Get Containers'
  )
}

function get_items_from_sinv(booking_number) {
  frappe.call({
    "method": "frappe.client.get",
    "args": {
        "doctype": "Container Release",
        "name": booking_number
    },
    "callback": function(response) {
         // add items to your child table
         var sinv = response.message;
         sinv.containers_released.forEach(function (item) {
             var child = cur_frm.add_child('export_container');
             frappe.model.set_value(child.doctype, child.name, 'container_number', item.container_number);
             frappe.model.set_value(child.doctype, child.name, 'release_date', item.release_date);
         });
         cur_frm.refresh_field('export_container');
     }
   });
}