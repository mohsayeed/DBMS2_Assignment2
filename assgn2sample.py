import psycopg2
conn = psycopg2.connect(host="localhost", dbname="assgn2", user="postgres", password="myPassword")
cur=conn.cursor()

cur.execute("SET STANDARD_CONFORMING_STRINGS TO OFF;")
cur.execute("SHOW STANDARD_CONFORMING_STRINGS;")

cur.execute("""
  CREATE TABLE assgn2table1(
   id integer PRIMARY KEY,
   title text,
   abstract text
)
""")

cur.execute("""
    CREATE TABLE assgn2table2(
    id integer,
    mainauthor text
)
""")

cur.execute("""
    CREATE TABLE assgn2table3(
    id integer,
    coauthor text
)
""")

cur.execute("""
    CREATE TABLE assgn2table4(
    id integer,
    venue text
)
""")

cur.execute("""
    CREATE TABLE assgn2table5(
    id integer,
    year integer
)
""")

cur.execute("""
    CREATE TABLE assgn2table6(
    id integer,
    referenceid integer
)
""")

with open('papers.tsv','r') as f:
	next(f)
	cur.copy_from(f, 'assgn2table1', sep='\t')
with open('mainauthor.tsv','r') as f:
	next(f)	
	cur.copy_from(f, 'assgn2table2', sep='\t')
with open('coauthor.tsv','r') as f:
	next(f)
	cur.copy_from(f, 'assgn2table3', sep='\t')
with open('venue.tsv','r') as f:
	next(f)
	cur.copy_from(f, 'assgn2table4', sep='\t')
with open('year.tsv','r') as f:
	next(f)
	cur.copy_from(f, 'assgn2table5', sep='\t')
with open('referenceslist.tsv','r') as f:
	next(f)
	cur.copy_from(f, 'assgn2table6', sep='\t')
conn.commit()
cur.close()
conn.close()








