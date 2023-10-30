# Postgres

#### Stop postres service
```bash
service postgresql stop
```

### CLI commands
```postgresql
-- Database size
\l+
-- or
\l+ <database_name>

\d+ <table_name>
\d+ django_migrations
```


#### Remove replication
```sql
SELECT * from pg_publication_tables;
 pubname | schemaname | tablename 
---------+------------+-----------
 pub1    | public     | auth_user
 pub1    | public     | auth_user_groups
(2 rows)

DROP PUBLICATION pub1 ;
```

#### ADD code column UNIQUE CONSTRAINT on table workflow_docstatus
```sql
ALTER TABLE workflow_docstatus ADD CONSTRAINT docstatus_code UNIQUE (code);
```

#### ADD code column UNIQUE CONSTRAINT on table workflow_doctype
```sql
ALTER TABLE workflow_doctype ADD CONSTRAINT doctype_pkey UNIQUE (id);
```

#### GROUP BY
```sql
SELECT 
  count(workflow_doctype.id) AS c, 
  array_agg(workflow_doctype.id) AS ids 
FROM workflow_doctype GROUP BY id;


SELECT 
  * 
FROM (SELECT 
        count(workflow_doctype.id) AS c, 
        array_agg(workflow_doctype.id) AS ids 
      FROM workflow_doctype GROUP BY id
    ) AS dups 
WHERE dups.c > 1;
```

### Sequences
#### Show all
```
\ds+
```

#### Next val
```sql
SELECT nextval('public.nsi_trp_pollutants_id_seq');
```

#### Set new one
```sql
SELECT setval('public.nsi_trp_pollutants_id_seq', 254);
```

### Connect to optigroups database
```shell
sudo -i -u postgres
psql
\c optigroups
```

### Make dump of optigroups database
```shell
$ sudo -i -u postgres
$ pg_dump optigroupd > my_dumb_sql
$ pg_dumpall optigroupd > my_dumb_sql
```

### Restore from dump 
```shell
sudo -i -u postgres
psql optigroupd < my_dump.sql
```

```sql
bot_v3=# show log_directory;
 log_directory 
---------------
 log
(1 row)

bot_v3=# show data_directory;
      data_directory      
--------------------------
 /var/lib/postgresql/data
(1 row)

bot_v3=# show log_filename;
          log_filename          
--------------------------------
 postgresql-%Y-%m-%d_%H%M%S.log
(1 row)
```

### user -U; host -h; port -p
```
psql -U app -h 192.168.32.220 -p 9981 
```

### Show tables ordered by size
```sql
select
  table_name,
  pg_size_pretty(pg_relation_size(quote_ident(table_name))),
  pg_relation_size(quote_ident(table_name))
from information_schema.tables
where table_schema = 'public'
order by 3 desc;
```

```sql
-- Total size of all tables
select
  pg_size_pretty(sum(pg_relation_size(quote_ident(table_name)))),
  sum(pg_relation_size(quote_ident(table_name)))
from information_schema.tables
where table_schema = 'public';
```

```sql
SELECT pg_size_pretty(pg_total_relation_size(c.oid)), c.oid::regclass, relkind
FROM   pg_class c
ORDER  BY pg_total_relation_size(c.oid) DESC
LIMIT  10;
```

### SQL From values
```sql
select * from (values ('1', 'aaa'), ('2', 'bbb'), ('3', 'ccc')) as x(a, b);
```

### WITH context
#### WITH context expression
```
with ctx as (
  select
      *
    from (
      values 
      ('1', '{}'::json),
      ('2', '{}'::json),
      ('3', '{}'::json)
    ) as ctx (setting_type, variable_settings)
)

insert into form_builder_applicationsettings (setting_type, variable_settings)
  select
      *
    from ctx;

```

#### WITH with return values:
```sql
with ctx as (
  select
      *
    from (
      values 
      ('1', '{}'::json),
      ('2', '{}'::json),
      ('3', '{}'::json)
    ) as ctx (setting_type, variable_settings)
)

insert into form_builder_applicationsettings (setting_type, variable_settings)
  select
      *
    from ctx
      returning
    *
    ;
```

#### via cursor
```python
with connection.cursor() as cursor:
    cursor.execute(
        '''
        with ctx as (
          select
              *
            from (
              values 
              ('1', '{}'::json),
              ('2', '{}'::json),
              ('3', '{}'::json)
            ) as ctx (setting_type, variable_settings)
        )

        insert into form_builder_applicationsettings (setting_type, variable_settings)
          select
              *
            from ctx
            returning
            *
        '''
    )
    rows = cursor.fetchall()
```



#### Logging
```
in postgresql.conf
log_min_duration_statement = 1000       # -1 is disabled, 0 logs all statements
                                        # and their durations, > 0 logs only
                                        # statements running at least this number
                                        # of milliseconds

logging_collector = on                  # Enable capturing of stderr and csvlog
                                        # into log files. Required to be on for
                                        # csvlogs.
                                        # (change requires restart)

#log_directory = 'log'                  # directory where log files are written,
                                        # can be absolute or relative to PGDATA
```







#### Show dicrectory where data is stored
```sql
SHOW data_directory;
```


#### Observe columns
```sql
SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'your_schema'
   AND table_name   = 'your_table'
     ;

SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'public'
   AND table_name   = 'django_migrations'
     ;
```

```sql
SELECT * FROM information_schema.tables WHERE table_name ILIKE 'django_%';
```


### Privilegues
```postgresql
\dg+
CREATE ROLE oc;
GRANT bot TO oc;
```
