import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


def f(function, xInterval):
    try:
        F_X = np.zeros(xInterval.shape)
        function = function.lower()
        index = 0
        for x in xInterval:
            F_X[index] = eval(function)
            index += 1

        return F_X
    except:
        return "Invalid Process"


def Validate(Function="", minX="", maxX=""):
    if Function == "" or minX == "" or maxX == "":
        return "Empty Data"

    try:
        float(minX)
    except:
        return "Enter a numeric value for minX"

    try:
        float(maxX)
    except:
        return "Enter a numeric value for maxX"

    if float(minX) > float(maxX):
        return "minX can't be greater than maxX"
    elif float(maxX) == float(minX):
        return "minX can't be equal to to maxX"
    else:
        return "OK"


def Submit(
    ErrorMessageLabel="",
    Function="",
    minX="",
    maxX="",
    nbins="100",
    plotGraph=None,
    plotFigure=None,
):
    Function_Value = Function.text().replace("^", "**")
    minX_Value = minX.text()
    maxX_Value = maxX.text()
    ValidationResult = Validate(Function_Value, minX_Value, maxX_Value)
    if ValidationResult == "minX can't be greater than maxX":
        ErrorMessageLabel.setText(ValidationResult + ".\nThey will be swaped")
        temp = minX_Value
        minX.setText(maxX_Value)
        maxX.setText(temp)
        # temp = minX
        # minX = maxX
        # maxX = temp
    elif ValidationResult != "OK":
        ErrorMessageLabel.setText(ValidationResult)
        return
    else:
        ErrorMessageLabel.setText("")

    xAxis = np.linspace(float(minX_Value), float(maxX_Value), int(nbins))
    yAxis = f(Function_Value, xAxis)

    if yAxis == "Invalid Process":
        ErrorMessageLabel.setText("Invalid Process")
        return

    plotFigure.clear()
    ax = plotFigure.add_subplot(111)
    ax.plot(xAxis, yAxis)
    plotGraph.draw()
