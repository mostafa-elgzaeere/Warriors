import sys
import mysql.connector
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.uic       import loadUiType
from os              import path
import PyQt5.sip
import sip

from untitled import Ui_MainWindow

stock_item={"",}
class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Warriors Academy")
        self.comboBox_14.activated.connect( self.set_maximum_in_count )


        self.data_base_connect()
        self.buttons_action()
        self.hide_tabWidget()
        self.show_stocks()
        self.show_all_players()
        self.show_players_in_crossfit()
        self.show_players_in_barkor()
        self.show_players_in_mma()
        self.show_players_in_karate()
        self.show_players_in_kungfu()
        self.show_players_in_boxing()
        self.show_players_in_fittnes()
        self.show_players_in_jumbaz()
        self.show_players_in_muaythai()
        self.show_players_in_ballet()
        self.show_players_in_airobics()
        self.show_players_in_foodsystem()
        self.show_players_in_taekwondo()

        self.show_sales()
        self.show_masrofat()

        self.load_stocks_in_combo()


    # connect data base
    def data_base_connect(self):
        self.db=mysql.connector.connect(db="mydb",user="root",host="localhost",password="Aa123456789")
        self.curs=self.db.cursor()

    # connnect buttons and methods
    def buttons_action(self):
        #  open pages
        self.pushButton.clicked.connect(self.open_home)
        self.pushButton_2.clicked.connect(self.open_players)

        self.pushButton_21.clicked.connect(self.open_crossfit)
        self.pushButton_23.clicked.connect(self.open_fittnes)
        self.pushButton_15.clicked.connect(self.open_jumbaz)

        self.pushButton_17.clicked.connect(self.open_boxing)
        self.pushButton_16.clicked.connect(self.open_karate)
        self.pushButton_18.clicked.connect(self.open_taekwondo)

        self.pushButton_22.clicked.connect(self.open_kungfu)
        self.pushButton_20.clicked.connect(self.open_mma)
        self.pushButton_24.clicked.connect(self.open_foodsystem)

        self.pushButton_19.clicked.connect(self.open_barkor)
        self.pushButton_14.clicked.connect(self.open_muaythai)
        self.pushButton_13.clicked.connect(self.open_ballet)
        self.pushButton_12.clicked.connect(self.open_airobics)
        #------------------------------------------------------#

        #actions in players page
        self.pushButton_25.clicked.connect(self.search_in_all_players)

        self.pushButton_26.clicked.connect(self.add_player)

        self.pushButton_28.clicked.connect(self.search_in_update_player)
        self.pushButton_27.clicked.connect(self.update_player)

        self.pushButton_29.clicked.connect(self.search_in_delete_player)
        self.pushButton_30.clicked.connect(self.delete_player)
        #------------------------------------------------------#

        #actions_in_sports_pages
        self.pushButton_31.clicked.connect(self.search_in_crossfit)
        self.pushButton_32.clicked.connect(self.search_in_barkor)
        self.pushButton_34.clicked.connect(self.search_in_mma)
        self.pushButton_33.clicked.connect(self.search_in_karate)
        self.pushButton_35.clicked.connect(self.search_in_taekwondo)
        self.pushButton_36.clicked.connect(self.search_in_kungfu)
        self.pushButton_37.clicked.connect(self.search_in_boxing)
        self.pushButton_38.clicked.connect(self.search_in_fittnes)
        self.pushButton_39.clicked.connect(self.search_in_jumbaz)
        self.pushButton_40.clicked.connect(self.search_in_muaythai)
        self.pushButton_41.clicked.connect(self.search_in_ballet)
        self.pushButton_42.clicked.connect(self.search_in_airobics)
        self.pushButton_43.clicked.connect(self.search_in_foodsystem)
        self.pushButton_44.clicked.connect(self.search_dalete_player_from_foodsystem)
        self.pushButton_45.clicked.connect(self.dalete_player_from_foodsystem)
        self.pushButton_49.clicked.connect(self.ok_in_update_search)



        #------------------------------------------------------#
        self.pushButton_46.clicked.connect(self.admin_permision_to_update)
        self.pushButton_47.clicked.connect(self.admin_permision_to_delete)
        self.pushButton_48.clicked.connect(self.admin_permision_to_delete_food)


        #-------------------------------------------------------#
        self.pushButton_3.clicked.connect(self.open_sales_page)
        self.pushButton_6.clicked.connect(self.open_masrofat_page)
        self.pushButton_7.clicked.connect(self.open_arbah_page)
        self.pushButton_51.clicked.connect(self.add_sales)
        self.pushButton_50.clicked.connect(self.add_masrofta)
        self.pushButton_4.clicked.connect(self.safy_arbah)
        self.pushButton_52.clicked.connect(self.collect_sales)
        self.pushButton_53.clicked.connect(self.collect_masrofat)
        self.pushButton_5.clicked.connect(self.arbah)
        self.pushButton_54.clicked.connect(self.delete_last_sale)
        self.pushButton_55.clicked.connect(self.delete_last_masrof)
        self.pushButton_56.clicked.connect(self.add_to_stock)
        self.pushButton_8.clicked.connect(self.open_stock)
        self.pushButton_58.clicked.connect(self.search_update_stock)
        self.pushButton_57.clicked.connect(self.update_stock)



    def open_sales_page(self):
        self.tabWidget.setCurrentIndex( 15 )
    def open_masrofat_page(self):
        self.tabWidget.setCurrentIndex( 16 )
    def open_arbah_page(self):
        self.tabWidget.setCurrentIndex( 17 )



    def add_sales(self):

        title = self.comboBox_14.currentText()
        price = self.lineEdit_33.text()
        count=self.spinBox.value()
        start = self.dateEdit_6.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        happend_at = f"{start_year}-{start_month}-{start_day}"

        try:
            total = int( self.spinBox.value() ) * int( self.lineEdit_33.text() )

            self.curs.execute( '''INSERT INTO sales (title,price,happend_at,count)
                                              VALUES (%s,%s,%s,%s)''',
                               (title, total, happend_at,count) )
            self.db.commit()
            QMessageBox.information( self, "Successful", "Add sale" )

            self.show_sales()
            self.collect_sales()

        except Exception as e :
            print(e)
            QMessageBox.warning( self, "Noooo", "please write a rightly data " )

        try:
            title = self.comboBox_14.currentText()
            sql=''' SELECT quantity FROM Stock WHERE title=%s '''
            val=(title,)
            self.curs.execute(sql,val)

            data=self.curs.fetchall()

            stock_quantity=data[0][0]
            sale_quantity=self.spinBox.value()
            safy=stock_quantity-sale_quantity
            print(safy)
            sql_2 = ''' UPDATE Stock SET quantity=%s WHERE title=%s'''
            val_2=(safy,title)
            if safy<1:
                sql_3='''DELETE FROM Stock WHERE title=%s'''
                val_3=(title,)
                self.curs.execute(sql_3,val_3)
                self.db.commit()

            self.curs.execute( sql_2, val_2 )
            self.db.commit()
        except:
            QMessageBox.warning( self, "Noooo", "this product not in stock" )

        self.show_stocks()
        self.comboBox_14.clear()
        self.load_stocks_in_combo()

        self.lineEdit_33.setText( " " )
        self.lineEdit_38.setText( " " )
        self.spinBox.setValue(1)
        self.tableWidget_17.clear()
        self.pushButton_51.setEnabled( False )

    def set_maximum_in_count(self):
        title = self.comboBox_14.currentText()
        sql = ''' SELECT quantity FROM Stock WHERE title=%s '''
        val = (title,)
        self.curs.execute( sql, val )
        data = self.curs.fetchall()
        try:
            stock_quantity = data[0][0]
            self.spinBox.setMaximum(stock_quantity)
            self.pushButton_51.setEnabled(True)
        except:
            QMessageBox.warning( self, "Noooo", "this product not in stock" )


    def show_sales(self):
        self.tableWidget_16.setRowCount( 0 )
        self.tableWidget_16.setRowCount( 2000 )
        self.tableWidget_16.insertRow( 0 )
        self.curs.execute( '''SELECT title , count ,price , happend_at FROM sales ''' )
        data = self.curs.fetchall()

        for current_row, row_item in enumerate( data ):
            for current_column, column_item in enumerate( row_item ):
                self.tableWidget_16.setItem( current_row, current_column, QTableWidgetItem( str( column_item ) ) )
                current_column += 1
        row_position = self.tableWidget_16.rowCount()
        self.tableWidget_16.insertRow( row_position )



    def collect_sales(self):
        self.tableWidget_17.clear()
        start = self.dateEdit_7.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        start_at = f"{start_year}-{start_month}-{start_day}"

        end = self.dateEdit_8.date()
        end_day = end.day()
        end_month = end.month()
        end_year = end.year()
        end_at = f"{end_year}-{end_month}-{end_day}"

        sql='''SELECT price FROM sales WHERE happend_at BETWEEN %s And %s '''
        val=(start_at,end_at)
        self.curs.execute( sql,val )
        data = self.curs.fetchall()
        sales=[]
        for i in data:
            sales.append(i[0])

        self.lineEdit_38.setText(str(sum(sales)))

        sql_2 = '''SELECT title , count , price FROM sales WHERE happend_at BETWEEN %s And %s '''
        val_2 = (start_at, end_at)
        self.curs.execute( sql_2, val_2 )

        data_2 = self.curs.fetchall()
        if len(data_2)>0:
            for current_row, row_item in enumerate( data_2 ):
                for current_column, column_item in enumerate( row_item ):
                    self.tableWidget_17.setItem( current_row, current_column, QTableWidgetItem( str( column_item ) ) )
                    current_column += 1
            row_position = self.tableWidget_17.rowCount()
            self.tableWidget_17.insertRow( row_position )

        else:self.tableWidget_17.setRowCount(1)




    def delete_last_sale(self):
        self.curs.execute(''' DELETE from sales order by id desc limit 1 ''')
        self.db.commit()
        self.show_sales()


    def add_masrofta(self):
        title = self.lineEdit_34.text()
        price = self.lineEdit_32.text()

        start = self.dateEdit_5.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        happend_at = f"{start_year}-{start_month}-{start_day}"
        try:
            self.curs.execute( '''INSERT INTO masrofat (title,price,happend_at)
                                                 VALUES (%s,%s,%s)''',
                               (title, price, happend_at) )
            self.db.commit()
            QMessageBox.information( self, "Successful", "Add sale" )

            self.show_masrofat()
            self.collect_masrofat()

        except:
            QMessageBox.warning( self, "Noooo", "please write a rightly data " )

        self.lineEdit_34.setText( " " )
        self.lineEdit_32.setText( " " )

    def show_masrofat(self):
        self.tableWidget_15.setRowCount( 0 )
        self.tableWidget_15.setRowCount( 2000 )
        self.tableWidget_15.insertRow( 0 )
        self.curs.execute( '''SELECT title , price , happend_at FROM masrofat ''' )
        data = self.curs.fetchall()

        for current_row, row_item in enumerate( data ):
            for current_column, column_item in enumerate( row_item ):
                self.tableWidget_15.setItem( current_row, current_column, QTableWidgetItem( str( column_item ) ) )
                current_column += 1
        row_position = self.tableWidget_15.rowCount()
        self.tableWidget_15.insertRow( row_position )

    def collect_masrofat(self):
        start = self.dateEdit_9.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        start_at = f"{start_year}-{start_month}-{start_day}"

        end = self.dateEdit_10.date()
        end_day = end.day()
        end_month = end.month()
        end_year = end.year()
        end_at = f"{end_year}-{end_month}-{end_day}"

        sql = '''SELECT price FROM masrofat WHERE happend_at BETWEEN %s And %s '''
        val = (start_at, end_at)
        self.curs.execute( sql, val )
        data = self.curs.fetchall()
        sales = []
        for i in data:
            sales.append( i[0] )
            print( i[0] )

        self.lineEdit_37.setText( str( sum( sales ) ) )

    def delete_last_masrof(self):
        self.curs.execute( ''' DELETE from masrofat order by id desc limit 1 ''' )
        self.db.commit()
        self.show_masrofat()

    #
    def arbah(self):

        sport=self.comboBox_12.currentText()
        start = self.dateEdit_12.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        start_at = f"{start_year}-{start_month}-{start_day}"

        end = self.dateEdit_11.date()
        end_day = end.day()
        end_month = end.month()
        end_year = end.year()
        end_at = f"{end_year}-{end_month}-{end_day}"

        sql='''select sub_price from Player WHERE sport=%s And start_at BETWEEN %s And %s And end_at BETWEEN %s And %s   '''
        val=(sport,start_at,end_at,start_at,end_at)
        self.curs.execute(sql,val)
        data = self.curs.fetchall()
        sales = []
        for i in data:
            sales.append( i[0] )
        self.lineEdit_25.setText( str( sum( sales ) ) )

        self.lineEdit_26.setText(" ")
        self.lineEdit_28.setText(" ")


    def safy_arbah(self):
        sport_rbh = self.lineEdit_25.text()
        modarb = self.lineEdit_26.text()
        try:
            mortb_elmodrb = float( sport_rbh ) * float( modarb ) / 100
            safy_rebah=float( sport_rbh ) - float( mortb_elmodrb )
            self.lineEdit_28.setText(str(safy_rebah))

        except:
            QMessageBox.warning( self, "Noooo", "please write a rightly data " )
            self.lineEdit_25.setText( " " )
            self.lineEdit_26.setText( " " )
            self.lineEdit_28.setText( " " )




    def open_stock(self):
        self.tabWidget.setCurrentIndex(18)

    def add_to_stock(self):
        title=self.lineEdit_40.text()
        one_pice=self.lineEdit_41.text()
        start = self.dateEdit_13.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        date = f"{start_year}-{start_month}-{start_day}"
        quantity=int(self.spinBox_2.value())



        if quantity>0:
            try:
                total = int( self.spinBox_2.value() ) * int( self.lineEdit_41.text() )
                self.curs.execute( '''INSERT INTO Stock (title,price,date,quantity,one_pice)
                                               VALUES (%s,%s,%s,%s,%s)''',
                               (title, total, date, quantity,one_pice) )
                self.db.commit()
                QMessageBox.information( self, "ok", "Added to Stock " )
            except:
                QMessageBox.warning( self, "Noooo", "Its an Correct Password Please Connect with Owner " )
        else:
            QMessageBox.warning( self, "Noooo", "quantity must be a big" )

        self.lineEdit_40.setText(" ")
        self.lineEdit_41.setText(" ")
        self.spinBox_2.setValue(1)

        self.show_stocks()
        self.comboBox_13.clear()
        self.comboBox_14.clear()

        self.load_stocks_in_combo()

    def load_stocks_in_combo(self):
        x=set(stock_item)
        for i in x:
            self.comboBox_13.addItem(i)
            self.comboBox_14.addItem(i)

    def search_update_stock(self):
        title_search=self.comboBox_13.currentText()
        sql=''' SELECT title , one_pice , quantity , date FROM Stock WHERE title=%s '''
        val=(title_search,)
        self.curs.execute(sql,val)

        data = self.curs.fetchall()

        for i in data:
            self.lineEdit_43.setText(i[0])
            self.lineEdit_42.setText(str(i[1]))
            self.spinBox_3.setValue(i[2])
            self.dateEdit_14.setDateTime(i[3] )




    def update_stock(self):
        title_search=self.comboBox_13.currentText()
        title=self.lineEdit_43.text()
        quantity=self.spinBox_3.value()
        start = self.dateEdit_14.date()
        start_day = start.day()
        start_month = start.month()
        start_year = start.year()
        date = f"{start_year}-{start_month}-{start_day}"
        one_pice=str(self.lineEdit_42.text())


        try:
            total = int( self.spinBox_3.value() ) * int(float(self.lineEdit_42.text())  )

            sql=''' UPDATE Stock SET title=%s , quantity=%s , date=%s , price=%s ,one_pice=%s WHERE title=%s'''
            val=(title,quantity,date,total,one_pice,title_search)
            self.curs.execute(sql,val)
            self.db.commit()
            self.show_stocks()
            self.comboBox_13.clear()
            self.lineEdit_43.setText(" ")
            self.lineEdit_42.setText( " " )
            self.spinBox_3.setValue(1)
            self.comboBox_14.clear()

            self.load_stocks_in_combo()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Noooo", "Its an Correct Password Please Connect with Owner ")


    def show_stocks(self):
        self.tableWidget_18.setRowCount( 0 )
        self.tableWidget_18.setRowCount( 2000 )
        self.tableWidget_18.insertRow( 0 )
        self.curs.execute( '''SELECT title , quantity , price ,  date  FROM stock WHERE quantity>0''' )
        data = self.curs.fetchall()


        for current_row, row_item in enumerate( data ):
            for current_column, column_item in enumerate( row_item ):
                stock_item.add(row_item[0])
                self.tableWidget_18.setItem( current_row, current_column, QTableWidgetItem( str( column_item ) ) )
                current_column += 1
        row_position = self.tableWidget_18.rowCount()
        self.tableWidget_18.insertRow( row_position )



    #------------------------------------------------------------------------------------------------------------------#
    def admin_permision_to_update(self):
        if self.lineEdit_29.text()=="lr+ar.lar":
            self.pushButton_27.setEnabled(True)
        else:
            QMessageBox.warning(self, "Noooo", "Its an Correct Password Please Connect with Owner ")


    def admin_permision_to_delete(self):
        if self.lineEdit_30.text()=="lr+ar.lar":
            self.pushButton_30.setEnabled(True)
        else:
            QMessageBox.warning(self, "Noooo", "Its an Correct Password Please Connect with Owner ")



    def admin_permision_to_delete_food(self):
        if self.lineEdit_31.text()=="lr+ar.lar":
            self.pushButton_45.setEnabled(True)
        else:
            QMessageBox.warning(self, "Noooo", "Its an Correct Password Please Connect with Owner ")


    # hide tabbar in tabWidget
    def hide_tabWidget(self):
        self.tabWidget.tabBar().setVisible(False)



    #open pages
    def open_home(self):
        self.tabWidget.setCurrentIndex(0)

    def open_players(self):
        self.tabWidget.setCurrentIndex(1)

    def open_crossfit(self):
        self.tabWidget.setCurrentIndex(2)

    def open_barkor(self):
        self.tabWidget.setCurrentIndex(3)

    def open_mma(self):
        self.tabWidget.setCurrentIndex(4)

    def open_karate(self):
        self.tabWidget.setCurrentIndex(5)

    def open_taekwondo(self):
        self.tabWidget.setCurrentIndex(6)

    def open_kungfu(self):
        self.tabWidget.setCurrentIndex(7)

    def open_boxing(self):
        self.tabWidget.setCurrentIndex(8)

    def open_fittnes(self):
        self.tabWidget.setCurrentIndex(9)

    def open_jumbaz(self):
        self.tabWidget.setCurrentIndex(10)

    def open_muaythai(self):
        self.tabWidget.setCurrentIndex(11)

    def open_ballet(self):
        self.tabWidget.setCurrentIndex(12)

    def open_airobics(self):
        self.tabWidget.setCurrentIndex(13)

    def open_foodsystem(self):
        self.tabWidget.setCurrentIndex(14)




    #show all players
    def show_all_players(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(2000)
        self.tableWidget.insertRow(0)
        self.curs.execute('''
                    SELECT name , sport , phone , age , sub_price , start_at , end_at , sub_type , in_diet , other FROM Player
                ''')
        data = self.curs.fetchall()
         
        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column+=1
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

    #search in pages
    def search_in_all_players(self):
        phone_search=self.lineEdit.text()
        if phone_search=="":
            self.show_all_players()
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql=(''' SELECT name , sport , phone , age , sub_price , start_at , end_at , sub_type , in_diet , other FROM Player
                      WHERE phone=%s ''')
            values=(phone_search,)
            self.curs.execute(sql,values)
            data = self.curs.fetchall()
            self.tableWidget.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)


    def search_in_update_player(self):
        self.comboBox_8.clear()
        self.comboBox_9.clear()

        search_phone=self.lineEdit_10.text()

        if search_phone=="":
            QMessageBox.warning(self, "Noooo", "you should write phone number")
        else:

            try:
                sql = '''SELECT name FROM Player WHERE phone=%s '''
                val = (search_phone,)
                self.curs.execute(sql, val)
                data = self.curs.fetchall()
                for x in data:
                    self.comboBox_9.addItem(str(x)[2:-3] )

                sql = '''SELECT sport FROM Player WHERE phone=%s '''
                val = (search_phone,)
                self.curs.execute( sql, val )
                data = self.curs.fetchall()
                for x in data:
                    self.comboBox_8.addItem( str( x )[2:-3] )


            except :
                pass


    def ok_in_update_search(self):

        search_phone=self.lineEdit_10.text()
        name=self.comboBox_9.currentText()
        sport=self.comboBox_8.currentText()

        name_search = self.comboBox.currentText()
        sql = '''SELECT name,age,phone,sport,sub_price,sub_type,start_at,end_at,in_diet,other FROM Player WHERE phone=%s AND name=%s AND sport=%s'''
        val = (search_phone,name,sport)
        self.curs.execute( sql, val )

        data = self.curs.fetchall()
        for i in data:
            self.lineEdit_7.setText( str( i[0] ) )
            self.lineEdit_8.setText( str( i[1] ) )
            self.lineEdit_6.setText( "0" + str( i[2] ) )
            self.lineEdit_9.setText( str( i[4] ) )
            self.dateEdit_3.setDateTime( i[6] )
            self.dateEdit_4.setDateTime( i[7] )
            self.comboBox_8.addItem( str( i[3] ) )
            self.lineEdit_39.setText(str (i[9]) )

            if i[5] == "Daily":
                self.comboBox_4.setCurrentIndex( 0 )
            if i[5] == "Monthly":
                self.comboBox_4.setCurrentIndex( 1 )
            if i[5] == "3 Months":
                self.comboBox_4.setCurrentIndex( 2 )
            if i[5] == "6 Months":
                self.comboBox_4.setCurrentIndex( 3 )
            if i[5] == "Yearly":
                self.comboBox_4.setCurrentIndex( 4 )

            if i[3] == "CrossFit":
                self.comboBox_5.setCurrentIndex( 0 )
            if i[3] == "Barkor":
                self.comboBox_5.setCurrentIndex( 1 )
            if i[3] == "MMA":
                self.comboBox_5.setCurrentIndex( 2 )
            if i[3] == "Karate":
                self.comboBox_5.setCurrentIndex( 3 )
            if i[3] == "Taekwondo":
                self.comboBox_5.setCurrentIndex( 4 )
            if i[3] == "KungFu":
                self.comboBox_5.setCurrentIndex( 5 )
            if i[3] == "Fittnes":
                self.comboBox_5.setCurrentIndex( 6 )
            if i[3] == "Jumbaz":
                self.comboBox_5.setCurrentIndex( 7 )
            if i[3] == "MuayThai":
                self.comboBox_5.setCurrentIndex( 8 )
            if i[3] == "Ballet":
                self.comboBox_5.setCurrentIndex( 9 )
            if i[3] == "Aerobics":
                self.comboBox_5.setCurrentIndex( 10 )
            if i[3] == "Boxing":
                self.comboBox_5.setCurrentIndex( 11 )

            if i[-1] == "Yes":
                self.comboBox_6.setCurrentIndex( 0 )
            if i[-1] == "No":
                self.comboBox_6.setCurrentIndex( 1 )


    # QMessageBox.warning(self, "Noooo", "please check the phone number ")

    def search_in_delete_player(self):
      self.comboBox_7.clear()
      self.comboBox_10.clear()
      if self.lineEdit_11.text()=="":
          QMessageBox.warning(self, "Noooo", "you should write phone number")
      else:
          search_phone = self.lineEdit_11.text()
          sql = '''SELECT name FROM Player WHERE phone=%s'''
          self.curs.execute(sql, [(search_phone)])
          data=self.curs.fetchall()
          for i in data:
              self.comboBox_10.addItem(str(i)[2:-3])
          sqll = '''SELECT sport FROM Player WHERE phone=%s'''
          vall = (search_phone,)
          self.curs.execute(sqll, vall)
          data = self.curs.fetchall()
          for x in data:
              self.comboBox_7.addItem(str(x)[2:-3])

