pipeline {
    agent any
    stages {
       stage('Build') {
           steps {
                dir (path: "./docker-images/aa-server/") {
                    sh './build-docker-image.sh'
                }
           }
       }
       stage('Unittest') {
           steps {
                dir (path: "./docker-images/aa-unittest/") {
                    sh './build-docker-image.sh'
                    sh './run-docker-image.sh'
                }
                echo 'End of unittest'
           }
       }
       stage('Redeploy') {
           steps {
                dir (path: "./docker-topologies/runtime/") {
                    echo "current directory is: ${pwd()}"
                    sh './export-env-var.sh'
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
           }
       }
       stage('Validation') {
           steps {
               echo 'Check container service is running !'
           }
       }
    }
}
