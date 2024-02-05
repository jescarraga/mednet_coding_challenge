# MedNet - Coding Challenge

This project is a API that converts a given number and his Unit of weight, height or distance to another unit of the same type.

Also allow to add or subtract two numbers on different units of weight, height or distance.

* All of the two projects have a README.md file, but the content is different. For the API, the readme also explains how to run the project locally and make some test.
  
* **TO RUN THE PROJECT LOCALLY, YOU NEED TO USE DOCKER-COMPOSE FILE**

# Assumptions

* The API will only convert between the following units:
    - Weight: kg, g, lb, oz
    - Height: cm, m, in, ft
    - Distance: km, m, cm, mi

* The API will only add or subtract between the any of the previous units.

* The API will only accept positive numbers.

* The API was developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints and WSL2 as the development environment with docker.

* The APi has swagger documentation, you can access it on the following url: http://localhost:8000/docs

* The API has tests only for the local deployment, withouth docker.

* The user have installed : 
    - Docker
    - Docker-compose
    - Git
    - Bash terminal
    - WSL2 (Windows Subsystem for Linux)
    - Python 3.7+
    - pip
    - venv
  
# Author

Hi everyone, I am Jordan Escarraga and I am a backend developer, focused on data-driven solutions.

# Local Setup

1. Open the bash terminal on linux 
   
        cd scripts

2. Run the following command to build the two docker images

        bash build_and_deploy.sh

3. Access the following url on your browser to access the API swagger documentation

        http://localhost:8000/docs

4. Access the following url on your browser to access the user interface
    
        http://localhost:8501/convert

5. Prove the API and the user interface

6. To deactivate the containers, run the following command

        docker-compose down