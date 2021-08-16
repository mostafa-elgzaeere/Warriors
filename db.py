from peewee import *
import datetime


db=MySQLDatabase("mydb",user="root",password="Aa123456789",host="localhost",port=3306)


class Player(Model):
    name=CharField(null=False,unique=False)
    age=IntegerField(null=False)
    phone=BigIntegerField(null=False)

    sport=CharField(null=False)

    sub_price = IntegerField(null=True)
    sub_type = CharField(null=True)


    start_at = DateTimeField(default=datetime.datetime.now)
    end_at = DateTimeField(default=datetime.datetime.now)


    in_diet=CharField(max_length=100)

    other=CharField(max_length=300,null=True ,default=" ")
    class Meta:
        database = db


class sales(Model):
    title = CharField( null=False, unique=False )
    price   = IntegerField( null=False )
    happend_at = DateTimeField(default=datetime.datetime.now)
    count=IntegerField( null=False )

    class Meta:
        database = db


class masrofat(Model):
    title = CharField( null=False, unique=False )
    price   = DecimalField( null=False )
    happend_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db





db.connect()
db.create_tables([Player,sales,masrofat])

