import sqlite3
import os
import sys

connection = sqlite3.connect('events.db')

def TopXSimpleLTVCustomers(x):
    db = connection.cursor()
    db.execute("CREATE TEMPORARY TABLE ORDERSTEMP AS SELECT CUSTOMER_ID, SUM(TOTAL_AMOUNT) AS TOTALAMOUNT FROM ORDERS GROUP BY CUSTOMER_ID")
    connection.commit()
    db.execute("CREATE TEMPORARY TABLE VISITTEMP AS SELECT CUSTOMER_ID, COUNT(1) AS TOTALVISITS, (COUNT(1)/7)+1 AS TOTALVISITSWEEK FROM VISIT GROUP BY CUSTOMER_ID")
    connection.commit()
    db.execute("CREATE TEMPORARY TABLE RESULT AS SELECT ORDERSTEMP.CUSTOMER_ID, round((52*(TOTALAMOUNT/TOTALVISITS)*TOTALVISITSWEEK*10),3) AS LTV FROM ORDERSTEMP, VISITTEMP ON ORDERSTEMP.CUSTOMER_ID = VISITTEMP.CUSTOMER_ID ")
    connection.commit()

    result = db.execute("SELECT \"CUSTOMER_ID\",\"LTV\" UNION SELECT cast(CUSTOMER_ID as text) as CUSTOMER_ID, cast(LTV as text) as LTV FROM result order by LTV desc limit %s" % x)
    connection.commit()
    return result

if __name__ == "__main__":
    #main(sys.argv[1:])

    db = connection.cursor()

    curr_dir = os.getcwd().split('/')
    dir_path = '/'.join(curr_dir[:-1])
    outputdata = os.path.join(dir_path, 'output/output.txt')

    x= sys.argv[1:][0]
    result = TopXSimpleLTVCustomers(x)

    outputfile = open(outputdata,"w")


    writeRow = ""
    for item in result:
        writeRow = ",".join(item)
        outputfile.write("%s\n" % writeRow)


    connection.close()

