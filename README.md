# flaskapiapp
#Build image
docker build -t nan/flaskapi .
docker run -p 7777:5000  nan/flaskapi
