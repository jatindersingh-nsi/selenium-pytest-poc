import pytest


def pytest_addoption(parser):
    """
    Override pytest default method to add new option
    """
    parser.addoption('--project-url', action='store', help='Project URL where the application is running.')
    parser.addoption('--driver-path', action='store', help='Browser driver path for Selenium.')


@pytest.fixture
def params(request):
    """
    Keep extra options available in every function and class methods. Specific test case will be skipped if it has
    `params` argument in signature and `--project-url` is not set in CLI.
    """
    params = {'project_url': request.config.getoption('--project-url'),
              'driver_path': request.config.getoption('--driver-path')}
    if params['project_url'] is None or params['driver_path'] is None:
        pytest.skip()
    return params
