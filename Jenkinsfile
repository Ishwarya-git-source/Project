pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-p')  // Jenkins credentials ID
        IMAGE_NAME = 'flask-app'
        DOCKERHUB_USER = 'ishwarya2001'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-repo-url.git', branch: 'main'
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
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-p') {
                        docker.image("${DOCKERHUB_USER}/${IMAGE_NAME}:latest").push()
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
