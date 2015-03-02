# Mostly copied from the official amon-plugins repo
# https://github.com/amonapp/amon-plugins/blob/master/Makefile

clean:
	rm -f Dockerfile

test: clean
	cp Dockerfile.build Dockerfile
	docker build --rm=true .
	rm Dockerfile

# Build the base container -> amonbase
init: clean
	docker pull phusion/baseimage
	cp Dockerfile.init Dockerfile
	docker build -t amonbase .