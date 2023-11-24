FastAPI Weather App
Welcome to the FastAPI Weather App repository! This application leverages FastAPI to fetch weather data for a specified city and country from the OpenWeatherMap API, processing the results for convenient use. The weather data is then saved to a JSON file, providing a seamless and efficient way to obtain and store weather information.

Features
FastAPI Framework: Utilizing the FastAPI framework for high-performance API development with automatic interactive documentation.
OpenWeatherMap API Integration: Fetching real-time weather data from the OpenWeatherMap API to provide accurate and up-to-date information.
JSON Data Storage: Saving processed weather data to a JSON file for easy retrieval and analysis.
Docker Containerization: The application can be run as a Docker container, ensuring consistent and reliable deployment across different environments.
Directory Structure
k8e: Contains Kubernetes deployment YAML files and a ConfigMap for streamlined deployment on Kubernetes clusters.

deployment.yaml
configmap.yaml
src: Holds all the source code for the FastAPI Weather App.

config.py: Configuration settings for the application.
main.py: Main FastAPI application file.
utils.py: Utility functions for the application.
weather_data.py: Handles the processing of weather data.
Additional Files:

Dockerfile: Docker configuration for containerizing the application.
requirements.txt: Lists the Python dependencies required for the application.
weather_data.json: JSON file to store the fetched and processed weather data.
Getting Started
To get started with the FastAPI Weather App, follow these steps:

Clone the repository.
Set up your configuration in config.py.
Build the Docker image using the provided Dockerfile.
Run the Docker container.
Access the FastAPI documentation and start fetching weather data!
For Kubernetes deployment, check the k8e directory for deployment files and configuration.

Dependencies
Ensure you have the necessary dependencies listed in requirements.txt installed to run the FastAPI Weather App successfully.

Feel free to explore, modify, and enhance the application according to your requirements. Happy coding!