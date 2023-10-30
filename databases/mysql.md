# MySQL

### Some commands:
#### Timezone
```
select time();
set time_zone = '+03:00';	// Moscow
```

[SHOW](https://dev.mysql.com/doc/refman/5.7/en/show.html)
```
SHOW TABLES;
SHOW TABLES LIKE "%edx%";
USE <database>;
SHOW INDEX FROM <table_name>;
```

#### Change encoding
Turn off server processes using the db!!!

```sql
ALTER DATABASE edxapp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE edxapp;
```

```sql
SHOW TABLE STATUS FROM edxapp like "course_overviews_courseoverview";

ALTER TABLE `edxapp`.`course_overviews_courseoverview` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
show table status like "course_overviews_courseoverview";

ALTER TABLE `edxapp`.`proctoring_proctoredexam` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE `edxapp`.`proctoring_proctoredexam` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE `edxapp`.`proctoring_proctoredexam` MODIFY exam_name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- For a single column you can simply do: 
ALTER TABLE table_name CHANGE column_name VARCHAR(45) COLLATE utf8mb4_bin;

-- Deadlocks: show reason of deadlocks
SHOW ENGINE INNODB STATUS

-- For example section:
LATEST FOREIGN KEY ERROR  

-- CHARACTER_SET
SELECT * FROM information_schema.SCHEMATA  ;

-- Columns types
SHOW FIELDS FROM proctoring_proctoredexam;
SHOW FULL COLUMNS FROM proctoring_proctoredexam;
```

#### Create an user:
```sql
CREATE USER 'advoegl'@'localhost' IDENTIFIED BY 'Platoon333';
GRANT ALL PRIVILEGES ON * . * TO 'advoegl'@'localhost';
SHOW GRANTS FOR 'advoegl'@'localhost';
```
```shell
mysql -u advoegl -p
```


#### Change Isolation Level
```sql
set tx_isolation = "READ-COMMITTED";
set tx_isolation = "REPEATABLE-READ";
```
