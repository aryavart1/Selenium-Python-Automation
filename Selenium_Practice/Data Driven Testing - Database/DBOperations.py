# insert , update, delete

insert_query="insert into student values(104,'Kim')"
update_query="update student set sname='Mary' where sid=104"
delete_query="delete from student where sid=104"

import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3307,user="root",passwd="root",database="mydb")
    curs=con.cursor()  # create curosor
    curs.execute(delete_query)  #execute query through cursor
    con.commit() # commit transaction
    con.close()
except:
    print("Connection unsuccessful...")

print("Finished.....")