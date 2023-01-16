# Copyright (c) 2023, Finbyz tech pvt plt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from erpnext.accounts.utils import get_fiscal_year, now
import json


class Ticket(Document):
	def validate(self):
		self.opening_date = self.creation
		if self.status == "Resolved":
			self.closure_date_and_time = now()
			opening = datetime.strptime(self.opening_date, '%Y-%m-%d %H:%M:%S.%f')
			close = datetime.strptime(self.closure_date_and_time, '%Y-%m-%d %H:%M:%S.%f')
			sla_calculation = close - opening
			frappe.msgprint(str(sla_calculation.total_seconds()))
			minutes = sla_calculation.total_seconds() / 60
			if minutes:
				self.sla_calculation = minutes
	def on_update_after_submit(self):
		if self.status == "Resolved":
			self.closure_date_and_time = now()
			opening = datetime.strptime(self.opening_date, '%Y-%m-%d %H:%M:%S.%f')
			close = datetime.strptime(self.closure_date_and_time, '%Y-%m-%d %H:%M:%S.%f')
			sla_calculation = close - opening
			frappe.msgprint(str(sla_calculation.total_seconds()))
			minutes = sla_calculation.total_seconds() / 60
			if minutes:
				self.sla_calculation = minutes

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