pipeline {
    agent any

    stages {
        stage('Clean') {
            steps {
                sh 'docker-compose down --remove-orphans || true'
                sh 'docker system prune -f || true'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Services') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test User Service') {
            steps {
                sh 'curl --fail http://localhost:5001/users'
            }
        }

        stage('Test Product Service') {
            steps {
                sh 'curl --fail http://localhost:5002/products || true'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker-compose down'
        }
    }
}
