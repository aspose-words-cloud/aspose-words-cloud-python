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
            
            docker.image('python:' + dockerImageVersion).inside('-u root'){
                stage('build'){
					sh "python -m pip install -r requirements.txt && python -m pip install -r test-requirements.txt"
				}
            
                stage('tests'){
					try{
						sh "nosetests --with-xunit"
					} finally{
						junit 'nosetests.xml'
					}
                }
            
                stage('bdd-tests'){
					
                }
				
				stage('clean-compiled'){
					sh "rm -rf %s"
				}
            }        
        } finally {
			 cleanWs()
        }
    }
}

node('billing-qa-ubuntu-16.04.4') {
	stage('oldpy'){
		try {
			runtests("2.7.15")
		} finally {
			cleanWs()
		}
	}
	
	stage('newpy'){
		try {
			runtests("3.6") 
		} finally {
			cleanWs()
		}
	}
}