import mysql.connector
conn = mysql.connector.connect(host = "csc648-dbinstance.covsgblvixwf.us-east-2.rds.amazonaws.com",
                            database = 'CSC648',
                            user = 'root',
                            password = 'root1234',
                            auth_plugin='mysql_native_password')
cursor = conn.cursor()


# conn = mysql.connector.connect(host = "localhost",
<<<<<<< HEAD
#                            database = 'CSC648',
#                            user = 'root',
#                            password = 'Derectorjin1',
#                            auth_plugin='mysql_native_password')
=======
#                             database = 'CSC648',
#                             user = 'root',
#                             password = 'Derectorjin1',
#                             auth_plugin='mysql_native_password')
>>>>>>> origin/brians_frontend
# cursor = conn.cursor()




