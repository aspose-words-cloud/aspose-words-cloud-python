parameters {
        string(name: 'branch', defaultValue: 'master', description: 'branch to test')		
		string(name: 'apiUrl', defaultValue: 'https://api-qa.aspose.cloud', description: 'server url')		
}

def runtests(dockerImageVersion)
{
    dir(dockerImageVersion){
        try {
            stage('checkout'){
				checkout([$class: 'GitSCM', branches: [[name: params.branch]], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'LocalBranch', localBranch: "**"]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '361885ba-9425-4230-950e-0af201d90547', url: 'https://git.auckland.dynabic.com/words-cloud/words-cloud-python.git']]])
                withCredentials([usernamePassword(credentialsId: '6839cbe8-39fa-40c0-86ce-90706f0bae5d', passwordVariable: 'AppKey', usernameVariable: 'AppSid')]) {
					sh 'mkdir -p Settings'
                    sh 'echo "{\\"AppSid\\": \\"$AppSid\\",\\"AppKey\\": \\"$AppKey\\", \\"BaseUrl\\": \\"$apiUrl\\"}" > Settings/servercreds.json'
                }
            }
            
            docker.image('python:' + dockerImageVersion).inside('-u root'){
                stage('build'){
					sh "python -m pip install -r requirements.txt && python -m pip install -r test-requirements.txt"
				}
            
                stage('tests'){
                    try {
                        sh "python -m xmlrunner discover -v -s ."
                    } 
					finally {
                        junit '**\\testReport.xml'
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

node('words-linux') {
	stage('newpy'){
		try {
			runtests("3.7") 
		} finally {
			cleanWs()
		}
	}
}
