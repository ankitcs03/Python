import cx_Oracle

try:
	DB = cx_Oracle.connect('asriva01/Fiserv#123@orcl')
	print(DB.version)
	print()
except cx_Oracle.DatabaseError as e:
	error = e.args
	print ( "Oracle-Error-Code : " + error.code, sys.stderr)
	print ( "Oracle-Error-Message:" + error.message, sys.stderr)
else:	
	cur =  DB.cursor()
	#cur.execute("insert into Employees values ('101','Ankit',27,'Engineer')")
	
	#DB.commit()
	count = 0
	cur.execute('select * from Employees' )

		
	for result in cur:
		while (count < len(cur.description)):
			print( cur.description[count][0], end="  ")
			count += 1
		print()	
		print (result)
		print()
		
		
		
	cur.close()
	
finally:
  # Close connection. 
  DB.close()