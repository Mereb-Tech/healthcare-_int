pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app:latest'
        DOCKER_REGISTRY = 'my-docker-registry.example.com'
        REGISTRY_CREDENTIALS = 'docker-registry-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository containing the application code
                //removed my git here
                 git branch: 'main', url: 'https://github.com/ '
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {

                    // assumes we have unit test invation here
                    docker.image("${DOCKER_IMAGE}").inside {
                        sh 'python -m unittest discover'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Push Docker image to Docker registry
                    docker.withRegistry('https://${DOCKER_REGISTRY}', "${REGISTRY_CREDENTIALS}") {
                        docker.image("${DOCKER_IMAGE}").push('latest')
                    }

                    // Optionally deploy to a local environment or remote server
                    // Example: Run Docker container locally (uncomment if needed)
                    // sh 'docker run -d --name my-python-app -p 8080:8080 ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images
            sh 'docker system prune -af'
        }
    }
}
