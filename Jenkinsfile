pipeline {
  agent any
  stages {
    stage('o') {
      steps {
        git(url: 'https://github.com/marioluan/jenkinsci.git', branch: 'master', changelog: true)
      }
    }
  }
}