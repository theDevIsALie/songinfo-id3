# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'songinfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mutagen
from mutagen.id3 import ID3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(689, 369)
        MainWindow.setFixedSize(689, 369)
        MainWindow.statusBar().setSizeGripEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.songInformationsTitle = QtWidgets.QLabel(self.centralwidget)
        self.songInformationsTitle.setGeometry(QtCore.QRect(10, 10, 311, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songInformationsTitle.sizePolicy().hasHeightForWidth())
        self.songInformationsTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.songInformationsTitle.setFont(font)
        self.songInformationsTitle.setObjectName("songInformationsTitle")
        self.readSongFile = QtWidgets.QPushButton(self.centralwidget)
        self.readSongFile.clicked.connect(self.readSongTags)
        self.readSongFile.setGeometry(QtCore.QRect(570, 10, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readSongFile.sizePolicy().hasHeightForWidth())
        self.readSongFile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.readSongFile.setFont(font)
        self.readSongFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.readSongFile.setObjectName("readSongFile")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.currentFile = QtWidgets.QLabel(self.centralwidget)
        self.currentFile.setGeometry(QtCore.QRect(10, 60, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.currentFile.setFont(font)
        self.currentFile.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.currentFile.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.currentFile.setObjectName("currentFile")
        self.songArtist = QtWidgets.QLabel(self.centralwidget)
        self.songArtist.setGeometry(QtCore.QRect(10, 110, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songArtist.sizePolicy().hasHeightForWidth())
        self.songArtist.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songArtist.setFont(font)
        self.songArtist.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songArtist.setObjectName("songArtist")
        self.songAlbum = QtWidgets.QLabel(self.centralwidget)
        self.songAlbum.setGeometry(QtCore.QRect(10, 140, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songAlbum.sizePolicy().hasHeightForWidth())
        self.songAlbum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songAlbum.setFont(font)
        self.songAlbum.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songAlbum.setObjectName("songAlbum")
        self.songAlbumArtist = QtWidgets.QLabel(self.centralwidget)
        self.songAlbumArtist.setGeometry(QtCore.QRect(10, 160, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songAlbumArtist.sizePolicy().hasHeightForWidth())
        self.songAlbumArtist.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songAlbumArtist.setFont(font)
        self.songAlbumArtist.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songAlbumArtist.setObjectName("songAlbumArtist")
        self.songTitle = QtWidgets.QLabel(self.centralwidget)
        self.songTitle.setGeometry(QtCore.QRect(10, 80, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songTitle.sizePolicy().hasHeightForWidth())
        self.songTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songTitle.setFont(font)
        self.songTitle.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songTitle.setObjectName("songTitle")
        self.songTrackNum = QtWidgets.QLabel(self.centralwidget)
        self.songTrackNum.setGeometry(QtCore.QRect(10, 190, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songTrackNum.sizePolicy().hasHeightForWidth())
        self.songTrackNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songTrackNum.setFont(font)
        self.songTrackNum.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songTrackNum.setObjectName("songTrackNum")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 260, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.songTrackTotal = QtWidgets.QLabel(self.centralwidget)
        self.songTrackTotal.setGeometry(QtCore.QRect(10, 210, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songTrackTotal.sizePolicy().hasHeightForWidth())
        self.songTrackTotal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songTrackTotal.setFont(font)
        self.songTrackTotal.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songTrackTotal.setObjectName("songTrackTotal")
        self.songEncodedBy = QtWidgets.QLabel(self.centralwidget)
        self.songEncodedBy.setGeometry(QtCore.QRect(10, 240, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songEncodedBy.sizePolicy().hasHeightForWidth())
        self.songEncodedBy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songEncodedBy.setFont(font)
        self.songEncodedBy.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songEncodedBy.setObjectName("songEncodedBy")
        self.songBitrate = QtWidgets.QLabel(self.centralwidget)
        self.songBitrate.setGeometry(QtCore.QRect(10, 280, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songBitrate.sizePolicy().hasHeightForWidth())
        self.songBitrate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songBitrate.setFont(font)
        self.songBitrate.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songBitrate.setObjectName("songBitrate")
        self.songLength = QtWidgets.QLabel(self.centralwidget)
        self.songLength.setGeometry(QtCore.QRect(10, 300, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songLength.sizePolicy().hasHeightForWidth())
        self.songLength.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.songLength.setFont(font)
        self.songLength.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.songLength.setObjectName("songLength")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 320, 671, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiono = QtWidgets.QAction(MainWindow)
        self.actiono.setObjectName("actiono")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Song\'s Informations"))

        font_db = QtGui.QFontDatabase()
        font_id = font_db.addApplicationFont("ressources/fonts/FFFFORWA.TTF")

        self.songInformationsTitle.setText(_translate("MainWindow", "Song\'s Informations (ID3)"))
        self.songInformationsTitle.setFont(QtGui.QFont("FFF Forward", 12, 1))
        self.readSongFile.setText(_translate("MainWindow", "Read Song File"))
        self.currentFile.setText(_translate("MainWindow", "Current File:"))
        self.songArtist.setText(_translate("MainWindow", "Artist:"))
        self.songAlbum.setText(_translate("MainWindow", "Album:"))
        self.songAlbumArtist.setText(_translate("MainWindow", "Album Artist:"))
        self.songTitle.setText(_translate("MainWindow", "Title:"))
        self.songTrackNum.setText(_translate("MainWindow", "Track Num:"))
        self.songTrackTotal.setText(_translate("MainWindow", "Track Total:"))
        self.songEncodedBy.setText(_translate("MainWindow", "Encoded by:"))
        self.songBitrate.setText(_translate("MainWindow", "Bitrate:"))
        self.songLength.setText(_translate("MainWindow", "Length:"))
        self.actiono.setText(_translate("MainWindow", "o"))

    def readSongTags(self):
        filter = "MPEG-1/2 Audio Layer III (*.mp3);; OGG Vorbis (*.ogg)"
        filename = QtWidgets.QFileDialog.getOpenFileName(filter=filter)
        if filename[0]:
            tags = ID3(filename[0])

            ui.currentFile.setText(f"Current File: {filename[0]}")

            # Title Tag
            if 'TIT2' in tags:
                titles = ""
                for title in tags['TIT2']:
                    titles += title
                    titles += ", "
                ui.songTitle.setText(f"Title: {titles[:-2]}")
            else:
                ui.songTitle.setText("Title: None")

            # Artist Tag
            if 'TPE1' in tags:
                artists = ""
                for artist in tags['TPE1']:
                    artists += artist
                    artists += ", "
                ui.songArtist.setText(f"Artist: {artists[:-2]}")
            else:
                ui.songArtist.setText("Artist: None")

            # Album Tag
            if 'TALB' in tags:
                albums = ""
                for album in tags['TALB']:
                    albums += album
                    albums += ", "
                ui.songAlbum.setText(f"Album: {albums[:-2]}")
            else:
                ui.songAlbum.setText("Album: None")

            # Album Artist Tag
            if 'TPE2' in tags:
                a_artists = ""
                for a_artist in tags['TPE2']:
                    a_artists += a_artist
                    a_artists += ", "
                ui.songAlbumArtist.setText(f"Album Artist: {a_artists[:-2]}")
            else:
                ui.songAlbumArtist.setText("Album Artist: None")

            # Track Num Tag
            if 'TRCK' in tags:
                track_info = str(tags['TRICK'])
                ui.songTrackNum.setText(f"Track Num: {track_info}")

                try:
                    track_total = str(track_info.split('/')[1])
                    ui.songTrackTotal.setText(f"Track Total: {track_total}")

                except:
                    ui.songTrackTotal.setText("Track Total: None")
            else:
                ui.songTrackNum.setText("Track Num: None")
                ui.songTrackTotal.setText("Track Total: None")

            # Encoded By Tag
            if 'TENC' in tags:
                encoders = ""
                for encoder in tags['TENC']:
                    encoders += encoder
                    encoders += ", "
                ui.songEncodedBy.setText(f"Encoded by: {encoders[:-2]}")
            else:
                ui.songEncodedBy.setText("Encoded by: None")

            audio = mutagen.File(filename[0])
            # Bitrate Tag
            ui.songBitrate.setText(f"Bitrate: {str(audio.info.bitrate)}bps")
            # Length Tag
            ui.songLength.setText(f"Length: {str(audio.info.length)}s")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())