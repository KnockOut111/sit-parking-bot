PROJECT_NAME=sit-parking-bot

help:
	@echo "🚀 Makefile commands for $(PROJECT_NAME):"
	@echo "  make build     - Build Docker images"
	@echo "  make up        - Start the container"
	@echo "  make down      - Stop the container"
	@echo "  make logs      - Tail logs from the container"
	@echo "  make shell     - Open shell inside running container"
	@echo "  make clean     - Remove images and containers"
	@echo "  make rebuild   - Force rebuild everything"

# Build the container
build:
	docker-compose build

# Start the scheduled automation
up:
	docker-compose up -d
	@echo "✅ $(PROJECT_NAME) is now running in the background."

# Stopps the project
down:
	docker-compose down 
	@echo "🛑 $(PROJECT_NAME) stopped."

# View logs
logs:
	docker logs -f sit-parking-bot

# Clean all containers, images and volumes
clean:
	$(DOCKER_COMPOSE) down --rmi all --volumes --remove-orphans
	@echo "🧹 Cleaned all containers, images, and volumes."

# Build second time
rebuild:
	docker-compose build --no-cache
	@echo "♻️ Rebuilt from scratch."

fullBuild:
	docker-compose build
	docker-compose up -d 
