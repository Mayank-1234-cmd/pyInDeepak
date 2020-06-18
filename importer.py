def view(app):
  import requests
  response = requests.get('http://raw.githack.com/Mayank-1234-cmd/pyInDeepak/master/' + app + '.py')
  response
#If doesn't work then response.content
