pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'microservices_project'
    }

    stages {
        stage('Clean') {
            steps {
                bat 'docker-compose down --remove-orphans || exit 0'
                bat 'docker system prune -f || exit 0'
            }
        }

        stage('Build Images') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Run Services') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test User Service') {
            steps {
                bat 'curl --fail http://localhost:5001/users || exit 1'
            }
        }

        stage('Test Product Service') {
            steps {
                bat 'timeout /T 5 /NOBREAK' // wait for 5 seconds (Windows shell)
                bat 'curl --fail http://localhost:5002/products || exit 1'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker-compose down || exit 0'
        }
    }
}
