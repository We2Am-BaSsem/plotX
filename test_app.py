import pytest

from PyQt5 import QtCore
from pytestqt.plugin import qtbot
from plotX import plotX


@pytest.fixture
def app(qtbot):
    app_under_test = plotX()
    qtbot.addWidget(app_under_test)
    return app_under_test


def test_submit_empty_data_raise_error(app, qtbot):
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Empty Data"


def test_submit_empty_minX_and_maxX_raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Empty Data"


def test_submit_empty_Function_and_maxX_raise_error(app, qtbot):
    qtbot.keyClicks(app.minX, "value")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Empty Data"


def test_submit_empty_minX_and_Function_raise_error(app, qtbot):
    qtbot.keyClicks(app.maxX, "value")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Empty Data"


def test_submit__string_minX__raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.keyClicks(app.minX, "value")
    qtbot.keyClicks(app.maxX, "-5")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Enter a numeric value for minX"


def test_submit__string_maxX__raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.keyClicks(app.minX, "5.5")
    qtbot.keyClicks(app.maxX, "value")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Enter a numeric value for maxX"


def test_submit__minX_greater_than_maxX__raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.keyClicks(app.minX, "5.5")
    qtbot.keyClicks(app.maxX, "1")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert (
        app.text_label.text()
        == "minX can't be greater than maxX.\nThey will be swaped"
    )


def test_submit__minX_equal_maxX__raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.keyClicks(app.minX, "5.5")
    qtbot.keyClicks(app.maxX, "5.5")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert (
        app.text_label.text()
        == "minX can't be equal to to maxX"
    )


def test_submit__string_invalid_function__raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "Function")
    qtbot.keyClicks(app.minX, "5.5")
    qtbot.keyClicks(app.maxX, "66")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Invalid Process"


def test_valid_submit__does_not_raise_error(app, qtbot):
    qtbot.keyClicks(app.F_X, "x+2")
    qtbot.keyClicks(app.minX, "5.5")
    qtbot.keyClicks(app.maxX, "66")
    qtbot.mouseClick(app.PlotButton, QtCore.Qt.LeftButton)
    assert app.text_label.text() == ""
