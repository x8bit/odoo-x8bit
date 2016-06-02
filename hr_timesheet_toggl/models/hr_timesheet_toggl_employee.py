# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
from openerp import models, fields, api
from TogglPy import Toggl
import logging

class hr_employee_toggl(models.Model):
	#_name = 'hr.employee'
	_inherit = 'hr.employee'

	#fields
	toggl_user_id = fields.Integer(string="Usuario Toggl")

	@api.model
	def getTrackedHours(self, payslip):
		#_logger = logging.getLogger(__name__)
		toggl = Toggl()
		toggl.setAPIKey("83aa5f3cd6854b57221a0df67a366d3a")
		data = {
			'grouping'     : "users",
			'subgrouping'  : "projects",
			'workspace_id' : 709530,
			'since'        : payslip.date_from,
			'until'        : payslip.date_to,
			'order_field'  : "duration",
			'order_desc'   : "on",
			'user_ids'     : self.toggl_user_id,
		}
		response = toggl.getSummaryReport(data)
		return round( response['total_grand'] / 1000.00 / 60.00 /60.00 )