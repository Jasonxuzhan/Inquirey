import sqlite3


#Create database of basename
def create_info_database(basename):   
    con = sqlite3.connect(basename)
    cur = con.cursor()

    #Creat basename info table  
    cur.execute("""CREATE TABLE IF NOT EXISTS customersinfo(
                source_from text,
                source_channel text,
                province text,
                city text,
                company text,
                contact_person text,
                telephone text,
                scenario text,
                cooperate_term text,
                request text,
                answer_by text,
                transfer_to text
    )""")
    
    con.commit()
    con.close()


# Creat customer info list, return a tuple
def creat_customer_info(customer_name):
    customer_sample_insert_type = []
    customer_info_sample = []
    customer_info_sample.append(input("请输入线索来源: ")) 
    customer_info_sample.append(input("请输入来源渠道: "))
    customer_info_sample.append(input("请输入省份，直辖市可在此输入: "))
    customer_info_sample.append(input("请输入城市: "))
    customer_info_sample.append(customer_name)
    customer_info_sample.append(input("请输入姓名: "))
    customer_info_sample.append(input("请输入电话号码: "))
    customer_info_sample.append(input("请输入应用场景: "))
    customer_info_sample.append(input("请输入合作方式: "))
    customer_info_sample.append(input("需求描述: "))
    customer_info_sample.append(input("接线员姓名: "))
    customer_info_sample.append(input("业务人员姓名: "))
    customer_sample_insert_type.append(tuple(customer_info_sample))
    return customer_sample_insert_type


#Insert customer information into base table, the second parmater must be a tuple with 12 elements
def insert_customer_info(basename, customer_info_tuple):
    con = sqlite3.connect(basename)
    cur = con.cursor()
    
    cur.executemany("INSERT INTO customersinfo VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", customer_info_tuple)
    
    con.commit()
    con.close()


#Display all customers info from database
def display_all_info(basename):
    con = sqlite3.connect(basename)
    cur = con.cursor()
    
    cur.execute("SELECT rowid, * FROM customersinfo")
    items = cur.fetchall()
    for item in items:
        print(item) 
    
    con.commit()
    con.close()


#Delete one info from database based on rowid 
def delete_one_info(basename):
    con = sqlite3.connect(basename)
    cur = con.cursor()

    confirmation = input(f"Pls input confirm text 'delete': ")
    if confirmation == "delete":
        rowid = input("Pls input customer id: ")
        cur.execute("SELECT * FROM customersinfo WHERE rowid = ?", rowid)
        confirm_operation = input("pls input 'Y' to delete , 'N' to quit: ")       
        if confirm_operation.lower() == "y":
            cur.execute("DELETE from customersinfo WHERE rowid = ?", rowid)
        else:
            print("You have canceled deleting operation")
    
    con.commit()
    con.close()


#Delete table 
def delete_all_info(basename):
    con = sqlite3.connect(basename)
    cur = con.cursor()

    confirmation = input("pls input confirm text 'delete': ")
    if confirmation == "delete":
        confirm_operation = input((f"pls input 'Y' to delete , 'N' to quit")) 
        if confirm_operation.lower() == "y":
            cur.execute("DROP TABLE customersinfo")
            print("All info had been deleted")
        else:
            print("You have canceled deleting operation")
    
    con.commit()
    con.close()