####################################crossFit######################################################################

    def show_players_in_crossfit(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setRowCount(2000)
        self.tableWidget_2.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
        in_diet ,other FROM Player WHERE sport='CrossFit' ''')
        data = self.curs.fetchall()
        self.progressBar.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_2.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(row_position)

    def search_in_crossfit(self):
        phone_search = self.lineEdit_12.text()
        if phone_search == "":
            self.show_players_in_crossfit()
        else:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                             WHERE phone=%s AND sport='CrossFit' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_2.setRowCount(len(data))
             
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_2.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)


#########################Barkor##########################################################################
    def show_players_in_barkor(self):
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setRowCount(2000)
        self.tableWidget_3.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                in_diet ,other FROM Player WHERE sport='Barkor' ''')
        data = self.curs.fetchall()
        self.progressBar_2.setValue(len(data))

         
        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_3.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)

    def search_in_barkor(self):
        phone_search = self.lineEdit_13.text()
        if phone_search == "":
            self.show_players_in_barkor()
        else:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                 WHERE phone=%s AND sport='Barkor' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_3.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_3.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)

##################################MMA####################################################
    def show_players_in_mma(self):
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.setRowCount(2000)
        self.tableWidget_5.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                     in_diet ,other FROM Player WHERE sport='MMA' ''')
        data = self.curs.fetchall()
        self.progressBar_3.setValue(len(data))

         
        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_5.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_5.rowCount()
        self.tableWidget_5.insertRow(row_position)

    def search_in_mma(self):
        phone_search = self.lineEdit_15.text()
        if phone_search == "":
            self.show_players_in_mma()
        else:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                       WHERE phone=%s AND sport='MMA' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()

            self.tableWidget_5.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_5.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)



#########################Karate##########################################################################
    def show_players_in_karate(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setRowCount(2000)
        self.tableWidget_4.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                             in_diet ,other FROM Player WHERE sport='Karate' ''')
        data = self.curs.fetchall()
        self.progressBar_4.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_4.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_4.rowCount()
        self.tableWidget_4.insertRow(row_position)

    def search_in_karate(self):
        phone_search = self.lineEdit_14.text()
        if phone_search == "":
            self.show_players_in_karate()
        else:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                             WHERE phone=%s AND sport='Karate' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_4.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_4.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

