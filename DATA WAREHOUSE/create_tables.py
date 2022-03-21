#Load Libraries
import configparser
import psycopg2
import boto3
from sql_queries import create_table_queries, drop_table_queries

#Dropping existing tables
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

#Creating new tables
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

#Connecting to the Redshift cluster from the dwf.cfg file
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()