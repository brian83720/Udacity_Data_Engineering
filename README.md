## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The goal of this project is to create an ETL pipeline to let the analytics team have better access to the data so they can know better what songs users are listening to.

## State and justify your database schema design and ETL pipeline.

### Summary 
We were given two types of data, 1.log_data 2.song_data  
We used these data to create 4 dimension tables (users, songs, artists,time), and 1 fact table (songplays).  
After defining the ETL Processes, we will then build the ETL pipeline.


### Dealing with song_data
We started off dealing with the song_data (we used the get_files function to get a list of all JSON files), and splitting the data into 2 dimension tables - songs and artists.  
The Songs table describes the songs in the music database, and contains the song_id, title, artist_id, year, and duration.  
The Artists table describes the artists in the music database, which contains the artist_id, name, location, latitude, and longitude.


### Dealing with log_data
After that, it was time to deal with the log_data. We only needed the records that had the "NextSong" action (df['page'] == 'NextSong').  
We used the log_data to create the other 2 dimension tables - time and users.  
The Time table describes the records' timestamps in Songplays, and cotains the start_time, hour, day, week, month, year, weekday.  
The user table describes the users in the app, which contains the user_id, first_name, last_name, gender, and level.  

Lastly, we need to create the Songplays fact table, which is the records in log_data associated with song plays.  
We will need the artist_id and song_id for the fact table. 
We wrote a join query in sql_queries.py joining the artist and songs table, in the where clause we added a "%s" placeholder so we can later pass in the values to filter the data we need.  
We then run a for loop to go through each record and got the artist_id and song_id.  
We insert the log_data values we need (songplay_id, start_time, user_id, level, session_id, location, user_agent) along with artist_id and song_id, and we complete our songplays face table.


### Creating the ETL Pipeline.
After creating our ETL process, we are now ready to build the ETL pipeline.  
We create three functions, one for processing the song_data, one for processing the log_data, and one for loop for running all the Json files from the file path we specify.  
We copy the ETL process onto the the first 2 functions for processing song_data and log_data, and then run the for loop twice with their respective file paths and function, one for process_song_file, one for process_log_file.


### Results
We did a test run, and as a result we ran through 87 files from data/song_data and 30 files from data/log_data.  
We verified and the data were processed into the tables.  
We created a star schema, and created an ETL Pipeline for ongoing Json data to be processed into the datatables.  
The analytics team from Sparkify will be able to have easier access to whatever data they need from the Json files.

For ETL Process scripts, please view https://github.com/brian83720/Udacity_Data_Engineering/blob/main/ETL%20Process.ipynb
For ETL Pipeline scripts, please view https://github.com/brian83720/Udacity_Data_Engineering/blob/main/etl.py
create_tables.py and sql_queries.py will also be in the repository to view.
Thank you!
