import pytest


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print('Running one time setup')
    if browser == 'chrome':
        print('running on chrome')
        browserType = 'chrome'
    else:
        print('running on other browser')
    if request.cls is not None:
        # to make the browser type available accross our module
        request.cls.browserType = browserType
    yield browserType
    print('Running on time tearDown')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")
