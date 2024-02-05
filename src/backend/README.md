# MedNet - Coding Challenge

This project is a API that converts a given number and his Unit of weight, height or distance to another unit of the same type.

Also allow to add or subtract two numbers on different units of weight, height or distance.

# Assumptions

* The API will only convert between the following units:
    - Weight: kg, g, lb, oz
    - Height: cm, m, in, ft
    - Distance: km, m, cm, mi

* The API will only add or subtract between the any of the previous units.

* The API will only accept positive numbers.

* The API was developed using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints and WSL2 as the development environment with docker.
  
# Author

Hi everyone, I am Jordan Escarraga and I am a backend developer, focused on data-driven solutions.

# Local Setup

1. Create a virtual environment, if you don't have one already

        py -m venv mednet-coding-challenge-api
        
or you can use python3

        python3 -m venv mednet-coding-challenge-api

1. Activate the virtual environment

    On Windows powershell

        .\mednet-coding-challenge-api\Scripts\activate

    On Windows using git bash

        source mednet-coding-challenge-api/Scripts/activate

    On linux

        source mednet-coding-challenge-api/bin/activate

2. Install the dependencies

       python3 -m pip install -r requirements.txt

3. **OPTIONAL** if you need add the required packages to the requirements.txt file, run the following command

        pip freeze > requirements.txt

4. **OPTIONAL** If you need to deactivate the virtual environment, run the following command
   
        deactivate

5. To run the tests, run the following command

        pytest

    And if you have problems with the execution of the tests, you can run the following command on la linux terminal

        export PYTHONPATH=$PWD

6. To run only the APi. without docker, run the following command

        python3 -m uvicorn app.main:app --reload

# Docker Setup

1 Build the image

        docker build --no-cache -t mednet-code-challenge-api .

2 Run the container

        docker run -p 8080:8080 --name mednet-code-challenge-api mednet-code-challenge-api