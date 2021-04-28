# CREATE KEYSPACE
create_keyspace = """
CREATE KEYSPACE IF NOT EXISTS sparkify 
WITH REPLICATION = { 'class' : 'SimpleStrategy',
                    'replication_factor' : 1 
                    };
"""

# DROP TABLES
session_table_drop = "DROP TABLE IF EXISTS session_table"
user_table_drop    = "DROP TABLE IF EXISTS user_table"
song_table_drop    = "DROP TABLE IF EXISTS song_table"

# CREATE TABLES

# session table
session_table_create = '''
CREATE TABLE IF NOT EXISTS session_table (
        session_id INT,
        item_in_session INT,
        user_id INT,
        artist_name TEXT,
        song_title TEXT,
        song_length FLOAT,
        PRIMARY KEY (session_id, item_in_session))
'''

# user table
user_table_create = '''
CREATE TABLE IF NOT EXISTS user_table (
        user_id INT,
        session_id INT,
        item_in_session INT,
        user_first_name TEXT,
        user_last_name TEXT,
        artist_name TEXT,
        song_title TEXT,
        PRIMARY KEY ((user_id, session_id), item_in_session))
'''

# song table
song_table_create = '''
CREATE TABLE IF NOT EXISTS song_table (
        song_title TEXT,
        user_id INT,
        user_first_name TEXT,
        user_last_name TEXT,
        PRIMARY KEY ((song_title), user_id))
'''


# INSERT RECORDS
# session table
session_table_insert ='''
INSERT INTO 
    session_table (
         session_id, 
         item_in_session, 
         user_id ,
         artist_name, 
         song_title, 
         song_length)
VALUES
    (%s, %s, %s, %s, %s,%s)
'''

# user table insert
user_table_insert = '''
INSERT INTO
    user_table(
        user_id,
        session_id,
        item_in_session,
        user_first_name,
        user_last_name,
        artist_name,
        song_title)
VALUES
    (%s, %s, %s, %s, %s, %s, %s)
'''

# song table insert
song_table_insert = '''
INSERT INTO
    song_table(
        song_title,
        user_id,
        user_first_name,
        user_last_name)
VALUES
    (%s, %s, %s, %s)
'''

# QUERY STATEMENTS

# QUERY 1
#"Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4"
session_table_query = '''
SELECT
    artist_name,
    song_title,
    song_length
FROM 
    session_table
WHERE
    session_id = %s
AND
    item_in_session = %s
'''

# QUERY 2
# Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
user_table_query = '''
SELECT
    artist_name,
    song_title,
    user_first_name,
    user_last_name
FROM
    user_table
WHERE
    user_id = %s
AND
    session_id =%s
'''

# QUERY 3
#  Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
song_table_query = '''
SELECT
    user_first_name,
    user_last_name
FROM
    song_table
WHERE
    song_title = %s
'''