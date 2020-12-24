import os
import pytest
from pytest_jsonreport.plugin import JSONReport


plugin = JSONReport()
# we need to pass project url here in --project-url
# res = pytest.main(['--project-url=test', '--json-report-file=none', 'test_only.py', 'test_gmail.py','-s'], plugins=[plugin])
driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drivers', 'chromedriver')
driver_path = '/usr/bin/chromedriver'
result = pytest.main([
    f'--driver-path={driver_path}',
    '--project-url=https://github.com/login',
    'test_only.py',
    '--json-report-file=none' 
    ], plugins=[plugin])

#: Tests passed.
OK = 0
#: Tests failed.
TESTS_FAILED = 1
#: pytest was interrupted.
INTERRUPTED = 2
#: An internal error got in the way.
INTERNAL_ERROR = 3
#: pytest was misused.
USAGE_ERROR = 4
#: pytest couldn't find tests.
NO_TESTS_COLLECTED = 5
if result == OK or result == TESTS_FAILED:
    print(plugin.report)
print(result.name)
