pipeline {
    agent any
    triggers{
         pollSCM('* * * * *')   
    }
    stages {
        stage('develop') {
            steps {
                sh '../scripts/docker-dev-rafapp.sh'
            }
        }
    }
}
