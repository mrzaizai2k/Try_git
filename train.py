import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Connect to the MySQL server
cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='your_host', database='your_database')

# Retrieve data from the database
query = "SELECT age, height, weight FROM patients"
df = pd.read_sql_query(query, cnx)

# Split the data into training and testing sets
X = df[['age', 'height']]
y = df['weight']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
score = model.score(X_test, y_test)
print("R^2 Score:", score)

# Close the connection
cnx.close()
