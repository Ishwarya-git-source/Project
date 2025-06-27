pipeline {
    agent any

    environment {
        CHANGED_SERVICE = '' // declared here, will assign correctly later
    }

    stages {
        stage('Detect Changes') {
            steps {
                script {
                    def changes = bat(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                    if (changes.contains('user-service')) {
                        echo 'User service changed'
                        // set env var properly via `env`
                        env.CHANGED_SERVICE = 'user-service'
                    } else if (changes.contains('product-service')) {
                        echo 'Product service changed'
                        env.CHANGED_SERVICE = 'product-service'
                    } else {
                        error "❌ No known service changed. Skipping build."
                    }
                }
            }
        }

        stage('Clean') {
            when {
                expression { return env.CHANGED_SERVICE }
            }
            steps {
                bat "docker-compose stop ${env.CHANGED_SERVICE} || exit 0"
                bat "docker-compose rm -f ${env.CHANGED_SERVICE} || exit 0"
            }
        }

        stage('Build') {
            when {
                expression { return env.CHANGED_SERVICE }
            }
            steps {
                bat "docker-compose build ${env.CHANGED_SERVICE}"
            }
        }

        stage('Run') {
            when {
                expression { return env.CHANGED_SERVICE }
            }
            steps {
                bat "docker-compose up -d ${env.CHANGED_SERVICE}"
            }
        }

        stage('Test') {
            when {
                expression { return env.CHANGED_SERVICE }
            }
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'user-service') {
                        bat 'curl --fail http://localhost:5001/users || exit 1'
                    } else if (env.CHANGED_SERVICE == 'product-service') {
                        bat 'curl --fail http://localhost:5003/products || exit 1'
                    }
                }
            }
        }
    }
}
