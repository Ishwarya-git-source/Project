pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'ishwarya2001'
        IMAGE_NAME = 'flask-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-p', url: 'https://github.com/Ishwarya-git-source/Project.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKERHUB_USER}/${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Make sure you have a Jenkins credential with ID 'dockerhub-credentials'
                    withDockerRegistry(credentialsId: 'dockerhub-credentials', url: '') {
                        timeout(time: 5, unit: 'MINUTES') {
                            bat "docker tag ${DOCKERHUB_USER}/${IMAGE_NAME}:latest index.docker.io/${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                            bat "docker push index.docker.io/${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