#########################Taekwondo##########################################################################
    def show_players_in_taekwondo(self):
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setRowCount(2000)
        self.tableWidget_6.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                     in_diet ,other FROM Player WHERE sport='Taekwondo' ''')
        data = self.curs.fetchall()
        self.progressBar_5.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_6.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_6.rowCount()
        self.tableWidget_6.insertRow(row_position)


    def search_in_taekwondo(self):
        phone_search = self.lineEdit_16.text()
        if phone_search == "":
            self.show_players_in_taekwondo()
        else:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                                    WHERE phone=%s AND sport='Taekwondo' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_6.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_6.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

#########################KungFu##########################################################################
    def show_players_in_kungfu(self):
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.setRowCount(2000)
        self.tableWidget_7.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                     in_diet ,other FROM Player WHERE sport='KungFu' ''')
        data = self.curs.fetchall()
        self.progressBar_6.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_7.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_7.rowCount()
        self.tableWidget_7.insertRow(row_position)

    def search_in_kungfu(self):
        phone_search = self.lineEdit_17.text()
        if phone_search == "":
            self.show_players_in_kungfu()
        else:
            self.tableWidget_7.setRowCount(0)
            self.tableWidget_7.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                                            WHERE phone=%s AND sport='KungFu' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_7.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_7.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)




