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

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/javaci001/EGITIM-SART.git'
            }
        }

        stage('Test Word Count') {
            steps {
                sh 'docker cp spark-ornek1.py spark-master:/spark/bin/spark-ornek2.py'
            }
        }


    }
}