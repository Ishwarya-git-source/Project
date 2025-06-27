pipeline {
    agent any

    environment {
        CHANGED_SERVICE = ''
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Detect Changes') {
            steps {
                script {
                    def changes = bat(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                    echo "🔍 Changed files:\n${changes}"

                    if (changes.contains('user-service')) {
                        env.CHANGED_SERVICE = 'user-service'
                    } else if (changes.contains('product-service')) {
                        env.CHANGED_SERVICE = 'product-service'
                    } else {
                        echo "ℹ️ No specific service changed — running all services."
                        env.CHANGED_SERVICE = 'all'   // ✅ Properly assign to env
                    }

                    echo "✅ CHANGED_SERVICE: ${env.CHANGED_SERVICE}"
                }
            }
        }

        stage('Clean') {
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'all') {
                        bat 'docker-compose stop || exit 0'
                        bat 'docker-compose rm -f || exit 0'
                    } else {
                        bat "docker-compose stop ${env.CHANGED_SERVICE} || exit 0"
                        bat "docker-compose rm -f ${env.CHANGED_SERVICE} || exit 0"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'all') {
                        bat 'docker-compose build'
                    } else {
                        bat "docker-compose build ${env.CHANGED_SERVICE}"
                    }
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'all') {
                        bat 'docker-compose up -d'
                    } else {
                        bat "docker-compose up -d ${env.CHANGED_SERVICE}"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (env.CHANGED_SERVICE == 'user-service' || env.CHANGED_SERVICE == 'all') {
                        bat 'curl --fail http://localhost:5001/users || exit 1'
                    }
                    if (env.CHANGED_SERVICE == 'product-service' || env.CHANGED_SERVICE == 'all') {
                        bat 'curl --fail http://localhost:5003/products || exit 1'
                    }
                }
            }
        }
    }
}
