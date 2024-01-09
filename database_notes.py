import sqlite3

conn = sqlite3.connect('customer.db')

#Creat a cursor
c = conn.cursor()


#Creat a table 
c.execute("""CREATE TABLE customers(
          first_name text,
          last_name text,
          email text
)""")

# Insert one line 
c.execute("INSERT INTO customers VALUES('john', 'xu', 'xuzhan121@gmail.com')")

#Insert more 
many_customers = [('Wes', 'Brown', 'brown@gmail.com'), ('Brown','jason','jason@gmail.com')]
c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

#Query the database
c.execute("SELECT rowid, * FROM customers")

c.fetchone() #return a tuple 
c.fetchmany(2) # return a list 
c.fetchall() #return a list 

#Search 
c.execute("SELECT * FROM customers WHERE last_name LIKE 'jason' ")  #or 'Ja%' ja开头的

#Update records
c.execute(""" UPDATE customers SET first_name = 'Brown'  
              WHERE Last_name = 'amyco'
""") #based on last_name and then change the first_name 


c.execute(""" UPDATE customers SET first_name = 'Brown'  
              WHERE rowid = 1
""") #based on rowid and then change the first_name, this is the best way to update records

#Delete records
c.execute("DELETE from customers WHERE rowid = 1")

#Order results, Order by
c.execute("SELECT rowid, * FROM customers ORDER BY rowid") #add 'DESC' is 降序排列， by last_name 也可以

#And / or 
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'jason' AND rowid = 1") #满足两个条件

#Limit results
c.execute("SELECT rowid, * FROM customers LIMIT 2") #限制返回2个数据

#Delete a table 
c.execute("DROP TABLE customers")


#Commit command
conn.commit()

#Close connection 
conn.close()

print("*******************************")

connection = sqlite3.connect('mydatebase.db')

#如果不存在则创建一个database table
connection.execute("""
    CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY AUTOINCRMENT,
                   title text,
                   author text,
                   year integer
    )
""")

# Insert data into the table
books_data = [
    ("war", "jason", 1999),
    ("love", "amyco", 2000)
]

connection.execute('INERT INTO books(title, author, year) VALUES(?,?,?)', books_data)

# Quirey data from the table
result = connection.execute('SELECT * FROM books')
data = result.fetchall()

# Sorting data from the table 
result = connection.execute('SELECT * FROM books ORDER BY year ASC') #ASC:升序，DESC：降序
data = result.fetchall()
print(data)

# Related tables will be see video again 

# Delete a book by ID 
book_id_delete = 1 
connection.execute('DELETE FROM books WHERE id = ?', (book_id_delete,)) #如果建立id，则id也同样被删除掉，但是primary id会更新, 如果只有一个book_id 删除则不需要加括号

# Drop tables
connection.execute('DROP TABLE books') #谨慎操作

# Altering tables
connection.execute('ALTER TABLE books ADD COLUMN transport TEXT') #添加一列


connection.commit()
connection.close()