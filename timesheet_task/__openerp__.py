# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2012 Camptocamp SA
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
{'name': 'Analytic Task',
 'version': '0.1',
 'author': "Camptocamp,Odoo Community Association (OCA)",
 'maintainer': 'Camptocamp',
 'category': 'Human Resources',
 'complexity': "normal",  # easy, normal, expert
 'depends': ['hr_timesheet', 'project', 'hr_timesheet_invoice'],
 'description': """Replace project.task.work items linked to task
                   with hr.analytic.timesheet""",
 'website': 'http://www.camptocamp.com',
 'init_xml': [],
 'update_xml': ['project_task_view.xml'],
 'demo_xml': [],
 'tests': [],
 'installable': True,
 'images': [],
 'auto_install': False,
 'license': 'AGPL-3',
 'application': True
 }
