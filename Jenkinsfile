node("master"){
    cleanWs()
    stage("Download source code"){
        git branch: 'deploy', credentialsId: 'git-ssh', url: 'git@github.com:roma512/python-app.git'
    }
    // stage("create bom"){
    //     sh "kubeclarity-cli analyze --input-type image 192.168.1.6:9001/docker-local/python-app:01.000.00 -o app.sbom"
    // }
    // stage("check vulnerability"){
    //     sh "kubeclarity-cli scan app.sbom --input-type sbom"
    stage("check SAST"){
        sh "helm upgrade --install python-app . --kube-insecure-skip-tls-verify --kube-apiserver=https://192.168.1.6:8443 --debug --kubeconfig=/home/super/cert/config.json --wait --timeout 60"
    }
    sh "rm -rf /tmp/stereoscope-1*"
    cleanWs()
}