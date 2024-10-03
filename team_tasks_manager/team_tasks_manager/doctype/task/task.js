// Copyright (c) 2024, Rahul Sarkar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Task", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Task', {
//     refresh: function(frm) {
//         if(frm.doc.status !== "Completed") {
//             frm.add_custom_button(__('Update Status'), function() {
//                 let next_status = frm.doc.status === "Open" ? "In Progress" : "Completed";
//                 frm.set_value('status', next_status);
//                 frm.save();
//             });
//         }
//     }
// });
