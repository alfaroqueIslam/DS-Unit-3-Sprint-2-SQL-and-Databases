import psycopg2
import sqlite3

dbname = 'qluaqybq'
user = 'qluaqybq'  # ElephantSQL chooses to reuse dbname and username
password = 'rhKOPsVgTV7sCwsgto06CoCc7ES-GCUz'
host = 'ruby.db.elephantsql.com'  # Port is default 5432

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

#How many passengers survived, and how many died?
pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1;')
print('Survived:', pg_curs.fetchall())
#How many passengers were in each class?
pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=0;')
print('Died:', pg_curs.fetchall())
#How many passengers survived/died within each class?
pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=1;')
print('Survived class 1:', pg_curs.fetchall())

pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=2;')
print('Survived class 2:', pg_curs.fetchall())

pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=3;')
print('Survived class 3:', pg_curs.fetchall())

pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=1;')
print('Died class 1:', pg_curs.fetchall())

pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=2;')
print('Died class 2:', pg_curs.fetchall())

pg_curs.execute('SELECT COUNT(*) FROM titanic WHERE survived=1 AND pclass=2;')
print('Died class 3:', pg_curs.fetchall())

#What was the average age of survivors vs nonsurvivors?
pg_curs.execute('SELECT AVG(age) FROM titanic WHERE survived=1;')
print('Survived AVG age:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(age) FROM titanic WHERE survived=0;')
print('Died AVG age:', pg_curs.fetchall())
#What was the average age of each passenger class?
pg_curs.execute('SELECT AVG(age) FROM titanic WHERE pclass=1;')
print('class 1 AVG age:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(age) FROM titanic WHERE pclass=2;')
print('class 2 AVG age:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(age) FROM titanic WHERE pclass=3;')
print('class 3 AVG age:', pg_curs.fetchall())
#What was the average fare by passenger class? By survival?
pg_curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass=1;')
print('class 1 AVG fare:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass=2;')
print('class 2 AVG fare:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(fare) FROM titanic WHERE pclass=3;')
print('class 3 AVG fare:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(fare) FROM titanic WHERE survived=1;')
print('Survived AVG fare:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(fare) FROM titanic WHERE survived=0;')
print('Died AVG fare:', pg_curs.fetchall())
#How many siblings/spouses aboard on average, by passenger class? By survival?
pg_curs.execute('SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass=1;')
print('class 1 AVG siblings_spouses_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass=2;')
print('class 2 AVG siblings_spouses_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE pclass=3;')
print('class 3 AVG siblings_spouses_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE survived=1;')
print('Survived AVG siblings_spouses_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(siblings_spouses_aboard) FROM titanic WHERE survived=0;')
print('Died AVG siblings_spouses_aboard:', pg_curs.fetchall())

#How many parents/children aboard on average, by passenger class? By survival?
pg_curs.execute('SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass=1;')
print('class 1 AVG parents_children_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass=2;')
print('class 2 AVG parents_children_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(parents_children_aboard) FROM titanic WHERE pclass=3;')
print('class 3 AVG parents_children_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(parents_children_aboard) FROM titanic WHERE survived=1;')
print('Survived AVG parents_children_aboard:', pg_curs.fetchall())

pg_curs.execute('SELECT AVG(parents_children_aboard) FROM titanic WHERE survived=0;')
print('Died AVG parents_children_aboard:', pg_curs.fetchall())
#Do any passengers have the same name?
