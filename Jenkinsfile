pipeline {
    agent any

    environment {
        CHANGED_SERVICE = ''
    }

    stages {
        stage('Detect Changes') {
            steps {
                script {
                    def changes = bat(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                    if (changes.contains('user-service')) {
                        env.CHANGED_SERVICE = 'user-service'
                    } else if (changes.contains('product-service')) {
                        env.CHANGED_SERVICE = 'product-service'
                    } else {
                        error "No known service changed. Skipping build."
                    }
                }
            }
        }

        stage('Clean') {
            steps {
                bat "docker-compose stop %CHANGED_SERVICE% || exit 0"
                bat "docker-compose rm -f %CHANGED_SERVICE% || exit 0"
            }
        }

        stage('Build') {
            steps {
                bat "docker-compose build %CHANGED_SERVICE%"
            }
        }

        stage('Run') {
            steps {
                bat "docker-compose up -d %CHANGED_SERVICE%"
            }
        }

        stage('Test') {
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'user-service') {
                        bat 'curl --fail http://localhost:5001/users || exit 1'
                    } else if (env.CHANGED_SERVICE == 'product-service') {
                        bat 'curl --fail http://localhost:5002/products || exit 1'
                    }
                }
            }
        }
    }
}
