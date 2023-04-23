VERSION=$1
docker build --file ./docker/auth/Dockerfile --tag www.thinhlh.com/auth_service:${VERSION} .
docker push www.thinhlh.com/auth_service:${VERSION}