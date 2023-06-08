import psycopg2




def storeuserdata(username, password, email):
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="loginbase"
             )
    cursor = connection.cursor()
    insert_query = "INSERT INTO users (user_name, hashed_pasword, emails) VALUES (%s, %s, %s); COMMIT;"
    cursor.execute(insert_query, (username, password, email,))
    
    return "Good Request", 200

    