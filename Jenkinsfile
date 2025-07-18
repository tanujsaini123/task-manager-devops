pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/tanujsaini123/devops-image-quote-app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t image-quote-app .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerHubcreds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag image-quote-app:latest $DOCKER_USER/image-quote-app:latest
                        docker push $DOCKER_USER/image-quote-app:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
                sh 'kubectl rollout restart deployment image-quote-app'
                sh 'kubectl port-forward svc/image-quote-service 5000:5000 --address=0.0.0.0 &'
            }
        }
    }
}
