import psycopg2




def log(session_dict):
    #print(session_dict)
    #session_dict = {"hi" : "bye"}
    
    with psycopg2.connect(dbname="postgres", user="postgres", host = "db", password="secret", port = "5432" )  as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS
                logs ( name TEXT);
            """) 

            cursor.execute("""
                INSERT INTO logs (name)
                VALUES (%s)
            """, (repr(session_dict), ))

            cursor.execute("SELECT * FROM logs")
            print(cursor.fetchone()) 
            conn.commit()
             


