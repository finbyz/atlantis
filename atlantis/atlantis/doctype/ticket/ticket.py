# Copyright (c) 2023, Finbyz tech pvt plt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from erpnext.accounts.utils import get_fiscal_year, now
import json
from frappe.utils import (
	add_to_date,
	cint,
	date_diff,
	get_datetime,
	get_time,
	get_weekdays,
	getdate,
	now_datetime,
	time_diff_in_seconds,
)


class Ticket(Document):
	def validate(self):
		self.opening_date = self.creation
	def on_submit(self):
		if self.status == "Resolved" and not self.sla_calculation:
			self.closure_date_and_time = now()
			opening = datetime.strptime(self.opening_date, '%Y-%m-%d %H:%M:%S.%f')
			close = datetime.strptime(self.closure_date_and_time, '%Y-%m-%d %H:%M:%S.%f')
			sla_calculation = close - opening
			minutes = sla_calculation.total_seconds() / 60
			if minutes:
				self.sla_calculation = minutes
			self.set_resolution_time()
	def on_update_after_submit(self):
		if self.status == "Resolved" and not self.sla_calculationI:
			self.closure_date_and_time = now()
			opening = datetime.strptime(self.opening_date, '%Y-%m-%d %H:%M:%S.%f')
			close = datetime.strptime(self.closure_date_and_time, '%Y-%m-%d %H:%M:%S.%f')
			sla_calculation = close - opening
			minutes = sla_calculation.total_seconds() / 60
			if minutes:
				self.sla_calculation = minutes
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

