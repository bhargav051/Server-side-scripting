# Copyright (c) 2024, Bhargav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class information(Document):
	def validate(self):
		if self.check and self.first_name and self.last_name:
			self.full_name = f"{self.first_name or ''} {self.last_name or ''}"
		else:
			self.full_name = f""


