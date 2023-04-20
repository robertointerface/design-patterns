"""
You can mark a specific file with a marker, the all the tests in the file
are marked.
"""

import pytest

pytestmark = pytest.mark.unittest
# you can also have multiple markers

#pytestmark = [pytest.mark.one_mark, pytest.mark.two_mark]
