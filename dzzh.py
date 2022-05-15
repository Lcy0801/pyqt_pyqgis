import sys
from qgis.PyQt.QtWidgets import (QApplication,
                                 QWidget,
                                 QMessageBox,
                                 QAbstractItemView,
                                 QTableWidgetItem)
from qgis.PyQt.QtCore import Qt
from dzzh_ui import Ui_Form
from mdb import mdb_conn


class DZZH(QWidget, Ui_Form):
    def __init__(self, mdb, mainWindow):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.mdb = mdb
        self.mainWindow = mainWindow
        self.zhTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.zhTable.setStyleSheet("selection-background-color:rgb(255,209,128)")
        self.loadData()
        self.zhTable.resizeColumnsToContents()
        self.escButton.clicked.connect(self.onescButtonClicked)

    def loadData(self):
        self.conn = mdb_conn(self.mdb)
        if self.conn == None:
            QMessageBox.critical(self, "错误", "无法连接到数据库{}!".format(self.mdb), QMessageBox.Yes, QMessageBox.Yes)
            return
        sqlstr = "select * from dizhendizhizaihai"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        zhsdata = cursor.fetchall()
        num = len(zhsdata)
        self.zhTable.setRowCount(num)
        self.zhTable.setColumnCount(9)
        self.zhTable.setHorizontalHeaderLabels(
            ['OBJECTID', '控制点编号', '经度（°）', '纬度（°）', '崩塌、滑坡', '断层地表位错', '砂土液化', '软土震陷', '地震地质灾害危险程度'])
        n = 0
        for zh in zhsdata:
            # zktable
            zkid = QTableWidgetItem(str(zh[0]))
            zkid.setTextAlignment(Qt.AlignCenter)
            zkno = QTableWidgetItem(str(zh[1]))
            zkno.setTextAlignment(Qt.AlignCenter)
            zklon = QTableWidgetItem(str(zh[2]))
            zklon.setTextAlignment(Qt.AlignCenter)
            zklat = QTableWidgetItem(str(zh[3]))
            zklat.setTextAlignment(Qt.AlignCenter)
            bthp = QTableWidgetItem(str(zh[4]))
            bthp.setTextAlignment(Qt.AlignCenter)
            dcdbcw = QTableWidgetItem(str(zh[5]))
            dcdbcw.setTextAlignment(Qt.AlignCenter)
            styh = QTableWidgetItem(str(zh[6]))
            styh.setTextAlignment(Qt.AlignCenter)
            rtzx = QTableWidgetItem(str(zh[7]))
            rtzx.setTextAlignment(Qt.AlignCenter)
            wxcd = QTableWidgetItem(str(zh[8]))
            wxcd.setTextAlignment(Qt.AlignCenter)
            self.zhTable.setItem(n, 0, zkid)
            self.zhTable.setItem(n, 1, zkno)
            self.zhTable.setItem(n, 2, zklon)
            self.zhTable.setItem(n, 3, zklat)
            self.zhTable.setItem(n, 4, bthp)
            self.zhTable.setItem(n, 5, dcdbcw)
            self.zhTable.setItem(n, 6, styh)
            self.zhTable.setItem(n, 7, rtzx)
            self.zhTable.setItem(n, 8, wxcd)
            n += 1
        self.conn.close()

    def onescButtonClicked(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    appWindow = DZZH(r"C:\Users\user\Desktop\地质管理系统\ui\anping.mdb", None)
    appWindow.show()
    app.exec_()
