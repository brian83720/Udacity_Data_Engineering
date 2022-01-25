# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays (
timestamp timestamp , user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, userAgent varchar
)
""")

user_table_create = ("""create table if not exists users (
user_id int primary key, firstName text, lastName text, gender text, level text
)
""")

song_table_create = ("""create table if not exists songs (
song_id varchar primary key, title text, artist_id varchar, year int, duration float
)
""")

artist_table_create = ("""create table if not exists artists (
artist_id varchar primary key, artist_name text, artist_location text, artist_longitude varchar, artist_latitude varchar
)
""")

time_table_create = ("""create table if not exists time (
datetime timestamp primary key, hour int, day int, weekofyear int, month int, year int, weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = (""" insert into songplays(timestamp, user_id, level, song_id, artist_id, session_id, userAgent)
values(%s,%s,%s,%s,%s,%s,%s)
on conflict do nothing
""")

user_table_insert = ("""insert into users(user_id,firstName, lastName, gender,level)
values(%s,%s,%s,%s,%s)
on conflict do nothing
""")

song_table_insert = (""" insert into songs(song_id, title, artist_id, year, duration)
values(%s,%s,%s,%s,%s)
on conflict do nothing
""")

artist_table_insert = ("""insert into artists(artist_id, artist_name, artist_location, artist_longitude, artist_latitude)
values(%s,%s,%s,%s,%s)
on conflict do nothing
""")


time_table_insert = ("""insert into time(datetime, hour, day, weekofyear, month, year ,weekday)
values(%s,%s,%s,%s,%s,%s,%s)
on conflict do nothing
""")

# FIND SONGS

song_select = ("""
select
s.song_id,
a.artist_id
from
songs s
join artists a
on s.artist_id = a.artist_id
where s.title = (%s)
and a.artist_name = (%s)
and s.duration = (%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

