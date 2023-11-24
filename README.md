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


## Jenkinsfile for FastAPI Deployment

This Jenkinsfile is designed to automate the deployment of a FastAPI application to a Kubernetes cluster. The pipeline consists of two stages: checking out the source code from a GitHub repository and deploying the application to Kubernetes.

### Prerequisites

- **Jenkins:** Ensure that you have Jenkins installed and configured with the necessary plugins for GitHub integration and Kubernetes deployments.

### Usage

1. **Configure Jenkins:**
   - Set up Jenkins with the required credentials:
     - `fastapi-id`: Kubernetes configuration credentials.
     - `github-credentials-id`: GitHub credentials for repository access.

2. **Pipeline Parameters:**
   - This pipeline requires a user to select the target environment during execution. The available options are 'dev', 'stage', and 'prod.'

3. **GitHub Repository:**
   - Update the `GITHUB_REPO_URL` variable in the Jenkinsfile to point to your FastAPI application's GitHub repository.

4. **Pipeline Execution:**
   - Run the Jenkins job, and it will prompt you to select the target environment before starting the deployment pipeline.

### Jenkinsfile Overview

- **Agent:** The pipeline is configured to run on any available Jenkins agent.
  
- **Environment Variables:**
  - `KUBECONFIG`: Kubernetes configuration credentials.
  - `K8S_NAMESPACE`: Target Kubernetes namespace.
  - `K8S_DEPLOYMENT_NAME`: Name of the Kubernetes deployment.
  - `GITHUB_REPO_URL`: URL of the GitHub repository.

- **Stages:**
  1. **Checkout:**
     - Clones the GitHub repository to the Jenkins workspace.

  2. **Deploy to Kubernetes:**
     - Uses `kubectl` to apply the Kubernetes deployment YAML from the GitHub repository to the specified environment.

### Example Usage

```bash
Jenkins Job: FastAPI-Deployment
Parameters: ENVIRONMENT = dev
