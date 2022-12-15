IMAGE_NAME := return200/sonarqube_exporter

default: build

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: test
test:
	docker run \
		$(IMAGE_NAME) \
		python -m unittest discover -s /lib -p 'test_*.py'
