pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/Ahmed-MRabie/data-cleaning-jenkins-project.git'
            }
        }

        stage('Run Python Script') {
            steps {
                echo '🐍 Running data cleaning script...'
                sh 'bash -c "source /opt/jenkins_venv/bin/activate && python3 script.py"'

            }
        }

        stage('Push Cleaned Data to GitHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    sh '''
                        git config --global user.email "ahmedmrabie525@gmail.com"
                        git config --global user.name "$GIT_USER"

                        git remote set-url origin https://$GIT_USER:$GIT_PASS@github.com/Ahmed-MRabie/data-cleaning-jenkins-project.git
                        git add cleaned_data.csv
                        git commit -m "Add cleaned data from Jenkins job" || echo "No changes to commit"
                        git push origin master
                    '''
                }
            }
        }

    }
}
