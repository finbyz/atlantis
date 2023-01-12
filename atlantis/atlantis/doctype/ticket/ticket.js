// Copyright (c) 2023, Finbyz tech pvt plt and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket', {
	refresh: function(frm) {
        if(frm.doc.__islocal){
            frm.set_value('agent_name' , frappe.session.user)
        }   
    },
});
