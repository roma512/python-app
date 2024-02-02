node("master"){
    cleanWs()
    stage("Download source code"){
        git branch: 'deploy', credentialsId: 'git-ssh', url: 'git@github.com:roma512/python-app.git'
    }
    stage("Deploy in kubernetes"){
        sh "helm upgrade --install python-app . --kube-insecure-skip-tls-verify --kube-apiserver=https://192.168.1.6:8443 --debug --kubeconfig=/home/super/cert/config.json --wait"
    }
    cleanWs()
}