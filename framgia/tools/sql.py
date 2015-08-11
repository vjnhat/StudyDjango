__author__ = 'FRAMGIA\le.cong.phuc'
from django.db import connection


def query_add(self,table_name,columns):
    cr = connection.cursor()

    cr.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])

    cr.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cr.fetchone()

    return row