# import mysql.connector
 
# # Creating connection object
# mydb = mysql.connector.connect(
	
#     host = "localhost",
#     user = "jk",
#     password = "getmein123",
#     database = "testDB"
# )
 







from flask import Flask
app = Flask(__name__)


@app.route("/") 
def Hello():
    return "Hello from jahanazeb khan"




# @app.route("/get_result") 
# def get_results():
#     lis = []
#     cursor = mydb.cursor()
#     cursor.execute('SELECT * FROM Persons')
#     # cursor.execute("SHOW DATABASE")
#     # Printing the connection object

#     myresult = cursor.fetchall()
#     for i in myresult:
#         lis.append(i)
        
#     return {"result":lis}
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