#########################Boxing##########################################################################
    def show_players_in_boxing(self):
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.setRowCount(2000)
        self.tableWidget_8.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                        in_diet ,other FROM Player WHERE sport='Boxing' ''')
        data = self.curs.fetchall()
        self.progressBar_7.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_8.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_8.rowCount()
        self.tableWidget_8.insertRow(row_position)


    def search_in_boxing(self):
        phone_search = self.lineEdit_18.text()
        if phone_search == "":
            self.show_players_in_boxing()
        else:
            self.tableWidget_8.setRowCount(0)
            self.tableWidget_8.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                                                   WHERE phone=%s AND sport='Boxing' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_8.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_8.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_position)

#########################KickBoxing##########################################################################
    def show_players_in_fittnes(self):
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.setRowCount(2000)
        self.tableWidget_9.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                                in_diet ,other FROM Player WHERE sport='Fittnes' ''')
        data = self.curs.fetchall()
        self.progressBar_8.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_9.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_9.rowCount()
        self.tableWidget_9.insertRow(row_position)

    def search_in_fittnes(self):
        phone_search = self.lineEdit_19.text()
        if phone_search == "":
            self.show_players_in_kickboxing()
        else:
            self.tableWidget_9.setRowCount(0)
            self.tableWidget_9.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet , other FROM Player
                                                                          WHERE phone=%s AND sport='Fittnes' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_9.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_9.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_9.rowCount()
            self.tableWidget_9.insertRow(row_position)



 #########################ChineseBoxing##########################################################################

    def show_players_in_jumbaz(self):
        self.tableWidget_10.setRowCount(0)
        self.tableWidget_10.setRowCount(2000)
        self.tableWidget_10.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                                        in_diet ,other FROM Player WHERE sport='Jumbaz' ''')
        data = self.curs.fetchall()
        self.progressBar_9.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_10.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_10.rowCount()
        self.tableWidget_10.insertRow(row_position)

    def search_in_jumbaz(self):
        phone_search = self.lineEdit_20.text()
        if phone_search == "":
            self.show_players_in_chineseboxing()
        else:
            self.tableWidget_10.setRowCount(0)
            self.tableWidget_10.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                                                                  WHERE phone=%s AND sport='Jumbaz' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_10.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_10.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_10.rowCount()
            self.tableWidget_10.insertRow(row_position)

#########################MuayThai##########################################################################
    def show_players_in_muaythai(self):
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_11.setRowCount(2000)
        self.tableWidget_11.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                                                in_diet ,other FROM Player WHERE sport='MuayThai' ''')
        data = self.curs.fetchall()
        self.progressBar_10.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_11.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_11.rowCount()
        self.tableWidget_11.insertRow(row_position)

    def search_in_muaythai(self):
        phone_search = self.lineEdit_21.text()
        if phone_search == "":
            self.show_players_in_muaythai()
        else:
            self.tableWidget_11.setRowCount(0)
            self.tableWidget_11.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet ,other FROM Player
                                                                                        WHERE phone=%s AND sport='MuayThai' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_11.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_11.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_11.rowCount()
            self.tableWidget_11.insertRow(row_position)

