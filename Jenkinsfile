pipeline {
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'stage', 'prod'], description: 'Select the target environment')
    }

    agent any

    environment {
        KUBECONFIG = credentials('fastapi-id')
        K8S_NAMESPACE = 'fastapi-dev'
        K8S_DEPLOYMENT_NAME = 'deployment-fast-api.yml'
        GITHUB_REPO_URL = 'https://github.com/hodafa/fastapi.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', credentialsId: 'github-credentials-id', url: GITHUB_REPO_URL
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl --kubeconfig=${KUBECONFIG} --context=${ENVIRONMENT} apply -f fastapi/${K8S_DEPLOYMENT_NAME} -n ${K8S_NAMESPACE}"
                }
            }
        }
    }
}
