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

To get started with the FastAPI Weather App, follow these steps:

1. Clone the repository.
2. Set up your configuration in `config.py`.
3. Build the Docker image using the provided `Dockerfile`.
4. Run the Docker container.
5. Access the FastAPI documentation and start fetching weather data!

For Kubernetes deployment, check the `k8e` directory for Helm chart and deployment files.

### Dependencies

Ensure you have the necessary dependencies listed in `requirements.txt` installed to run the FastAPI Weather App successfully.

### Additional Information

Feel free to explore, modify, and enhance the application according to your requirements. Happy coding!
