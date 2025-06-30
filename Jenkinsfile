pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Detect, Build and Run Changed Service') {
            steps {
                script {
                    def changedFiles = bat(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                    echo "🔍 Changed files:\n${changedFiles}"

                    def changedService = ''
                    if (changedFiles.contains('user-service')) {
                        changedService = 'user-service'
                    } else if (changedFiles.contains('product-service')) {
                        changedService = 'product-service'
                    } else {
                        echo "ℹ️ No specific service changed — running all services."
                        changedService = 'all'
                    }

                    // CLEAN
                    if (changedService == 'all') {
                        bat "docker-compose down --remove-orphans || exit 0"
                    } else {
                        bat "docker-compose stop ${changedService} || exit 0"
                        bat "docker-compose rm -f ${changedService} || exit 0"
                    }

                    // BUILD
                    if (changedService == 'all') {
                        bat "docker-compose build"
                    } else {
                        bat "docker-compose build ${changedService}"
                    }

                    // RUN
                    if (changedService == 'all') {
                        bat "docker-compose down || exit 0"
                        bat "docker-compose up -d"
                    } else {
                        bat "docker-compose up -d ${changedService}"
                    }

                    // WAIT before testing
                    echo "⏳ Waiting for service to be ready..."
                    sleep time: 10, unit: 'SECONDS'

                    // TEST
                    if (changedService == 'user-service' || changedService == 'all') {
                        retry(3) {
                            bat 'curl --fail http://localhost:5011/users || exit 1'
                        }
                    }

                    if (changedService == 'product-service' || changedService == 'all') {
                        retry(3) {
                            bat 'curl --fail http://localhost:5003/products || exit 1'
                        }
                    }
                }
            }
        }
    }
}
