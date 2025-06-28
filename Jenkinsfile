pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/Ahmed-MRabie/data-cleaning-jenkins-project.git'
        }

        stage('Run Python Script') {
            steps {
                echo '🐍 Running data cleaning script...'
                sh 'python3 script.py'
            }
        }

        stage('Archive Cleaned File') {
            steps {
                echo '📦 Archiving cleaned data file...'
                archiveArtifacts artifacts: 'cleaned_data.csv', fingerprint: true
            }
        }
    }
}

