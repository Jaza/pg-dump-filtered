#!/usr/bin/env python

from __future__ import print_function

from binascii import hexlify
import psycopg2
import sys
import urlparse

if len(sys.argv) < 3:
    print('Must specify database_uri and world_id arguments, e.g. {0} "postgresql://pg_dump_test:pg_dump_test@localhost:5432/pg_dump_test" 1'.format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

# Grab DB credentials from first command-line argument.
database_uri = sys.argv[1]
db_uri_parsed = urlparse.urlparse(database_uri)

conn = psycopg2.connect(database=db_uri_parsed.path[1:],
                        user=db_uri_parsed.username,
                        password=db_uri_parsed.password,
                        host=db_uri_parsed.hostname)

# Grab the top-level ID to query by, from second command-line argument.
world_id = int(sys.argv[2])

# Dumping data for these tables.
tables = [
    'world',
    'country',
    'city',
    'person']

for table in tables:
    t_cur = conn.cursor()

    # Thanks to:
    # http://bytes.com/topic/python/answers/438133-find-out-schema-psycopg
    t_cur.execute((
        "SELECT        column_name "
        "FROM          information_schema.columns "
        "WHERE         table_name = '%s' "
        "ORDER BY      ordinal_position") % table)

    t_fields_str = ', '.join([x[0] for x in t_cur])
    d_cur = conn.cursor()

    # Start constructing the query to grab the data for dumping.
    query = (
        "SELECT        x.* "
        "FROM          %s x ") % table

    # The rest of the query depends on which table we're at.
    if table == 'world':
        query += "WHERE         x.id = %(world_id)s "
    elif table == 'country':
        query += "WHERE         x.world_id = %(world_id)s "
    elif table == 'city':
        query += (
            "INNER JOIN    country c "
            "ON            x.country_id = c.id ")
        query += "WHERE         c.world_id = %(world_id)s "
    elif table == 'person':
        query += (
            "INNER JOIN    city ci "
            "ON            x.city_id = ci.id "
            "INNER JOIN    country c "
            "ON            ci.country_id = c.id ")
        query += "WHERE         c.world_id = %(world_id)s "

    # For all tables, filter by the top-level ID.
    d_cur.execute(query, {'world_id': world_id})

    for d_row in d_cur:
        # Start constructing the INSERT statement to dump.
        d_str = "INSERT INTO %s (%s) VALUES (" % (table, t_fields_str)
        d_vals = []

        for i, d_field in enumerate(d_row):
            d_type = type(d_field).__name__

            # Rest of the INSERT statement depends on the type of
            # each field.
            if d_type == 'datetime':
                d_vals.append("'%s'" % d_field.isoformat().replace('T', ' '))
            elif d_type == 'bool':
                d_vals.append('%s' % (d_field and 'true' or 'false'))
            elif d_type == 'buffer':
                d_vals.append(r"'\x" + ("%s'" % hexlify(d_field)))
            elif d_type == 'int':
                d_vals.append('%d' % d_field)
            elif d_type == 'Decimal':
                d_vals.append('%f' % d_field)
            elif d_type in ('str', 'unicode'):
                d_vals.append("'%s'" % d_field.replace("'", "''"))
            elif d_type == 'NoneType':
                d_vals.append('NULL')

        d_str += ', '.join(d_vals)
        d_str += ');'
        print(d_str)

conn.close()
