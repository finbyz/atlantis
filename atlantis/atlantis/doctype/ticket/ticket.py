# Copyright (c) 2023, Finbyz tech pvt plt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from erpnext.accounts.utils import get_fiscal_year, now
import json
from frappe.utils import (
	time_diff_in_seconds,
)


class Ticket(Document):
	def validate(self):
		self.opening_date = self.creation
	def on_submit(self):
		if self.status == "Resolved" and not self.sla_calculation:
			self.set_resolution_time()
	def on_update_after_submit(self):
		if self.status == "Resolved" and not self.sla_calculation:
			self.set_resolution_time()
	def set_resolution_time(self):
		# total time taken from issue creation to closing
		resolution_time = time_diff_in_seconds(self.closure_date_and_time, self.creation)
		self.db_set("sla_calculation", resolution_time)


@frappe.whitelist()
def set_multiple_status(names, status):
	names = json.loads(names)
	for name in names:
		set_status(name, status)



@frappe.whitelist()
def set_status(name, status):
	st = frappe.get_doc("Ticket", name)
	st.status = status
	st.save()

def set_violation_time():
	from frappe.utils import (
	time_diff_in_seconds,
	)
	from erpnext.accounts.utils import get_fiscal_year, now
	ticket_list = frappe.get_list("Ticket" , {'status':["!=" , "Resolved"] , 'docstatus' :1 } , pluck="name")
	for row in ticket_list:
		opening_date = frappe.db.get_value('Ticket', row ,'opening_date')
		violation_time = time_diff_in_seconds(now() , opening_date )
		if violation_time > 7200:
			print(violation_time)
			frappe.db.set_value('Ticket' , row , 'violation' , violation_time ,update_modified= False)