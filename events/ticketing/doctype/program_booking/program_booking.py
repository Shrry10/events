# Copyright (c) 2025, Shreyas Parida and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ProgramBooking(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from events.ticketing.doctype.program_booking_attendee.program_booking_attendee import ProgramBookingAttendee
		from frappe.types import DF

		amended_from: DF.Link | None
		attendees: DF.Table[ProgramBookingAttendee]
		currency: DF.Link
		program: DF.Link
		total_amount: DF.Currency
		user: DF.Link
	# end: auto-generated types

	def validate(self):
		self.set_total()
		self.set_currency()

	def set_currency(self):
		self.currency = self.attendees[0].currency

	def set_total(self):
		self.total_amount = 0.0
		for attendee in self.attendees:
			self.total_amount += attendee.amount

	def on_submit(self):
		self.generate_tickets()

	def generate_tickets(self):
		for attendee in self.attendees:
			ticket = frappe.new_doc("Program Ticket")
			ticket.program = self.program
			ticket.booking = self.name
			ticket.ticket_type = attendee.ticket_type
			ticket.attendee_name = attendee.full_name
			ticket.insert().submit()