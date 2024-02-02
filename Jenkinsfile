node("master"){
    cleanWs()
    stage("Download source code"){
        git credentialsId: 'git-ssh', url: 'git@github.com:roma512/python-app.git'
    }
    stage("check SAST"){
        sh "helm install python-app ."
    }
    cleanWs()
}