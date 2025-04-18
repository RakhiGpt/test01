pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git url: 'https://github.com/RakhiGpt/test01.git', branch: 'main'
            }
        }

        stage('Setup Dependencies') {
            steps {
                echo "setting up python virtual environment and installing dependencies"
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        
        stage('Run OTP Generator') {
            steps {
                echo "Executing otp.py"
                bat '''
                call venv\\Scripts\\activate 
                python otp.py
                '''
            }
        }

        stage('Run tests') {
            steps {
                echo "running test_otp.py"
                bat '''
                call venv\\Scripts\\activate 
                python test_otp.py
                '''
            }
        }
    }
}
                           
      