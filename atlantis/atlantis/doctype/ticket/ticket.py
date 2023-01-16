# Copyright (c) 2023, Finbyz tech pvt plt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from erpnext.accounts.utils import get_fiscal_year, now


class Ticket(Document):
	def validate(self):
		self.opening_date = self.creation
		if self.status == "Resolved":
			self.closure_date_and_time = now()
			opening = datetime.strptime(self.opening_date, '%Y-%m-%d %H:%M:%S.%f')
			close = datetime.strptime(self.closure_date_and_time, '%Y-%m-%d %H:%M:%S.%f')
			sla_calculation = close - opening
			minutes = sla_calculation.total_seconds() / 60
			if minutes:
				self.sla_calculation = minutes
			else:
				self.sla_calculation = sla_calculation.total_seconds() / 60 / 60
