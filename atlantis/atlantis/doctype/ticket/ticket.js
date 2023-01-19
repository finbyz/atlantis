// Copyright (c) 2023, Finbyz tech pvt plt and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket', {
	refresh: function(frm) {
        if(frm.doc.__islocal){
            frm.set_value('agent_name' , frappe.session.user)
        }
    },
    status:function(frm){
        if(frm.doc.status == "Resolved"){
            frappe.model.get_value("User" , frappe.session.user , 'full_name' , (r)=>{
                frm.set_value('closed___by' , r.full_name)
            })
        }
        else{
            frm.set_value('closed___by' , null)
        }
    }  
});
