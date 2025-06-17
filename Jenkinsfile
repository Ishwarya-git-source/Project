pipeline {
    agent any

    environment {
        // define any environment variables you need here
        BUILD_ENV = 'dev'
    }

    stages {
        stage('Clone') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'git clone https://your-repo-url.git'
                    } else {
                        bat 'git clone https://your-repo-url.git'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh './build.sh'
                    } else {
                        bat 'build.bat'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh './test.sh'
                    } else {
                        bat 'test.bat'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh './deploy.sh'
                    } else {
                        bat 'deploy.bat'
                    }
                }
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
