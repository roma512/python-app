node("master"){
    cleanWs()
    stage("Download source code"){
        git credentialsId: 'git-ssh', url: 'git@github.com:roma512/python-app.git'
    }
    stage("Compilation app"){
        sh"""pyinstaller --add-data "templates/profile.html:templates/profile.html" --add-data "templates/vulnerable.html:templates/vulnerable.html" sql-injection.py"""
    }
    stage("Build image"){
        sh "docker build -t python-app ."
    }
    stage("Tag image"){
        sh "docker tag python-app registry.local:9001/docker-local/python-app:01.000.00"
    }
    stage("Registry login"){
        withCredentials([usernamePassword(credentialsId: 'nexus-cred', passwordVariable: 'pass', usernameVariable: 'user')]) {
            sh "docker login -u ${user} -p ${pass} registry.local:9001"
        }
    }
    stage("Push image in registry"){
        sh "docker push registry.local:9001/docker-local/python-app:01.000.00"
    }
    cleanWs()
}