node("master"){
    cleanWs()
    stage("Download source code"){
        git branch: 'deploy', credentialsId: 'git-ssh', url: 'git@github.com:roma512/python-app.git'
    }
    stage("check SAST"){
        sh "helm install python-app . --kube-apiserver=https://192.168.1.6:8443 --namespace=default --insecure-skip-tls-verify"
    }
    cleanWs()
}