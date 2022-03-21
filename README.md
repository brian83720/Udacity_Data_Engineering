<h1>Purpose of the Database and Sparkify's Analytical Goals</h1>
Sparkify's Goal is to bring their song database and processes onto the cloud due to the increase of their user base.
The database that was extracted from a S3 bucket not is copied into Redshift, and transformed into sets of dimensional tables for the analytic team to find insights from the user behavior.


<h1>Database Design and ETL Pipeline</h1>

<h2>Database Design</h2>
First we need to think of what the data team will need to analyze, maybe have a meeting with the data team to see the requirements.
Once we are sure what the demand is, we can then start to design our fact and dimension tables.
We will need a total of 7 tables, 2 staging tables, 1 fact table, and 4 dimension table.
We need to create a Redshift Cluster and an iam read-only role, and fill in the endpoints for each in the dwh.cfg file.
Once done, we connect to the redshift cluster, then define the fields and data type and run a drop_table function and a create_table function.
Drop_table is to drop any existing table, and we create new ones.
We have then loaded 7 tables into the Redshift Cluster.

<h2>ETL Pipeline</h2>
Now it is time to copy the data from the S3 bucket the the staging tables in the Redshift cluster.
The S3 bucket address is defined in dwh.cig and we grab it and run the staging_events_copy and staging_songs_copy to copy the data into the Redshift cluster.
Once the data is copied over to the Redshift cluster, we then insert the data into different tables to make the data cleaner to use with the insert table function.

Now we have the tables for Sparkify's data team to discover pattern and trends in the user behavior, and hopefully they use their findings to fulfill the need of their consumers.