#########################ballet##########################################################################
    def show_players_in_ballet(self):
        self.tableWidget_12.setRowCount(0)
        self.tableWidget_12.setRowCount(2000)
        self.tableWidget_12.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                                                        in_diet ,other FROM Player WHERE sport='Ballet' ''')
        data = self.curs.fetchall()
        self.progressBar_11.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_12.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_12.rowCount()
        self.tableWidget_12.insertRow(row_position)


    def search_in_ballet(self):
        phone_search = self.lineEdit_22.text()
        if phone_search == "":
            self.show_players_in_ballet()
        else:
            self.tableWidget_12.setRowCount(0)
            self.tableWidget_12.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet , other FROM Player
                                                                                                WHERE phone=%s AND sport='Ballet' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_12.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_12.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_12.rowCount()
            self.tableWidget_12.insertRow(row_position)

#########################airobics##########################################################################
    def show_players_in_airobics(self):
        self.tableWidget_13.setRowCount(0)
        self.tableWidget_13.setRowCount(2000)
        self.tableWidget_13.insertRow(0)
        self.curs.execute('''SELECT name , phone , age , sub_price , start_at , end_at , sub_type , 
                                                                             in_diet , other FROM Player WHERE sport='Aerobics' ''')
        data = self.curs.fetchall()
        self.progressBar_12.setValue(len(data))

        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_13.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_13.rowCount()
        self.tableWidget_13.insertRow(row_position)


    def search_in_airobics(self):
        phone_search = self.lineEdit_23.text()
        if phone_search == "":
            self.show_players_in_airobics()
        else:
            self.tableWidget_13.setRowCount(0)
            self.tableWidget_13.insertRow(0)
            sql = (''' SELECT name , phone , age , sub_price , start_at , end_at , sub_type , in_diet , other FROM Player
                                                                                                          WHERE phone=%s AND sport='Aerobics' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_13.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_13.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_13.rowCount()
            self.tableWidget_13.insertRow(row_position)

