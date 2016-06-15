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
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class project_task_track_button(models.Model):
	#_name = 'hr.employee'
	_name = 'project.task.tracking'

	task_id = fields.Many2one('project.task', string='Task', required=True)
	description = fields.Char(string='Description', required=True)

class project_task_track_time(models.Model):
	_inherit = 'project.task'

	is_being_tracked_by_user = fields.Boolean(compute='_is_being_tracked')

	# @api.depends('id')
	def _is_being_tracked(self):
		for record in self:
			tracking = self.env['project.task.tracking'].search([('create_uid', '=', self._uid),('task_id', '=', record.id)], limit=1)
			record.is_being_tracked_by_user = tracking

	@api.model
	def stopTrackingTime(self, user):
		_logger.info("click stopTrackingTime")

		uid = user['uid']
		tracking = self.env['project.task.tracking'].search([('create_uid', '=', uid)], limit=1)

		if tracking:
			date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			tracked_time = datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S') - datetime.strptime(tracking.create_date, '%Y-%m-%d %H:%M:%S')
			is_older = datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S') > datetime.strptime(tracking.create_date, '%Y-%m-%d %H:%M:%S')

			if tracked_time.seconds > 60 and is_older:
				task = tracking.task_id

				data = {
					'date' : tracking.create_date,
					'user_id' : uid,
					'name' : tracking.description,
					'account_id' : task.analytic_account_id.id,
					'unit_amount' : (tracked_time.seconds / 60) / 60.00,
					'is_timesheet' : 1,
					'task_id': task.id,
				}

				task.timesheet_ids.create(data)

			#borrar tracking
			tracking.task_id.write({'is_being_tracked_by_user': False})
			tracking.unlink()

	@api.model
	def trackTime(self, cr, user, context=None):
		_logger.info("click trackTime")

		task = self.browse(cr)

		self.stopTrackingTime(user)

		tracking = self.env['project.task.tracking'].create({'task_id': task.id, 'description': 'Timed tracking'}).id
		view_id = self.env.ref('project_task_track_time.project_task_track_button_view_description').id

		return {
			"type": "ir.actions.act_window",
			"res_model": "project.task.tracking",
			"views": [[view_id, "form"]],
			"view_id": view_id,
			"res_id": tracking,
			"target": "new",
			"context": context,
			'flags': {
				'form': {
					'action_buttons': True
				}
			},
		}
