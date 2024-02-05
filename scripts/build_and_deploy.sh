#build the two images

# go to the backend directory
cd ../src/backend
docker build --no-cache -t mednet-code-challenge-api .

# go to the frontend directory
cd ..
cd frontend
docker build --no-cache -t mednet-code-challenge-ui .

# go back to the root directory
cd ../../

# deploy the two images
docker-compose -f docker-compose.yml up -d
