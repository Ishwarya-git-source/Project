pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-p')  // DockerHub creds
        IMAGE_NAME = 'flask-app'
        DOCKERHUB_USER = 'ishwarya2001'
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
            withDockerRegistry(credentialsId: 'dockerhub-credentials', url: '') {
                timeout(time: 5, unit: 'MINUTES') {
                    bat "docker tag ishwarya2001/flask-app:latest index.docker.io/ishwarya2001/flask-app:latest"
                    bat "docker push index.docker.io/ishwarya2001/flask-app:latest"
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