#########################foodsystem##########################################################################
    def show_players_in_foodsystem(self):
        self.tableWidget_14.setRowCount(0)
        self.tableWidget_14.setRowCount(2000)
        self.tableWidget_14.insertRow(0)
        self.curs.execute('''SELECT name , phone , sport , age , sub_price , sub_type , start_at , end_at , other
                                                                                     FROM Player WHERE in_diet='Yes' ''')
        data = self.curs.fetchall()
         
        for current_row, row_item in enumerate(data):
            for current_column, column_item in enumerate(row_item):
                self.tableWidget_14.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                current_column += 1
        row_position = self.tableWidget_14.rowCount()
        self.tableWidget_14.insertRow(row_position)

    def search_in_foodsystem(self):
        phone_search = self.lineEdit_24.text()
        if phone_search == "":
            self.show_players_in_foodsystem()
        else:
            self.tableWidget_14.setRowCount(0)
            self.tableWidget_14.insertRow(0)
            sql = (''' SELECT name , phone , sport,  age , sub_price , sub_type , start_at , end_at , other FROM Player
                                                                                                                  WHERE phone=%s AND ='Yes' ''')
            values = (phone_search,)
            self.curs.execute(sql, values)
            data = self.curs.fetchall()
            self.tableWidget_14.setRowCount(len(data))
            for current_row, row_item in enumerate(data):
                for current_column, column_item in enumerate(row_item):
                    self.tableWidget_14.setItem(current_row, current_column, QTableWidgetItem(str(column_item)))
                    current_column += 1
            row_position = self.tableWidget_14.rowCount()
            self.tableWidget_14.insertRow(row_position)




    #add_update_delete
    def add_player(self):
        name=self.lineEdit_2.text()
        age=self.lineEdit_3.text()
        phone=self.lineEdit_4.text()
        sub_price=self.lineEdit_5.text()
        sub_type=self.comboBox_3.currentText()

        start = self.dateEdit.date()
        start_day=start.day()
        start_month=start.month()
        start_year=start.year()
        start_at=f"{start_year}-{start_month}-{start_day}"

        end = self.dateEdit_2.date()
        end_day = end.day()
        end_month = end.month()
        end_year = end.year()
        end_at = f"{end_year}-{end_month}-{end_day}"

        in_diet=self.comboBox_2.currentText()
        sport=self.comboBox.currentText()
        other=self.lineEdit_36.text()

        try:

            self.curs.execute('''INSERT INTO Player (name,age,phone,sport,sub_price,sub_type,start_at,end_at,in_diet,other)
                                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                              (name, age, phone, sport, sub_price, sub_type, start_at
                               , end_at, in_diet,other))
            self.db.commit()

            QMessageBox.information(self, "Successful", "A player has been added successfully")

            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_36.setText("")

            self.show_all_players()
            self.show_players_in_crossfit()
            self.show_players_in_barkor()
            self.show_players_in_mma()
            self.show_players_in_karate()
            self.show_players_in_kungfu()
            self.show_players_in_boxing()
            self.show_players_in_fittnes()
            self.show_players_in_jumbaz()
            self.show_players_in_muaythai()
            self.show_players_in_ballet()
            self.show_players_in_airobics()
            self.show_players_in_foodsystem()

        except:
            QMessageBox.warning(self, "Noooo", "you should add completely and rightly data")






    def update_player(self):
            search_phone = self.lineEdit_10.text()
            search_name=self.comboBox_9.currentText()
            name = self.lineEdit_7.text()
            age = self.lineEdit_8.text()
            phone = self.lineEdit_6.text()
            sub_price = self.lineEdit_9.text()
            sub_type = self.comboBox_4.currentText()
            start = self.dateEdit_3.date()
            start_day = start.day()
            start_month = start.month()
            start_year = start.year()
            start_at = f"{start_year}-{start_month}-{start_day}"

            end = self.dateEdit_4.date()
            end_day = end.day()
            end_month = end.month()
            end_year = end.year()
            end_at = f"{end_year}-{end_month}-{end_day}"


            in_diet = self.comboBox_6.currentText()
            sport = self.comboBox_5.currentText()
            other = self.lineEdit_39.text()

            if(search_phone!="" and name !="" and age!=""and phone!="" and sub_price!=""):
                try:
                    sql = '''UPDATE Player SET name=%s ,age=%s ,phone=%s ,sport=%s ,sub_price=%s ,sub_type=%s ,start_at=%s ,end_at=%s ,in_diet=%s ,other=%s WHERE name=%s'''
                    val = (name, age, phone,sport,sub_price,sub_type,start_at,end_at,in_diet,other,search_name)
                    self.curs.execute(sql, val)
                    self.db.commit()
                    QMessageBox.information(self, "Successful", "A player data has been updated ")
                    self.lineEdit_10.setText("")
                    self.lineEdit_7.setText("")
                    self.lineEdit_8.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_9.setText("")
                    self.lineEdit_39.setText( "" )
                    self.comboBox_4.setCurrentIndex(0)
                    self.lineEdit_29.setText("")
                    self.comboBox_9.clear()
                    self.comboBox_8.clear()
                    self.pushButton_27.setEnabled(False)

                    self.show_all_players()
                    self.show_players_in_crossfit()
                    self.show_players_in_barkor()
                    self.show_players_in_mma()
                    self.show_players_in_karate()
                    self.show_players_in_kungfu()
                    self.show_players_in_boxing()
                    self.show_players_in_fittnes()
                    self.show_players_in_jumbaz()
                    self.show_players_in_muaythai()
                    self.show_players_in_taekwondo()
                    self.show_players_in_ballet()
                    self.show_players_in_airobics()
                    self.show_players_in_foodsystem()





                except:
                    QMessageBox.warning(self, "Noooo", "please write a rightly data ")


            else:
                QMessageBox.warning(self, "Noooo", "please write a completely and rightly data ")




    def delete_player(self):
        if self.lineEdit_11.text() == "":
            QMessageBox.warning(self, "Noooo", "you should write phone number")
        else:
            try:
                search_phone = self.lineEdit_11.text()
                sport=self.comboBox_7.currentText()
                search_name=self.comboBox_10.currentText()
                msg = QMessageBox.warning(self, "Delete Player", "Are you sure you want to delete this player ? ",
                                          QMessageBox.Yes | QMessageBox.No)
                if msg == QMessageBox.Yes:
                    sql = '''DELETE FROM Player WHERE phone=%s AND sport=%s AND name=%s'''
                    self.curs.execute(sql, (search_phone,sport,search_name))
                    self.db.commit()
                    QMessageBox.information(self, "Successful", "A player has been deleted")
                    self.lineEdit_11.setText("")
                    self.comboBox_7.clear()
                    self.comboBox_10.clear()
                    self.lineEdit_30.setText("")
                    self.pushButton_30.setEnabled(False)




                    self.show_all_players()
                    self.show_players_in_crossfit()
                    self.show_players_in_barkor()
                    self.show_players_in_mma()
                    self.show_players_in_karate()
                    self.show_players_in_kungfu()
                    self.show_players_in_boxing()
                    self.show_players_in_fittnes()
                    self.show_players_in_jumbaz()
                    self.show_players_in_muaythai()
                    self.show_players_in_ballet()
                    self.show_players_in_airobics()
                    self.show_players_in_foodsystem()


            except Exception as e:
                    print(e)


    def search_dalete_player_from_foodsystem(self):
        phone=self.lineEdit_27.text()
        if phone == "":
            QMessageBox.warning(self, "Noooo", "you should write phone number")
        else:
            try:
                sql='''SELECT name FROM Player WHERE phone=%s AND in_diet='Yes' '''
                self.curs.execute(sql, [(phone)])
                data=self.curs.fetchall()
                for i in data:
                    self.comboBox_11.addItem(str(i)[2:-3])

            except:
                QMessageBox.warning(self, "Noooo", "you should write rightly phone number")


    def dalete_player_from_foodsystem(self):
        phone=self.lineEdit_27.text()
        name=self.comboBox_11.currentText()
        if phone=="":
            QMessageBox.warning(self, "Noooo", "you should write phone number")
        else:
            try:
                sql = '''UPDATE Player SET in_diet='No' WHERE phone=%s AND name=%s'''
                self.curs.execute(sql, (phone,name))
                self.db.commit()
                self.lineEdit_27.setText("")
                self.lineEdit_31.setText("")
                self.comboBox_11.clear()
                self.pushButton_45.setEnabled(False)
                self.show_all_players()
                self.show_players_in_crossfit()
                self.show_players_in_barkor()
                self.show_players_in_mma()
                self.show_players_in_karate()
                self.show_players_in_kungfu()
                self.show_players_in_boxing()
                self.show_players_in_fittnes()
                self.show_players_in_jumbaz()
                self.show_players_in_muaythai()
                self.show_players_in_ballet()
                self.show_players_in_airobics()
                self.show_players_in_foodsystem()


            except:
                 QMessageBox.warning(self, "Noooo", "you should write rightly phone number")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__': main()
