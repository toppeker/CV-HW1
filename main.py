import sys
# import WrapperFunctions
import PlotterFunctions
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

# global variables
inputFileName = ""
targetFileName = ""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load ui file
        uic.loadUi('mainscreen.ui', self)

        # Exit Action Handler
        self.actionExit.triggered.connect(QApplication.instance().quit)
        # Open Input Action Handler
        self.actionOpen_Input.triggered.connect(self.on_pushInput_triggered)
        # Open Target Action Handler
        self.actionOpen_Target.triggered.connect(self.on_pushTarget_triggered)
        # Equalize histogram button handler
        self.toolButton.clicked.connect(self.on_clickButton)


    # This function opens the input image and draws the histogram
    @QtCore.pyqtSlot()
    def on_pushInput_triggered(self):
        # choose the input file
        global inputFileName
        inputFileName = fileName = self.openFileNameDialog()

        # draw image
        pixmap = QtGui.QPixmap(fileName)
        self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))

        # draw histogram of this image
        PlotterFunctions.doHistogramPlots(fileName, 'inputHistogram.png')
        pixmap2 = QtGui.QPixmap('inputHistogram.png')
        self.label_4.setPixmap(pixmap2.scaled(self.label_4.size(), QtCore.Qt.IgnoreAspectRatio))


    # This function opens the target image and draws the histogram
    @QtCore.pyqtSlot()
    def on_pushTarget_triggered(self):
        # choose the target file
        global targetFileName
        targetFileName = fileName = self.openFileNameDialog()

        # draw image
        pixmap = QtGui.QPixmap(fileName)
        self.label_2.setPixmap(pixmap.scaled(self.label_2.size(), QtCore.Qt.IgnoreAspectRatio))

        # draw histogram of this image
        PlotterFunctions.doHistogramPlots(fileName, 'targetHistogram.png')
        pixmap2 = QtGui.QPixmap('targetHistogram.png')
        self.label_5.setPixmap(pixmap2.scaled(self.label_5.size(), QtCore.Qt.IgnoreAspectRatio))


    @QtCore.pyqtSlot()
    def on_clickButton(self):
        # check whether input and target images are chosen or not
        if not (inputFileName and targetFileName):
            self.messageBox()
        else:
            # plot the output image
            print(inputFileName)
            PlotterFunctions.matchThreeChannels(inputFileName, targetFileName)
            pixmap = QtGui.QPixmap("output.png")
            self.label_3.setPixmap(pixmap.scaled(self.label_3.size(), QtCore.Qt.IgnoreAspectRatio))

            # draw histogram of this image
            PlotterFunctions.doHistogramPlots("output.png", "outputHistogram.png")
            pixmap2 = QtGui.QPixmap("outputHistogram.png")
            self.label_6.setPixmap(pixmap2.scaled(self.label_6.size(), QtCore.Qt.IgnoreAspectRatio))



    @QtCore.pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

    @QtCore.pyqtSlot()
    def messageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("You need to choose input and target images before you click on Equalize Histograms button!")
        msg.setInformativeText("Please choose both images and click on Equalize Histogram button")
        msg.setWindowTitle("Missing image!")

        msg.exec_()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
