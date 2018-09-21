import sqlite3
import ast
import os

connection = sqlite3.connect('events.db')

def ingest(events):
    db = connection.cursor()
    for event in events:
        input_list =()
        if event['type'] == 'CUSTOMER':
            for key in event.keys():
                input_list = input_list + (event[key],)
            if event['verb'] == 'NEW':
                db.execute('INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?,?)', input_list)
            #print(input_list)
            elif event['verb'] =='UPDATE':
                db.execute('UPDATE CUSTOMER SET last_name = \"'+ event['last_name']+  '\", adr_city = \"' + event['adr_city'] + '\", adr_state = \"'+ event['adr_state']+'\" where key=\"'+event['key']+'\"')


            #print("Customer")
            connection.commit()

        elif event['type'] == 'SITE_VISIT':
            for key in event.keys():
                input_list = input_list + (str(event[key]),)
            if event['verb'] == 'NEW':
                db.execute('INSERT INTO VISIT VALUES(?,?,?,?,?,?)', input_list)
            #print("Visit")
            connection.commit()

        elif event['type'] == 'IMAGE':
            for key in event.keys():
                input_list = input_list + (event[key],)
            if event['verb'] == 'UPLOAD':
                db.execute('INSERT INTO IMAGE VALUES(?,?,?,?,?,?,?)', input_list)
            #print("Image")
            connection.commit()

        elif event['type'] == 'ORDER':
            for key in event.keys():
                input_list = input_list + (event[key],)
            if event['verb'] == 'NEW':
                db.execute('INSERT INTO ORDERS VALUES(?,?,?,?,?,?)', input_list)
            elif event['verb'] =='UPDATE':
                db.execute('UPDATE ORDERS SET event_time = \"' + event['event_time'] + '\", total_amount = \"' + event['total_amount'] + '\" where key=\"' + event['key'] + '\"')
            #print("Order")
            connection.commit()

        else:
            print("Unknown event data")






if __name__ =="__main__":
    db = connection.cursor()

    curr_dir = os.getcwd().split('/')
    dir_path = '/'.join(curr_dir[:-1])

    inputdata_path = os.path.join(dir_path, 'input/input.txt')


    file = open(inputdata_path,"r").read()
    inputdata = ast.literal_eval(file)
    ingest(inputdata)

    connection.close()