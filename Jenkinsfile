parameters {
        string(name: 'branch', defaultValue: 'master', description: 'branch to test')		
		string(name: 'testServerUrl', defaultValue: 'https://auckland-words-cloud-staging.dynabic.com', description: 'server url')		
}

def runtests(dockerImageVersion)
{
    dir(dockerImageVersion){
        try {
            stage('checkout'){
                checkout([$class: 'GitSCM', branches: [[name: '*/' + params.branch]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '9d6c4dfa-042c-4ed1-81c7-9175179dddda', url: 'https://github.com/aspose-words-cloud/aspose-words-cloud-python.git/']]])
                withCredentials([usernamePassword(credentialsId: '6839cbe8-39fa-40c0-86ce-90706f0bae5d', passwordVariable: 'AppKey', usernameVariable: 'AppSid')]) {
					sh 'mkdir -p Settings'
                    sh 'echo "{\\"AppSid\\": \\"$AppSid\\",\\"AppKey\\": \\"$AppKey\\", \\"BaseUrl\\": \\"${testServerUrl}\\"}" > Settings/servercreds.json'
                }
            }
			docker {
				image 'python:' + dockerImageVersion
				args '-u root:sudo -v /home/jenkins/workspace/aspose-for-cloud/words-sdk-python/' + dockerImageVersion + ':/home/jenkins/workspace/aspose-for-cloud/words-sdk-python/' + dockerImageVersion
			}
            
            docker.inside{
                stage('build'){
					sh "pip install -r requirements.txt && pip install -r test-requirements.txt"
                }
            
                stage('tests'){   
					sh "python -m unittest discover -v -s ."
                }
            
                stage('bdd-tests'){
					
                }
            }        
        } finally {                       
            deleteDir()
        }
    }
}

node('billing-qa-ubuntu-16.04.4') {
    runtests("2.7.15")
	runtests("3.6")          
}