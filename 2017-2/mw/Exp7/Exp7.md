# Exp7
## Preparation
Database   :  kali_clone  NATnetwork  
Attacker  : kali_attacker NATnetwork
![](pics/网络配置.png)

## Fingerprinting   
the application is written in PHP
![](pics/PHP编写.png)

### Inspecting HTTP headers
the application is only available via HTTP
![](pics/开放端口.png)  
nothing is runnning on the port 443
![](pics/443端口被拒.png)

### Using a directory Buster  
detect remote files and directories
![](pics/文件目录.png)
detect PHP script on the server
![](pics/PHP脚本目录.png)

## Detection and exploitation of SQL injection

### Detection of SQL injection

#### Detection based on Integers
accessing /article.php?id=2-0 displays article2
![](pics/id=2-0.png)  
accessing /article.php?id=2-1 displays article1
![](pics/id=2-1.png)

The subtraction is performed by the database, so it's likely that there is a SQL injection.

#### Detection on Strings
If SQL injection is present in the web page, an odd number of single quotes will throw an error, an even number of single quotes won't.  
![](pics/id=2'.png)

Now we have found a SQL injection in the page 10.0.2.7/cat.php

## Access to the administration pages and code execution

### The UNION keyword
Using UNION, the attacker can manipulate the end of the query and retrieve information from other tables.  
The most important rule is that both statements should return the same number of columns otherwise the database will trigger an error.

### Exploiting SQL injections with UNION  
- Find the number of columns to perform the UNION
- Find what columns are echoed in the page
  - using UNION SELECT and increase the number of columns   
  ![](pics/union select 1,2,3,4.png)
  the database triggers errors until the end of the query returns 4 columns   

  - using ORDER BY statement.    
  ![](pics/order by 4.png)    

   if the column number in the ORDER BY statement is bigger than the number of columns in the query, an error is thrown    
   ![](pics/order by 5.png)   

- Retrieve information from the database meta-tables   
  ![](pics/id=2'.png)  

  Based on the error message we received, we know that the backend database used is MySQL.
  - the user used by the PHP application to connect to the database with current_user()   
  ![the current user](pics/union select current_user.png)     

  - the version of the database using version()     
  ![the database version](pics/union select version.png)     

  - the current database    
  ![the current database](pics/union select database.png)  

- Retrieve information from other tables/databases  
  MySQL provides tables containing meta-information about the database, tables and columns available since the version 5 of MySQL. These tables are stored in the database information_schema.  
  a raw list of all tables  
  ![a raw list of all tables](pics/union select table_name.png)  
  a raw list of all columns  
  ![a raw list of all columns](pics/union select column_name.png)  

  To know what column belongs to what table:
  - put tablename and columnname in different parts of the injection
  - concatenate tablename and columnname in the same part of the injection using the keyword CONCAT  
  ![](pics/concat.png)
  get the username and password used to access the administration pages  
  ![](pics/login&&password.png)

## Access to the administration pages and code execution
### Cracking the password
The password can be easily cracked using 2 different methods:
- A search engine  
![](pics/decryption.png)
- [John-The-Ripper](http://www.openwall.com/john/) can be used to crack this password.  
For web application, a good guess would be MD5.  
### Uploading a Webshell and Code Execution  
Once access to the administration page is obtained, we can see that there is a file upload function allowing a user to upload a picture, we can use this functionality to try to upload a PHP script.   
This PHP script once uploaded on the server will give us a way to run PHP code and commands.
![](pics/login.png)
![](pics/upload.png)
Now, we need to find where the PHP script, managing the upload put the file on the web server.   
We can visit the web page of the newly uploaded image to see where the <img tag is pointing to:   
![](pics/view page source.png)   
start running commands using the cmd parameter   

- get a full list of the system's users
![](pics/passwd.png)
- get the version of the current kernel
![](pics/uname.png)
