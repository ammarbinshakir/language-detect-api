#!/bin/bash

if [ "$1" == "dev" ]; then
  echo "🧪 Starting in DEV mode with auto-reload..."
  docker compose --profile dev up --build
elif [ "$1" == "prod" ]; then
  echo "🚀 Starting in PROD mode..."
  docker compose --profile prod up --build
else
  echo "❌ Please specify mode: dev or prod"
  echo "Usage: ./run.sh dev"
fi
