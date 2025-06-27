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
                    // Check if there are at least 2 commits
                    def commits = bat(script: 'git log --oneline -2', returnStdout: true).trim().split("\n")
                    if (commits.size() < 2) {
                        echo "🟡 First build detected or only one commit. Building all services."
                        env.CHANGED_SERVICE = 'all'
                    } else {
                        // Check which files were changed
                        def changes = bat(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                        echo "🔍 Changed files:\n${changes}"

                        if (changes.contains('user-service')) {
                            env.CHANGED_SERVICE = 'user-service'
                        } else if (changes.contains('product-service')) {
                            env.CHANGED_SERVICE = 'product-service'
                        } else {
                            error "❌ No known service changed. Skipping build."
                        }
                    }
                }
            }
        }

        stage('Clean') {
            when {
                expression {
                    return env.CHANGED_SERVICE == 'user-service' || env.CHANGED_SERVICE == 'product-service' || env.CHANGED_SERVICE == 'all'
                }
            }
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
            when {
                expression {
                    return env.CHANGED_SERVICE == 'user-service' || env.CHANGED_SERVICE == 'product-service' || env.CHANGED_SERVICE == 'all'
                }
            }
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
            when {
                expression {
                    return env.CHANGED_SERVICE == 'user-service' || env.CHANGED_SERVICE == 'product-service' || env.CHANGED_SERVICE == 'all'
                }
            }
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
            when {
                expression {
                    return env.CHANGED_SERVICE == 'user-service' || env.CHANGED_SERVICE == 'product-service' || env.CHANGED_SERVICE == 'all'
                }
            }
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
