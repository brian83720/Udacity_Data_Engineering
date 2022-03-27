import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Copying the data from the S3 bucket to the Redshift Cluster
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Inserting the data from the loading tables to the dimensional tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Grabbing the data from 'dwh.cfg', connecting to the cluster with the credentials from 'dwh.cfg'.
    Then running the load_staging_tables & insert_tables functions.
    Closing the connection after that
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()