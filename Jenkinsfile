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

        stage('hostname yaz') {
            steps {
                sh 'hostname -f'
            }
        }   

        stage('git clone yap') {
            steps {
                git branch: 'main', url: 'https://github.com/javaci001/EGITIM-SART.git'
            }
        }

        stage('dosyayi gonder') {
            steps {
                sh 'docker cp /var/lib/jenkins/workspace/pipeline1/spark-ornek1.py spark-master:/spark/bin/spark-ornek2.py'
            }
        }


    }
}