# Project Name
NLP Semantic Similarities

We are comapring words and sentences using POS as well as NLP. At the same time there is a comparitve note between using ‘en_core_web_sm’ and ‘en_core_web_md’

## Prerequisites

- Docker: You need to have Docker installed on your system. You can download and install it from [Docker's official website](https://www.docker.com/get-started).

## Getting Started

These instructions will guide you through building and running the Docker container for this project.

**Clone the Repository**: 
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

**Build the Docker Image**:

Build the Docker image using the provided Dockerfile.

docker build -t your-image-name . (Note: if you intend on running this on Docker Hub From MacOs you will need to change your build to "docker build --platform linux/amd64.")
Replace your-image-name with a suitable name for your Docker image.

**Run the Docker Container**:

Run the Docker container based on the image you just built.

docker run -it your-image-name
This will start the container and run your Python script using PyPy.

**View Output**:

You should see the output of your Python script in the terminal.

## Customization
If you want to customize the behavior of the Docker container or the Python script, you can modify the following files:

Dockerfile: Adjust the Dockerfile to include additional dependencies or make changes to the container environment.
your_script.py: Modify your Python script as needed.

## Contributing
If you'd like to contribute to this project, please follow these steps:

## Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and commit them to your branch.
Submit a pull request with a clear description of your changes.
License
This project is licensed under the [License Name Here] - see the LICENSE.md file for details.

## Acknowledgments
Stackoverflow
Thank you to my personal friends in tech
HyperionDev has had a massive hand in assisting me with tough tasks

