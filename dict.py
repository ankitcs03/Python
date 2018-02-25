fvt_language = {'ankit'  :'hindi',
				'deepak' :'english',
				'utkarsh':'bangali',
				'shiv'   : 'bhojpuri'
			   }
fvt_user = [ 'shiv','deepak']

for name in fvt_language:
	print (name.title())
	
	if name in fvt_user:
		print("Hello " + name.title() +  ", I can see your fvt language is "  + fvt_language[name])
		
print("\n\n")
print(fvt_language.keys())
