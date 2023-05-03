VERSION=$1
docker build --file ./docker/auth/Dockerfile --tag www.thinhlh.com:5000/auth_service:${VERSION} .
docker push www.thinhlh.com:5000/auth_service:${VERSION}

# Perform remote deploy with docker context
# 1. Create a context | 
    # docker context create context-name --docker "host=ssh://user@server-address"
    # You can config ssh key by setting the ssh inside ssh key config file ~/.ssh/config
    
# 2. Then run all commands with --context context-name like normally

# https://www.docker.com/blog/how-to-deploy-on-remote-docker-hosts-with-docker-compose/

docker-compose --context remote-server-thinhlh down --rmi all --volumes
docker-compose --context remote-server-thinhlh --env-file .env up -d
docker-compose --context remote-server-thinhlh logs --follow