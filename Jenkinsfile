pipeline {
    agent any

    environment {
        BUILD_ENV = 'dev'
    }

    stages {
        // No Clone stage needed!

        stage('Build') {
            steps {
                bat 'echo Building the app...'
                bat 'dir' // or your actual build command like `npm install`
            }
        }

        stage('Test') {
            steps {
                bat 'echo Running tests...'
                bat 'dir' // or `npm test`, etc.
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                bat "Deploying to Kubernetes..."
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
