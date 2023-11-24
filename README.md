## FastAPI Weather App

### Application Overview

Welcome to the FastAPI Weather App repository! This application leverages FastAPI to fetch weather data for a specified city and country from the OpenWeatherMap API, processing the results for convenient use. The weather data is then saved to a JSON file, providing a seamless and efficient way to obtain and store weather information.

### Directory Structure

- **`k8e`**: Helm chart for the FastAPI Weather App.
  - `deployment.yaml`: Kubernetes deployment configuration.
  - `configmap.yaml`: ConfigMap for configuration settings.

- **`src`**: Source code for the FastAPI Weather App.
  - `config.py`: Configuration settings for the application.
  - `main.py`: Main FastAPI application file.
  - `utils.py`: Utility functions for the application.
  - `weather_data.py`: Handles the processing of weather data.

- **Additional Files**:
  - `Dockerfile`: Docker configuration for containerizing the application.
  - `requirements.txt`: Python dependencies required for the application.
  - `weather_data.json`: JSON file to store the fetched and processed weather data.

### Getting Started

To begin using the FastAPI Weather App, you have two options:
Option 1:
1. Clone the repository.
2. Set up your configuration in `config.py`.
3. Build the Docker image using the provided `Dockerfile`.
4. Run the Docker container.
5. Access the FastAPI documentation and start fetching weather data!

Option 2:
Utilize Kubernetes deployment:

Check the k8e directory for deployment files.
If needed, make adjustments to the ConfigMap values in the configmap.yaml file or update the image tag, city, and country parameters within the containers section of the deployment file."


### Dependencies
Docker


