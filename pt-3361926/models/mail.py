from odoo import api, fields, models
import datetime

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def send_birthday_messages(self):
        """Runs daily, checks employees with birthdays and sends an email."""

        employees = self.env['hr.employee'].search_read([]) # ('birthday.day', '=', datetime.date.today().day)

        # loops for all employees
        for employee in employees:
            # ensures they have both a birthday and email to send to
            if employee['birthday'] and employee['work_email']:
                birthday = employee['birthday']
                cur_date = datetime.date.today()
                # checks if month and date of birthday matches current day
                if cur_date.day == birthday.day and cur_date.month == birthday.month:
                    mail_pool = self.env['mail.mail']
                    values={}
                    # adds email values
                    values.update({'subject': 'Happy birthday, ' + employee['display_name'].split(' ')[0] + '!'})
                    values.update({'email_to': employee['work_email']})
                    values.update({'body_html': '<p>Happy birthday! We at JaniClean hope you have a magical day filled with ponies and rainbows. Wow. Yes.</p>' })
                    msg_id = mail_pool.create(values)

                    # if email was generated correctly, send
                    if msg_id:
                        mail_pool.send([msg_id])