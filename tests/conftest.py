import logging
import os
import random
import shutil
import sys
import time

import pytest
from PyQt5.QtWidgets import QApplication, QStyleFactory

import scctool.settings
from scctool.controller import MainController
from scctool.view.main import MainWindow


def pytest_addoption(parser):
    """Add options to pytest parser."""
    parser.addoption("--aligulac_api_key", action="store",
                     default='', help="aligulac apikey")


@pytest.fixture
def aligulac_api_key(request):
    """Return API key."""
    return request.config.getoption("--aligulac_api_key")


app = None


@pytest.fixture()
def scct_app(tmpdir_factory, caplog):
    caplog.set_level(logging.ERROR)
    global app
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    tmp_dir = tmpdir_factory.getbasetemp()
    if tmp_dir.join('profiles').check(exists=0):
        profile_dir = tmp_dir.mkdir('profiles').mkdir(
            hex(random.randint(49152, 65535))[2:])
        casting_html_src = os.path.normpath(os.path.join(
            os.path.dirname(__file__), '../casting_html'))
        assert os.path.exists(casting_html_src)
        casting_html = profile_dir.join('casting_html')
        if casting_html.check(exists=0):
            shutil.copytree(
                casting_html_src,
                casting_html)
    scctool.settings.loadSettings(str(tmp_dir), True)
    cntlr = MainController()
    main_window = MainWindow(
        cntlr, app, False)
    main_window.show()
    yield (main_window, cntlr)
    # main_window.close()
    # cntlr.cleanUp()
    # time.sleep(1)
    # app.exit(1)
    # time.sleep(1)
    for record in caplog.records:
        assert record.levelname != 'CRITICAL'
        assert record.levelname != 'ERROR'
