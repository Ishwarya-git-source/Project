pipeline {
    agent any

    stages {
        stage('Clean') {
            steps {
                bat 'docker-compose down --remove-orphans || true'
                bat 'docker system prune -f || true'
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
                bat 'curl --fail http://localhost:5001/users'
            }
        }

        stage('Test Product Service') {
            steps {
                bat 'curl --fail http://localhost:5002/products || true'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker-compose down'
        }
    }
}
