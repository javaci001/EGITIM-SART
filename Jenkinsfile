pipeline {
    agent any
        stages {
            stage('Hello') {
                steps {
                    echo 'Hello World'
                }
            }
        stage('Log date') {
            steps {
                sh 'date'
            }
        }   

        stage('Log date 2') {
            steps {
                sh 'hostname -f'
            }
        }   
    }
}