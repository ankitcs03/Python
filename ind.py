
# Define an alphabetic indexing tuple.
ind = tuple('abcdefghijklmnopqrstuvwxyz')

typ = ('DVD_FULL_SCREEN','DVD_WIDE_SCREEN','BLU-RAY')
mat = {}
stmt=""

for j, e in enumerate(typ):
    mat[str(ind[j])] = typ[j]
    if j == len(typ) - 1:
      stmt = stmt + ":" + str(ind[j])
    else:
      stmt = stmt + ":" + str(ind[j]) + ", "
	  
print (stmt)
print ()
print (mat)