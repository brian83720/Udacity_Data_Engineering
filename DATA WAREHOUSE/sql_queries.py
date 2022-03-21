import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= (""" 
CREATE TABLE IF NOT EXISTS staging_events(
artist text,
auth text,
firstName text,
gender text,
itemInSession int,
lastName text,
length float,
level text,
location text,
method text,
page text,
registration text,
sessionId int,
song text,
status int,
ts bigint,
userAgent text,
userId int)
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs(
song_id text,
num_songs int,
artist_id text,
artist_latitude float,
artist_longitude float,
artist_location text,
artist_name text,
title text,
duration float,
year int)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplayId int IDENTITY(0,1) PRIMARY KEY,
startTime timestamp,
userId int,
level text,
songId text,
artistId text,
sessionId int,
location text,
userAgent text)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
userId int,
firstName text,
lastName text,
gender text,
level text)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
songId text,
title text,
artistId text,
year int,
duration float)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist(
artistId text,
name text,
location text,
artistLatitude float,
artistLongitude float)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
startTime timestamp,
hour varchar,
day int,
week int,
month int,
year int,
weekday int)
""")

# STAGING TABLES

staging_events_copy = ("""
copy staging_events from {}
credentials  'aws_iam_role={}'
FORMAT AS JSON {}
compupdate off region 'us-west-2';
""").format(config.get("S3","LOG_DATA"), config.get("IAM_ROLE", "ARN"), config.get("S3", "LOG_JSONPATH"))

staging_songs_copy = ("""
copy staging_songs from {}
credentials  'aws_iam_role={}'
JSON 'auto' truncatecolumns
compupdate off
region 'us-west-2';
""").format(config.get("S3","SONG_DATA"), config.get("IAM_ROLE", "ARN"))

# FINAL TABLES

songplay_table_insert = ("""
    insert into songplays(startTime, userId, level, songId, artistId, sessionId, location, userAgent)
    select distinct '1970-01-01'::date + s.ts/1000 * interval '1 second' as start_time
    , s.userid 
    , s.level
    , ss.song_id as songId
    , ss.artist_id as artistId
    , s.sessionid 
    , s.location
    , s.useragent
    from staging_events s
    left join staging_songs ss
    on s.song = ss.title

""")

user_table_insert = ("""
    insert into users(userId,firstName, lastName, gender,level)
    select distinct userid
    , firstname
    , lastname
    , gender
    , level
    from staging_events
""")

song_table_insert = ("""
    insert into songs(songId, title, artistId, year, duration)
    select distinct song_id as songId
    , title
    , artist_id as artistId
    , year
    , duration
    from staging_songs
""")

artist_table_insert = ("""
    insert into artist(artistId, name, location, artistLongitude, artistLatitude)
    select distinct artist_id as artistId
    , artist_name as name
    , artist_location as location
    , artist_longitude as artistLongitude
    , artist_latitude as artistLatitude
    from staging_songs
""")

time_table_insert = ("""
    insert into time (startTime, hour, day, week, month, year ,weekday)
    select distinct start_time as startTime
    ,EXTRACT(HOUR FROM start_time) As hour
    ,EXTRACT(DAY FROM start_time) As day
    ,EXTRACT(WEEK FROM start_time) As week
    ,EXTRACT(MONTH FROM start_time) As month
    ,EXTRACT(YEAR FROM start_time) As year
    ,EXTRACT(DOW FROM start_time) As_weekday
    FROM (
    SELECT distinct ts,'1970-01-01'::date + ts/1000 * interval '1 second' as start_time
    FROM staging_events
    ) tab
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
