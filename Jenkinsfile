pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    sh '''
                        docker-compose -f $DOCKER_COMPOSE_FILE up -d --build
                    '''
                }
            }
        }

        stage('Run Testes Mocks') {
            steps {
                script {
                    sh '''
                        docker-compose exec -T fastapi robot tests/mocks
                    '''
                }
            }
        }

        stage('Run Testes de Implementacao') {
            steps {
                script {
                    sh '''
                        docker-compose exec -T fastapi robot tests/implementacao
                    '''
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            sh 'docker-compose down --volumes --remove-orphans'
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
