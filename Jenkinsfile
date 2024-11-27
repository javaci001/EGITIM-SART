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
                sh '''
                    docker cp /var/lib/jenkins/workspace/pipeline1/spark_ornek1.py spark-master:/spark/bin/spark_ornek2.py'
                    echo `date` " tarihinde jenkins ile otomatik olarak spark_ornek2.py guncellenmistir " > spark_ornek2_py_deploy_aciklama.txt
                '''
            }
        }


    }
}