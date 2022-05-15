import sys

from qgis.PyQt.QtWidgets import QApplication, QWidget, QMainWindow,QMessageBox, QTableWidgetItem, QAbstractItemView
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QPixmap,QIcon,QBrush
from jydzcx_ui import Ui_Form
from mdb import mdb_conn


class JYDZCX(Ui_Form, QWidget):
    def __init__(self, mdb, mainWindow=None):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.mdb = mdb
        self.mainWindow = mainWindow
        self.loadTableData()
        self.zkTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.zkTable.setStyleSheet("selection-background-color:rgb(255,209,128)")
        self.zkTable.resizeColumnsToContents()
        self.zkCombox.currentTextChanged.connect(self.onzkComboxTextChanged)
        self.loadzkNo()
        self.escButton.clicked.connect(self.onescButtonClicked)
        self.queryButton.clicked.connect(self.onqueryButtonClicked)
        self.clearButton.clicked.connect(self.onclearButtonClicked)
        self.viewImg.clicked.connect(self.onviewImgClicked)

    def loadTableData(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self,"错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        self.zkTable.setColumnCount(10)
        self.zkTable.setHorizontalHeaderLabels(
            ['OBJECTID', '钻孔编号', '周期', 'F50年63_', 'F50年10_', 'F50年2_', 'F100年63_', 'F100年10_', 'F100年2_', 'F100年1_'])
        sqlstr = "select count(*) from jiyandizhendong"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        zksdata = cursor.fetchone()
        zknum = zksdata[0]
        self.zkTable.setRowCount(zknum)
        sqlstr = "select * from jiyandizhendong"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        zksdata = cursor.fetchall()
        n = 0
        for zkdata in zksdata:
            zkid = QTableWidgetItem(str(zkdata[0]))
            zkid.setTextAlignment(Qt.AlignCenter)
            zkno = QTableWidgetItem(str(zkdata[1]))
            zkno.setTextAlignment(Qt.AlignCenter)
            zkzq = QTableWidgetItem(str(zkdata[2]))
            zkzq.setTextAlignment(Qt.AlignCenter)
            zkF50_63 = QTableWidgetItem(str(zkdata[3]))
            zkF50_63.setTextAlignment(Qt.AlignCenter)
            zkF50_10 = QTableWidgetItem(str(zkdata[4]))
            zkF50_10.setTextAlignment(Qt.AlignCenter)
            zkF50_2 = QTableWidgetItem(str(zkdata[5]))
            zkF50_2.setTextAlignment(Qt.AlignCenter)
            zkF100_63 = QTableWidgetItem(str(zkdata[6]))
            zkF100_63.setTextAlignment(Qt.AlignCenter)
            zkF100_10 = QTableWidgetItem(str(zkdata[7]))
            zkF100_10.setTextAlignment(Qt.AlignCenter)
            zkF100_2 = QTableWidgetItem(str(zkdata[8]))
            zkF100_2.setTextAlignment(Qt.AlignCenter)
            zkF100_1 = QTableWidgetItem(str(zkdata[9]))
            zkF100_1.setTextAlignment(Qt.AlignCenter)
            self.zkTable.setItem(n, 0, zkid)
            self.zkTable.setItem(n, 1, zkno)
            self.zkTable.setItem(n, 2, zkzq)
            self.zkTable.setItem(n, 3, zkF50_63)
            self.zkTable.setItem(n, 4, zkF50_10)
            self.zkTable.setItem(n, 5, zkF50_2)
            self.zkTable.setItem(n, 6, zkF100_63)
            self.zkTable.setItem(n, 7, zkF100_10)
            self.zkTable.setItem(n, 8, zkF100_2)
            self.zkTable.setItem(n, 9, zkF100_1)
            n += 1
        self.conn.close()

    def loadzkNo(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self,"错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = "select distinct 钻孔编号 from jiyandizhendong"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        zknos = cursor.fetchall()
        for zkno in zknos:
            zkno = str(zkno[0])
            self.zkCombox.insertItem(int(zkno[2:]) - 1, zkno)
        self.zkCombox.setCurrentIndex(0)

    def onzkComboxTextChanged(self, zkno):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self,"错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = "select 周期 from jiyandizhendong where 钻孔编号='{}'".format(zkno)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        zkzqs = cursor.fetchall()
        for zkzq in zkzqs:
            self.zqCombox.addItem(str(zkzq[0]))
        self.conn.close()

    def onescButtonClicked(self):
        self.close()

    def onqueryButtonClicked(self):
        zkindex = self.zkCombox.currentIndex()
        zqindex = self.zqCombox.currentIndex()
        if zkindex == -1 or zqindex == -1:
            QMessageBox.warning(self,"警告", "请设置钻孔编号和周期参数后再进行查询！", QMessageBox.Yes, QMessageBox.Yes)
            return
        zkno_ = self.zkCombox.currentText()
        zkzq_ = self.zqCombox.currentText()
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self,"错误", "无法连接到数据库{}".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sql = "select * from jiyandizhendong where 钻孔编号='{}' and 周期='{}'".format(zkno_, zkzq_)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        zksdata = cursor.fetchall()
        zksnum = len(zksdata)
        self.zkzqTable.setColumnCount(10)
        self.zkzqTable.setHorizontalHeaderLabels(
            ['OBJECTID', '钻孔编号', '周期', 'F50年63_', 'F50年10_', 'F50年2_', 'F100年63_', 'F100年10_', 'F100年2_', 'F100年1_'])
        self.zkzqTable.setRowCount(zksnum)
        n = 0
        for zkdata in zksdata:
            zkid = QTableWidgetItem(str(zkdata[0]))
            zkid.setTextAlignment(Qt.AlignCenter)
            zkno = QTableWidgetItem(str(zkdata[1]))
            zkno.setTextAlignment(Qt.AlignCenter)
            zkzq = QTableWidgetItem(str(zkdata[2]))
            zkzq.setTextAlignment(Qt.AlignCenter)
            zkF50_63 = QTableWidgetItem(str(zkdata[3]))
            zkF50_63.setTextAlignment(Qt.AlignCenter)
            zkF50_10 = QTableWidgetItem(str(zkdata[4]))
            zkF50_10.setTextAlignment(Qt.AlignCenter)
            zkF50_2 = QTableWidgetItem(str(zkdata[5]))
            zkF50_2.setTextAlignment(Qt.AlignCenter)
            zkF100_63 = QTableWidgetItem(str(zkdata[6]))
            zkF100_63.setTextAlignment(Qt.AlignCenter)
            zkF100_10 = QTableWidgetItem(str(zkdata[7]))
            zkF100_10.setTextAlignment(Qt.AlignCenter)
            zkF100_2 = QTableWidgetItem(str(zkdata[8]))
            zkF100_2.setTextAlignment(Qt.AlignCenter)
            zkF100_1 = QTableWidgetItem(str(zkdata[9]))
            zkF100_1.setTextAlignment(Qt.AlignCenter)
            self.zkzqTable.setItem(n, 0, zkid)
            self.zkzqTable.setItem(n, 1, zkno)
            self.zkzqTable.setItem(n, 2, zkzq)
            self.zkzqTable.setItem(n, 3, zkF50_63)
            self.zkzqTable.setItem(n, 4, zkF50_10)
            self.zkzqTable.setItem(n, 5, zkF50_2)
            self.zkzqTable.setItem(n, 6, zkF100_63)
            self.zkzqTable.setItem(n, 7, zkF100_10)
            self.zkzqTable.setItem(n, 8, zkF100_2)
            self.zkzqTable.setItem(n, 9, zkF100_1)
            n += 1
        self.zknoLabel.setText("钻孔编号：{}".format(zkno_))
        self.zkzqLabel.setText("周期：{}".format(zkzq_))
        self.conn.close()

    def onclearButtonClicked(self):
        self.zkzqTable.clear()
        self.zknoLabel.setText("钻孔编号：")
        self.zkzqLabel.setText("周期：")

    def onviewImgClicked(self):
        zkindex = self.zkCombox.currentIndex()
        if zkindex == -1:
            QMessageBox.warning(self,"警告", "查看基岩反应谱需要先设置钻孔编号参数！", QMessageBox.Yes, QMessageBox.Yes)
            return
        zkno = self.zkCombox.currentText()
        zkimgFile = "./jyfyp/{}.jpg".format(zkno)
        self.zkPixmap = QPixmap(zkimgFile)
        self.imgWindow = QMainWindow()
        self.imgWindow.setFixedSize(800, 800)
        self.imgWindow.setWindowIcon(QIcon("./icons/反应谱.png"))
        self.imgWindow.setWindowTitle("钻孔基岩反应谱:{}".format(zkno))
        palette = self.imgWindow.palette()
        palette.setBrush(self.imgWindow.backgroundRole(), QBrush(
            self.zkPixmap.scaled(self.imgWindow.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.imgWindow.setPalette(palette)
        self.imgWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = JYDZCX(r"C:\Users\user\Desktop\地质管理系统\ui\anping.mdb")
    appWindow.show()
    app.exec_()
