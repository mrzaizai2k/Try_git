import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root', password='mrzaizai2k',
                              host='localhost', database='test')

# Create a table
cursor = cnx.cursor()
table_name = 'users'
create_table_query = '''
CREATE TABLE {} (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB'''.format(table_name)
cursor.execute(create_table_query)

# Insert data into the table
insert_query = "INSERT INTO {} (name, age) VALUES (%s, %s)".format(table_name)
data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
cursor.executemany(insert_query, data)
cnx.commit()

# Retrieve data from the table
select_query = "SELECT * FROM {}".format(table_name)
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
cursor.close()
cnx.close()
