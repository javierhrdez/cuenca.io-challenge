docker-compose -f docker-compose.common.yml -f docker-compose.test.yml build --no-cache  
docker-compose -f docker-compose.common.yml -f docker-compose.test.yml up  

docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml build  
docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml up  



docker build -t javierhrdez/cuenca_challenge .

