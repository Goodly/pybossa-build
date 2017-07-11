#/usr/bin/python2.7

import os
import dj_database_url
import psycopg2
import psycopg2.extensions as ext

DATABASE_URL = os.environ.get('PYBOSSA_DATABASE_URL',
                              'postgresql://pybossa:tester@localhost/pybossa')

config = dj_database_url.parse(DATABASE_URL, conn_max_age=60)

with psycopg2.connect(host=config['HOST'],
                        port=config['PORT'],
                        dbname='postgres',
                        user=config['USER'],
                        password=config['PASSWORD']) as conn:
    DROP_DB_SQL = """
        DROP DATABASE IF EXISTS {0};
    """.format(ext.quote_ident(config['NAME'], conn))
    CREATE_DB_SQL = """
        CREATE DATABASE {0}
        ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8'
        TEMPLATE template0;
    """.format(ext.quote_ident(config['NAME'], conn))

# autocommit mode required for create and drop
    conn.set_session(autocommit=True)
    with conn.cursor() as cur:
        print DROP_DB_SQL
        cur.execute(DROP_DB_SQL)
        print CREATE_DB_SQL
        cur.execute(CREATE_DB_SQL)
