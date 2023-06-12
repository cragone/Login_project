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
    insert_query = "INSERT INTO users (user_name, hashed_password, emails) VALUES (%s, %s, %s); COMMIT;"
    cursor.execute(insert_query, (username, password, email,))
    
    return "Good Request", 200


def retrieve_hashed_password(username):
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="loginbase"
             )
    cursor = connection.cursor()
    query = "SELECT hashed_password FROM users WHERE user_name = %s"
    cursor.execute(query, (username,))
    hashed_password = cursor.fetchone()
    return hashed_password[0] if hashed_password else None


    