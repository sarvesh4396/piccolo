from piccolo import table
from piccolo import columns
from piccolo.engine import PostgresEngine


DB = PostgresEngine({
    'host': 'localhost',
    'database': 'piccolo',
    'user': 'piccolo',
    'password': 'piccolo'
})


###############################################################################
# Simple example

class Band(table.Table):
    name = columns.Varchar(length=50)
    manager = columns.Varchar(length=20)
    power = columns.Integer()

    class Meta():
        db = DB


class Manager(table.Table):
    name = columns.Varchar(length=50)

    class Meta():
        db = DB


###############################################################################
# More complex

class Venue(table.Table):
    name = columns.Varchar(length=100)
    capacity = columns.Integer()

    class Meta():
        db = DB


class Concert(table.Table):
    band_1 = columns.ForeignKey(Band)
    band_2 = columns.ForeignKey(Band)
    venue = columns.ForeignKey(Venue)

    class Meta():
        db = DB
