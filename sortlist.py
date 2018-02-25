import urllib.request

numbers=[12,6,3432,43,7,43,2]
print(numbers)

numbers = [ int(i) for i in numbers ]
numbers.sort()
print(numbers)


urllib.request.urlretrieve("https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/06/Django-Framework-Python-Interview-Questions-Edureka.png", "local-filename.jpg")