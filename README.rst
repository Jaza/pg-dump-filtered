PG Dump Filtered
================

Example Python script that outputs an SQL dump (as INSERT statements) of a set of related tables, filtered by the ID of the top-level table.

With only a small amount of tweaking, this script should be able to produce a dump of virtually any relational data set, filtered by virtually any criteria that you might fancy.


Instructions
------------

To try out the test script, do the following:

1.  Create a new Postgres DB / user, e.g:

.. code:: sql

    CREATE pg_dump_test;
    CREATE USER pg_dump_test WITH PASSWORD 'pg_dump_test';
    GRANT ALL PRIVILEGES ON DATABASE pg_dump_test TO pg_dump_test;

2.  Import the test schema and test data, e.g:

.. code:: bash

    PGPASSWORD=pg_dump_test psql -U pg_dump_test pg_dump_test < ./test_schema.sql
    PGPASSWORD=pg_dump_test psql -U pg_dump_test pg_dump_test < ./test_data.sql

3.  Generate a DB dump for all data related to the top-level entity with ID "2", e.g:

.. code:: bash

    ./pg_dump_filtered.py "postgresql://pg_dump_test:pg_dump_test@localhost:5432/pg_dump_test" 2
