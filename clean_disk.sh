#!/bin/bash

echo "🔁 Stopping and removing all containers related to this project..."
docker-compose down --volumes --remove-orphans

echo "🧹 Removing dangling images..."
docker image prune -f

echo "🧼 Removing dangling volumes..."
docker volume prune -f

echo "🕸️ Removing unused networks..."
docker network prune -f

echo "✅ Docker cleanup complete."