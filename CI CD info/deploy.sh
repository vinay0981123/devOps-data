#!/bin/bash

set -e  # Exit immediately if any command fails

echo "Pulling the latest image..."
docker-compose pull ezzygo

echo "Stopping and removing the existing container..."
docker-compose down

echo "Deploying the updated container..."
docker-compose up -d --force-recreate

echo "Removing unused Docker images..."
docker image prune -f

echo "Deployment completed successfully!"
