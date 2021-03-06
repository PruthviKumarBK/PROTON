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
import logging
import pygogo as gogo
from pathlib import Path

__author__ = "Pruthvi Kumar, pruthvikumar.123@gmail.com"
__copyright__ = "Copyright (C) 2018 Pruthvi Kumar | http://www.apricity.co.in"
__license__ = "BSD 3-Clause License"
__version__ = "1.0"


class LogUtilities(object):
    """
    Manages logging within PROTON stack.
    """

    def __init__(self):
        super(LogUtilities, self).__init__()
        self.get_logger = self._logger

    @staticmethod
    def _logger(log_file_name, log_file_path):
        """
        Spins up a logger.
        :param log_file_name:[str] logger file name
        :param log_file_path:[str] path where log file needs to be created.
        :return: A valid logger on success; error message on failure.
        """
        try:
            if log_file_name is None or log_file_path is None:
                raise Exception('log_file_name and log_file_path are mandatory to spawn a logger. '
                                'They cannot be None.')
            elif type(log_file_name) is not str or type(log_file_path) is not str:
                raise Exception('log_file_name and log_file_path must be of type String.')
            else:
                dirname = os.path.dirname(log_file_path)
                if os.path.exists(dirname):
                    log_format = '[%(asctime)s] <---> [%(name)s] <---> [%(levelname)s] <---> [%(message)s]'
                    formatter = logging.Formatter(log_format)
                    my_logger = gogo.Gogo(
                        log_file_name,
                        low_hdlr=gogo.handlers.file_hdlr(log_file_path),
                        low_formatter=formatter,
                        high_level='error',
                        high_formatter=formatter,
                    ).logger
                    return my_logger
                else:
                    raise Exception('Given path does not exist in the system. Please enter valid path. '
                                    'PS: PROTON loggers are in ~/PROTON/trace directory')
        except Exception as e:
            print('Unable to spawn a logger. Stack Trace to follow.')
            print(str(e))
