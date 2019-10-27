# BSD 3-Clause License
#
# Copyright (c) 2018, Pruthvi Kumar All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following
# disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided with the distribution.
#
# Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from configuration import ProtonConfig
from nucleus.generics.log_utilities import LogUtilities

__author__ = "Pruthvi Kumar, pruthvikumar.123@gmail.com"
__copyright__ = "Copyright (C) 2018 Pruthvi Kumar | http://www.apricity.co.in"
__license__ = "BSD 3-Clause License"
__version__ = "1.0"


class ProtonEmail(object):
    """
    PROTONs email client.
    """
    email_logger = LogUtilities().get_logger(log_file_name='emailer_logs',
                                             log_file_path='{}/trace/emailer_logs.log'.format(ProtonConfig.ROOT_DIR))
    __sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    def __init__(self):
        super(ProtonEmail, self).__init__()

    @classmethod
    def send_email(cls, to_email, subject, html_content, from_email='proton_framework@apricity.co.in'):
        """
        PROTONs postman.

        :param to_email: valid email to which email needs to be sent to.
        :param subject: Email subject
        :param html_content: Email content.(Can include HTML markups)
        :param from_email: valid email from which email has to be sent from. (default to proton_framework@apricity.co.in)
        :return: A dictionary containing email status code, email body and email headers.
        """
        try:
            message = Mail(
                from_email=from_email,
                to_emails=to_email,
                subject=subject,
                html_content=html_content)
            response = cls.__sg.send(message)
            return {
                'email_status_code': response.status_code,
                'email_body': response.body,
                'email_headers': response.headers
            }

        except Exception as e:
            cls.email_logger.exception('[Email]: Unable to send email. Details to follow.')
            cls.email_logger.exception(str(e))




