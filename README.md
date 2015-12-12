# W205-exercise2

 After running the instance and making sure that all the librarys are installed

 Please run :
 
    psql -U postgres
   
    CREATE USER tali WITH PASSWORD 'pass'
   
    CREATE DATABASE Tcount WITH OWNER tali ENCODING 'utf-8';
   
 If you got an error for utf-8 Please run the following scripts:
 First, we need to drop template1. Templates can’t be dropped, so we first modify it so t’s an ordinary database:

    UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';

 Now we can drop it:

    DROP DATABASE template1;

 Now its time to create database from template0, with a new default encoding:

    CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UNICODE';

 Now modify template1 so it’s actually a template:

    UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';

 Now switch to template1 and VACUUM FREEZE the template:

    \c template1

    VACUUM FREEZE;

 Then create the DATABASE
 
    CREATE DATABASE tcount WITH OWNER tali ENCODING 'utf-8';
    
 go to tcount database
 
	psql -U tali tcount
    
	DELETE TABLE Tweetwordcount;
    
	CREATE TABLE Tweetwordcount (id serial PRIMARY KEY, word TEXT      NOT NULL,count INT     NOT NULL);

exit from postgres or open a new terminal  

make a projetc of EX2Twwetwordcount

    sparse quick EX2Twwetwordcount
    
go to the directory of EX2Twwetwordcount

replace the topology and spouts and bolts

    sparse run 


	
	
	
