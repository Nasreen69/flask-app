pipeline {
    agent any

    environment {
        IMAGE_NAME = 'a1mln0ps/flask'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Nasreen69/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
                            dockerImage.push()
                            dockerImage.push("latest")
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                    kubectl set image deployment/flask-deployment flask=${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }	
    }
}
