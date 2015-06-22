PG Dump Filtered
================

Example Python script that outputs an SQL dump (as ``INSERT`` statements) of a set of related tables, filtered by the ID of the top-level table.

With only a small amount of tweaking, this script should be able to produce a dump of virtually any relational data set, filtered by virtually any criteria that you might fancy.

This script is for Postgres, whose ``pg_dump`` utility lacks any query-level filtering functionality. It could also be quite easily adapted to other DBMSes (e.g. MySQL, SQL Server, Oracle), although most of Postgres' competitors have a dump utility with at least some filtering capability.


Instructions
------------

To try out the test script, do the following:

1.  Create a new Postgres DB / user, e.g:

.. code:: sql

    CREATE DATABASE pg_dump_test;
    CREATE USER pg_dump_test WITH PASSWORD 'pg_dump_test';
    GRANT ALL PRIVILEGES ON DATABASE pg_dump_test TO pg_dump_test;

2.  Import the test schema and test data, e.g:

.. code:: bash

    PGPASSWORD=pg_dump_test psql -U pg_dump_test pg_dump_test < ./test_schema.sql
    PGPASSWORD=pg_dump_test psql -U pg_dump_test pg_dump_test < ./test_data.sql

3.  Install Python dependencies (i.e. psycopg2):

.. code:: bash

    pip install -r requirements.txt

4.  Generate a DB dump for all data related to the top-level entity with ID "2", e.g:

.. code:: bash

    ./pg_dump_filtered.py \
    "postgresql://pg_dump_test:pg_dump_test@localhost:5432/pg_dump_test" 2 \
    > ~/pg_dump_test_output.sql

More info
---------

For a comprehensive guide of how to use this script, see this blog post:

http://greenash.net.au/thoughts/2015/06/generating-a-postgres-db-dump-of-a-filtered-relational-set/
