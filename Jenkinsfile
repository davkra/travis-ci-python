pipeline {
  agent { label 'develop' }
  stages {
    stage('Install Dependencies') {
      steps {
            sh 'pip install -r requirements.txt'
            sh 'pip install pytest'
      }
    }
    stage('Run Tests') {
      steps {
            sh 'pytest'
      }
    }
  }
}
