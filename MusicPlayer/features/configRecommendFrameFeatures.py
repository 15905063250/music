import addition
import pandas as pd

import recommend
# from  recommend import *
from base import QObject, QTableWidgetItem
import glob
import logging
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton
from configMainFeatures import *
transTime = addition.itv2time
from player import *
from base import QFileDialog, QObject, QTableWidgetItem, checkFolder
class ConfigRecommendFrame(QObject):

    # def __init__(self, parent):
    #     super().__init__()
    #     self.recommendFrame = parent
    #     # self.recommendFrame = parent
    #     self.musicList = []
    #     self.folder = []
    #
    #     self.bindConnect()
    def __init__(self, recommendFrame):
        super(ConfigRecommendFrame, self).__init__()
        self.recommendFrame = recommendFrame
        self.showTable = self.recommendFrame.singsTable
        # self.selectButton = self.recommendFrame.selectButton
        self.musiclist = []
        self.folder = []
        self.bindConnect()
        # self.loadCookies()

    def setSongs(self, musicInfo):
        # df = pd.read_csv('like.csv', names=['user', 'name', 'author', 'time', 'url'], header=0, encoding='utf-8',
        #                  sep=",")
        # recomm = recommend.UserCF.recommended()




        self.recommendFrame.singsTable.setRowCount(len(musicInfo))
        # print()
        for index, data in enumerate(musicInfo):
            self.musicList.append(data._asdict())
            self.recommendFrame.singsTable.setItem(index, 0, QTableWidgetItem(data.name))
            self.recommendFrame.singsTable.setItem(index, 1, QTableWidgetItem(data.author))
            self.recommendFrame.singsTable.setItem(index, 2, QTableWidgetItem(transTime(data.time/1000)))


    def bindConnect(self):
        # self.recommendFrame.selectButton
        # self.recommendFrame.selectButton.clicked.connect(self.selectFolder)
        self.recommendFrame.singsTable.itemDoubleClicked.connect(self.itemDoubleClickedEvent)

    def itemDoubleClickedEvent(self):
        currentRow = self.recommendFrame.singsTable.currentRow()
        data = self.musicList[currentRow]

        self.recommendFrame.parent.playWidgets.setPlayerAndPlayList(data)
