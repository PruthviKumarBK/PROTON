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

from configuration import ProtonConfig
from nucleus.generics.log_utilities import LogUtilities
from unittest import TestCase

__author__ = "Pooja Pruthvi, pooja.pruthvikumar@gmail.com"
__copyright__ = "Copyright (C) 2018 Pooja Pruthvi"
__license__ = "BSD 3-Clause License"
__version__ = "1.0"


class TestLogUtilities(TestCase):
    log_utilities_object = LogUtilities()

    def test_log_utilities(self):
        assert isinstance(self.log_utilities_object, LogUtilities)

    def test_logger(self):
        return_logger = self.log_utilities_object.get_logger(log_file_name='test_log_utillities_logs',
                                                             log_file_path='{}/trace/test_log_utillities_logs.log'.format(
                                                                 ProtonConfig.ROOT_DIR))
        print(str(return_logger))
        assert str(type(return_logger)) == "<class 'logging.Logger'>"
        assert str(return_logger) == '<Logger test_log_utillities_logs.base (DEBUG)>'
