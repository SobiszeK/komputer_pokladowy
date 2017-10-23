# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/rpm_widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_rpm_widget(object):
    def setupUi(self, rpm_widget):
        rpm_widget.setObjectName(_fromUtf8("rpm_widget"))
        rpm_widget.resize(301, 301)
        rpm_widget.setStyleSheet(_fromUtf8("background: none;"))
        self.rpmCaption = QtGui.QLabel(rpm_widget)
        self.rpmCaption.setGeometry(QtCore.QRect(120, 240, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption.setFont(font)
        self.rpmCaption.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 14pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption.setObjectName(_fromUtf8("rpmCaption"))
        self.graphicsView = QtGui.QGraphicsView(rpm_widget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.graphicsView.setStyleSheet(_fromUtf8("background: transparent; "))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.rpmNumber = QtGui.QLCDNumber(rpm_widget)
        self.rpmNumber.setGeometry(QtCore.QRect(74, 173, 151, 61))
        self.rpmNumber.setStyleSheet(_fromUtf8("color: yellow;\n"
"background-color: rgba(255, 255, 255, 20)"))
        self.rpmNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.rpmNumber.setDigitCount(5)
        self.rpmNumber.setObjectName(_fromUtf8("rpmNumber"))
        self.black_circle = QtGui.QLabel(rpm_widget)
        self.black_circle.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.black_circle.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.black_circle.setStyleSheet(_fromUtf8("background-color: none;"))
        self.black_circle.setFrameShape(QtGui.QFrame.Box)
        self.black_circle.setFrameShadow(QtGui.QFrame.Sunken)
        self.black_circle.setText(_fromUtf8(""))
        self.black_circle.setPixmap(QtGui.QPixmap(_fromUtf8("img/blackcircle.png")))
        self.black_circle.setScaledContents(True)
        self.black_circle.setObjectName(_fromUtf8("black_circle"))
        self.dots_widget = QtGui.QWidget(rpm_widget)
        self.dots_widget.setEnabled(True)
        self.dots_widget.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.dots_widget.setObjectName(_fromUtf8("dots_widget"))
        self.circle1 = QtGui.QLabel(self.dots_widget)
        self.circle1.setGeometry(QtCore.QRect(14, 195, 31, 31))
        self.circle1.setText(_fromUtf8(""))
        self.circle1.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle1.png")))
        self.circle1.setScaledContents(True)
        self.circle1.setObjectName(_fromUtf8("circle1"))
        self.circle2 = QtGui.QLabel(self.dots_widget)
        self.circle2.setGeometry(QtCore.QRect(7, 172, 31, 31))
        self.circle2.setText(_fromUtf8(""))
        self.circle2.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle2.png")))
        self.circle2.setScaledContents(True)
        self.circle2.setObjectName(_fromUtf8("circle2"))
        self.circle3 = QtGui.QLabel(self.dots_widget)
        self.circle3.setGeometry(QtCore.QRect(1, 148, 31, 31))
        self.circle3.setText(_fromUtf8(""))
        self.circle3.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle3.png")))
        self.circle3.setScaledContents(True)
        self.circle3.setObjectName(_fromUtf8("circle3"))
        self.circle4 = QtGui.QLabel(self.dots_widget)
        self.circle4.setGeometry(QtCore.QRect(2, 124, 31, 31))
        self.circle4.setText(_fromUtf8(""))
        self.circle4.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle4.png")))
        self.circle4.setScaledContents(True)
        self.circle4.setObjectName(_fromUtf8("circle4"))
        self.circle5 = QtGui.QLabel(self.dots_widget)
        self.circle5.setGeometry(QtCore.QRect(8, 99, 31, 31))
        self.circle5.setText(_fromUtf8(""))
        self.circle5.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle5.png")))
        self.circle5.setScaledContents(True)
        self.circle5.setObjectName(_fromUtf8("circle5"))
        self.circle6 = QtGui.QLabel(self.dots_widget)
        self.circle6.setGeometry(QtCore.QRect(18, 75, 31, 31))
        self.circle6.setText(_fromUtf8(""))
        self.circle6.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle6.png")))
        self.circle6.setScaledContents(True)
        self.circle6.setObjectName(_fromUtf8("circle6"))
        self.circle7 = QtGui.QLabel(self.dots_widget)
        self.circle7.setGeometry(QtCore.QRect(31, 54, 31, 31))
        self.circle7.setText(_fromUtf8(""))
        self.circle7.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle7.png")))
        self.circle7.setScaledContents(True)
        self.circle7.setObjectName(_fromUtf8("circle7"))
        self.circle8 = QtGui.QLabel(self.dots_widget)
        self.circle8.setGeometry(QtCore.QRect(48, 36, 31, 31))
        self.circle8.setText(_fromUtf8(""))
        self.circle8.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle8.png")))
        self.circle8.setScaledContents(True)
        self.circle8.setObjectName(_fromUtf8("circle8"))
        self.circle9 = QtGui.QLabel(self.dots_widget)
        self.circle9.setGeometry(QtCore.QRect(68, 21, 31, 31))
        self.circle9.setStyleSheet(_fromUtf8(""))
        self.circle9.setText(_fromUtf8(""))
        self.circle9.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle9.png")))
        self.circle9.setScaledContents(True)
        self.circle9.setObjectName(_fromUtf8("circle9"))
        self.circle10 = QtGui.QLabel(self.dots_widget)
        self.circle10.setGeometry(QtCore.QRect(89, 11, 31, 31))
        self.circle10.setText(_fromUtf8(""))
        self.circle10.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle10.png")))
        self.circle10.setScaledContents(True)
        self.circle10.setObjectName(_fromUtf8("circle10"))
        self.circle11 = QtGui.QLabel(self.dots_widget)
        self.circle11.setEnabled(True)
        self.circle11.setGeometry(QtCore.QRect(112, 4, 31, 31))
        self.circle11.setText(_fromUtf8(""))
        self.circle11.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle11.png")))
        self.circle11.setScaledContents(True)
        self.circle11.setObjectName(_fromUtf8("circle11"))
        self.circle12 = QtGui.QLabel(self.dots_widget)
        self.circle12.setGeometry(QtCore.QRect(136, 1, 31, 31))
        self.circle12.setText(_fromUtf8(""))
        self.circle12.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle12.png")))
        self.circle12.setScaledContents(True)
        self.circle12.setObjectName(_fromUtf8("circle12"))
        self.circle13 = QtGui.QLabel(self.dots_widget)
        self.circle13.setGeometry(QtCore.QRect(159, 5, 31, 31))
        self.circle13.setText(_fromUtf8(""))
        self.circle13.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle13.png")))
        self.circle13.setScaledContents(True)
        self.circle13.setObjectName(_fromUtf8("circle13"))
        self.circle14 = QtGui.QLabel(self.dots_widget)
        self.circle14.setGeometry(QtCore.QRect(182, 11, 31, 31))
        self.circle14.setText(_fromUtf8(""))
        self.circle14.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle14.png")))
        self.circle14.setScaledContents(True)
        self.circle14.setObjectName(_fromUtf8("circle14"))
        self.circle15 = QtGui.QLabel(self.dots_widget)
        self.circle15.setGeometry(QtCore.QRect(205, 21, 31, 31))
        self.circle15.setText(_fromUtf8(""))
        self.circle15.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle15.png")))
        self.circle15.setScaledContents(True)
        self.circle15.setObjectName(_fromUtf8("circle15"))
        self.circle16 = QtGui.QLabel(self.dots_widget)
        self.circle16.setGeometry(QtCore.QRect(224, 37, 31, 31))
        self.circle16.setText(_fromUtf8(""))
        self.circle16.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle16.png")))
        self.circle16.setScaledContents(True)
        self.circle16.setObjectName(_fromUtf8("circle16"))
        self.circle17 = QtGui.QLabel(self.dots_widget)
        self.circle17.setGeometry(QtCore.QRect(241, 55, 31, 31))
        self.circle17.setText(_fromUtf8(""))
        self.circle17.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle17.png")))
        self.circle17.setScaledContents(True)
        self.circle17.setObjectName(_fromUtf8("circle17"))
        self.circle18 = QtGui.QLabel(self.dots_widget)
        self.circle18.setGeometry(QtCore.QRect(253, 75, 31, 31))
        self.circle18.setText(_fromUtf8(""))
        self.circle18.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle18.png")))
        self.circle18.setScaledContents(True)
        self.circle18.setObjectName(_fromUtf8("circle18"))
        self.circle19 = QtGui.QLabel(self.dots_widget)
        self.circle19.setGeometry(QtCore.QRect(263, 98, 31, 31))
        self.circle19.setText(_fromUtf8(""))
        self.circle19.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle19.png")))
        self.circle19.setScaledContents(True)
        self.circle19.setObjectName(_fromUtf8("circle19"))
        self.circle20 = QtGui.QLabel(self.dots_widget)
        self.circle20.setGeometry(QtCore.QRect(269, 121, 31, 31))
        self.circle20.setText(_fromUtf8(""))
        self.circle20.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle20.png")))
        self.circle20.setScaledContents(True)
        self.circle20.setObjectName(_fromUtf8("circle20"))
        self.circle21 = QtGui.QLabel(self.dots_widget)
        self.circle21.setGeometry(QtCore.QRect(270, 145, 31, 31))
        self.circle21.setText(_fromUtf8(""))
        self.circle21.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle21.png")))
        self.circle21.setScaledContents(True)
        self.circle21.setObjectName(_fromUtf8("circle21"))
        self.circle22 = QtGui.QLabel(self.dots_widget)
        self.circle22.setGeometry(QtCore.QRect(266, 169, 31, 31))
        self.circle22.setText(_fromUtf8(""))
        self.circle22.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle22.png")))
        self.circle22.setScaledContents(True)
        self.circle22.setObjectName(_fromUtf8("circle22"))
        self.circle23 = QtGui.QLabel(self.dots_widget)
        self.circle23.setGeometry(QtCore.QRect(257, 191, 31, 31))
        self.circle23.setText(_fromUtf8(""))
        self.circle23.setPixmap(QtGui.QPixmap(_fromUtf8("img/colorized_circles/circle23.png")))
        self.circle23.setScaledContents(True)
        self.circle23.setObjectName(_fromUtf8("circle23"))
        self.pintop = QtGui.QLabel(rpm_widget)
        self.pintop.setGeometry(QtCore.QRect(130, 130, 41, 41))
        self.pintop.setStyleSheet(_fromUtf8("background: none;"))
        self.pintop.setFrameShape(QtGui.QFrame.NoFrame)
        self.pintop.setText(_fromUtf8(""))
        self.pintop.setPixmap(QtGui.QPixmap(_fromUtf8("img/pintop.png")))
        self.pintop.setScaledContents(True)
        self.pintop.setObjectName(_fromUtf8("pintop"))
        self.dark_dots_widget = QtGui.QWidget(rpm_widget)
        self.dark_dots_widget.setEnabled(True)
        self.dark_dots_widget.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.dark_dots_widget.setObjectName(_fromUtf8("dark_dots_widget"))
        self.circle1_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle1_3.setGeometry(QtCore.QRect(14, 195, 31, 31))
        self.circle1_3.setText(_fromUtf8(""))
        self.circle1_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle1.png")))
        self.circle1_3.setScaledContents(True)
        self.circle1_3.setObjectName(_fromUtf8("circle1_3"))
        self.circle2_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle2_3.setGeometry(QtCore.QRect(7, 172, 31, 31))
        self.circle2_3.setText(_fromUtf8(""))
        self.circle2_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle2.png")))
        self.circle2_3.setScaledContents(True)
        self.circle2_3.setObjectName(_fromUtf8("circle2_3"))
        self.circle3_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle3_3.setGeometry(QtCore.QRect(1, 148, 31, 31))
        self.circle3_3.setText(_fromUtf8(""))
        self.circle3_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle3.png")))
        self.circle3_3.setScaledContents(True)
        self.circle3_3.setObjectName(_fromUtf8("circle3_3"))
        self.circle4_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle4_3.setGeometry(QtCore.QRect(2, 124, 31, 31))
        self.circle4_3.setText(_fromUtf8(""))
        self.circle4_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle4.png")))
        self.circle4_3.setScaledContents(True)
        self.circle4_3.setObjectName(_fromUtf8("circle4_3"))
        self.circle5_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle5_3.setGeometry(QtCore.QRect(8, 99, 31, 31))
        self.circle5_3.setText(_fromUtf8(""))
        self.circle5_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle5.png")))
        self.circle5_3.setScaledContents(True)
        self.circle5_3.setObjectName(_fromUtf8("circle5_3"))
        self.circle6_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle6_3.setGeometry(QtCore.QRect(18, 75, 31, 31))
        self.circle6_3.setText(_fromUtf8(""))
        self.circle6_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle6.png")))
        self.circle6_3.setScaledContents(True)
        self.circle6_3.setObjectName(_fromUtf8("circle6_3"))
        self.circle7_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle7_3.setGeometry(QtCore.QRect(31, 54, 31, 31))
        self.circle7_3.setText(_fromUtf8(""))
        self.circle7_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle7.png")))
        self.circle7_3.setScaledContents(True)
        self.circle7_3.setObjectName(_fromUtf8("circle7_3"))
        self.circle8_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle8_3.setGeometry(QtCore.QRect(48, 36, 31, 31))
        self.circle8_3.setText(_fromUtf8(""))
        self.circle8_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle8.png")))
        self.circle8_3.setScaledContents(True)
        self.circle8_3.setObjectName(_fromUtf8("circle8_3"))
        self.circle9_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle9_3.setGeometry(QtCore.QRect(68, 21, 31, 31))
        self.circle9_3.setStyleSheet(_fromUtf8(""))
        self.circle9_3.setText(_fromUtf8(""))
        self.circle9_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle9.png")))
        self.circle9_3.setScaledContents(True)
        self.circle9_3.setObjectName(_fromUtf8("circle9_3"))
        self.circle10_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle10_3.setGeometry(QtCore.QRect(89, 11, 31, 31))
        self.circle10_3.setText(_fromUtf8(""))
        self.circle10_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle10.png")))
        self.circle10_3.setScaledContents(True)
        self.circle10_3.setObjectName(_fromUtf8("circle10_3"))
        self.circle11_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle11_3.setEnabled(True)
        self.circle11_3.setGeometry(QtCore.QRect(112, 4, 31, 31))
        self.circle11_3.setText(_fromUtf8(""))
        self.circle11_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle11.png")))
        self.circle11_3.setScaledContents(True)
        self.circle11_3.setObjectName(_fromUtf8("circle11_3"))
        self.circle12_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle12_3.setGeometry(QtCore.QRect(136, 1, 31, 31))
        self.circle12_3.setText(_fromUtf8(""))
        self.circle12_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle12.png")))
        self.circle12_3.setScaledContents(True)
        self.circle12_3.setObjectName(_fromUtf8("circle12_3"))
        self.circle13_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle13_3.setGeometry(QtCore.QRect(159, 5, 31, 31))
        self.circle13_3.setText(_fromUtf8(""))
        self.circle13_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle13.png")))
        self.circle13_3.setScaledContents(True)
        self.circle13_3.setObjectName(_fromUtf8("circle13_3"))
        self.circle14_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle14_3.setGeometry(QtCore.QRect(182, 11, 31, 31))
        self.circle14_3.setText(_fromUtf8(""))
        self.circle14_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle14.png")))
        self.circle14_3.setScaledContents(True)
        self.circle14_3.setObjectName(_fromUtf8("circle14_3"))
        self.circle15_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle15_3.setGeometry(QtCore.QRect(205, 21, 31, 31))
        self.circle15_3.setText(_fromUtf8(""))
        self.circle15_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle15.png")))
        self.circle15_3.setScaledContents(True)
        self.circle15_3.setObjectName(_fromUtf8("circle15_3"))
        self.circle16_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle16_3.setGeometry(QtCore.QRect(224, 37, 31, 31))
        self.circle16_3.setText(_fromUtf8(""))
        self.circle16_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle16.png")))
        self.circle16_3.setScaledContents(True)
        self.circle16_3.setObjectName(_fromUtf8("circle16_3"))
        self.circle17_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle17_3.setGeometry(QtCore.QRect(241, 55, 31, 31))
        self.circle17_3.setText(_fromUtf8(""))
        self.circle17_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle17.png")))
        self.circle17_3.setScaledContents(True)
        self.circle17_3.setObjectName(_fromUtf8("circle17_3"))
        self.circle18_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle18_3.setGeometry(QtCore.QRect(253, 75, 31, 31))
        self.circle18_3.setText(_fromUtf8(""))
        self.circle18_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle18.png")))
        self.circle18_3.setScaledContents(True)
        self.circle18_3.setObjectName(_fromUtf8("circle18_3"))
        self.circle19_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle19_3.setGeometry(QtCore.QRect(263, 98, 31, 31))
        self.circle19_3.setText(_fromUtf8(""))
        self.circle19_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle19.png")))
        self.circle19_3.setScaledContents(True)
        self.circle19_3.setObjectName(_fromUtf8("circle19_3"))
        self.circle20_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle20_3.setGeometry(QtCore.QRect(269, 121, 31, 31))
        self.circle20_3.setText(_fromUtf8(""))
        self.circle20_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle20.png")))
        self.circle20_3.setScaledContents(True)
        self.circle20_3.setObjectName(_fromUtf8("circle20_3"))
        self.circle21_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle21_3.setGeometry(QtCore.QRect(270, 145, 31, 31))
        self.circle21_3.setText(_fromUtf8(""))
        self.circle21_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle21.png")))
        self.circle21_3.setScaledContents(True)
        self.circle21_3.setObjectName(_fromUtf8("circle21_3"))
        self.circle22_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle22_3.setGeometry(QtCore.QRect(266, 169, 31, 31))
        self.circle22_3.setText(_fromUtf8(""))
        self.circle22_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle22.png")))
        self.circle22_3.setScaledContents(True)
        self.circle22_3.setObjectName(_fromUtf8("circle22_3"))
        self.circle23_3 = QtGui.QLabel(self.dark_dots_widget)
        self.circle23_3.setGeometry(QtCore.QRect(257, 191, 31, 31))
        self.circle23_3.setText(_fromUtf8(""))
        self.circle23_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/dark_colorized_circles/circle23.png")))
        self.circle23_3.setScaledContents(True)
        self.circle23_3.setObjectName(_fromUtf8("circle23_3"))
        self.rpmCaption_2 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_2.setGeometry(QtCore.QRect(30, 130, 20, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_2.setFont(font)
        self.rpmCaption_2.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_2.setObjectName(_fromUtf8("rpmCaption_2"))
        self.rpmCaption_3 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_3.setGeometry(QtCore.QRect(70, 60, 20, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_3.setFont(font)
        self.rpmCaption_3.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_3.setObjectName(_fromUtf8("rpmCaption_3"))
        self.rpmCaption_4 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_4.setGeometry(QtCore.QRect(140, 40, 16, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_4.setFont(font)
        self.rpmCaption_4.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_4.setObjectName(_fromUtf8("rpmCaption_4"))
        self.rpmCaption_5 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_5.setGeometry(QtCore.QRect(200, 60, 20, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_5.setFont(font)
        self.rpmCaption_5.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_5.setObjectName(_fromUtf8("rpmCaption_5"))
        self.rpmCaption_6 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_6.setGeometry(QtCore.QRect(240, 130, 20, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_6.setFont(font)
        self.rpmCaption_6.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_6.setObjectName(_fromUtf8("rpmCaption_6"))
        self.rpmCaption_7 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_7.setGeometry(QtCore.QRect(230, 200, 20, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans MT"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.rpmCaption_7.setFont(font)
        self.rpmCaption_7.setStyleSheet(_fromUtf8("color: white; \n"
"background:none;\n"
"font: 75 italic 12pt \"Gill Sans MT\" ;\n"
"color: rgb(216, 216, 216);"))
        self.rpmCaption_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_7.setObjectName(_fromUtf8("rpmCaption_7"))
        self.rpmCaption_8 = QtGui.QLabel(rpm_widget)
        self.rpmCaption_8.setGeometry(QtCore.QRect(110, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.rpmCaption_8.setFont(font)
        self.rpmCaption_8.setStyleSheet(_fromUtf8("color: white; \n"
"font: 14pt \"Ubuntu Mono\";\n"
"background:none;\n"
"font: 63 italic 14pt \"Ubuntu\";\n"
"color: rgb(216, 216, 216);\n"
"font: italic 14pt \"Ubuntu\";"))
        self.rpmCaption_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rpmCaption_8.setObjectName(_fromUtf8("rpmCaption_8"))
        self.black_circle.raise_()
        self.dark_dots_widget.raise_()
        self.dots_widget.raise_()
        self.graphicsView.raise_()
        self.pintop.raise_()
        self.rpmCaption.raise_()
        self.rpmNumber.raise_()
        self.rpmCaption_2.raise_()
        self.rpmCaption_3.raise_()
        self.rpmCaption_4.raise_()
        self.rpmCaption_5.raise_()
        self.rpmCaption_6.raise_()
        self.rpmCaption_7.raise_()
        self.rpmCaption_8.raise_()

        self.retranslateUi(rpm_widget)
        QtCore.QMetaObject.connectSlotsByName(rpm_widget)

    def retranslateUi(self, rpm_widget):
        rpm_widget.setWindowTitle(_translate("rpm_widget", "Form", None))
        self.rpmCaption.setText(_translate("rpm_widget", "km/h", None))
        self.rpmCaption_2.setText(_translate("rpm_widget", "1", None))
        self.rpmCaption_3.setText(_translate("rpm_widget", "2", None))
        self.rpmCaption_4.setText(_translate("rpm_widget", "3", None))
        self.rpmCaption_5.setText(_translate("rpm_widget", "4", None))
        self.rpmCaption_6.setText(_translate("rpm_widget", "5", None))
        self.rpmCaption_7.setText(_translate("rpm_widget", "6", None))
        self.rpmCaption_8.setText(_translate("rpm_widget", "rpm * 1000", None))

