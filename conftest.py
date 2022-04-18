
option = None
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="choose chrome or firefox. Default is chrome")

def pytest_configure(config):
    global option
    option = config.option.browser