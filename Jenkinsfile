pipeline {
    agent any
    trigger{
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
