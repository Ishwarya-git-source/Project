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
                bat '''
                set RETRIES=5
                set WAIT=3
                set COUNT=0
                :retry
                curl --fail http://localhost:5002/products && goto success
                set /a COUNT+=1
                if %COUNT% GEQ %RETRIES% goto fail
                timeout /t %WAIT% > nul
                goto retry
                :fail
                exit 1
                :success
                echo Product service is up!
                '''
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
