set JENKINS_HOME=C:\Users\User\Desktop\EPSI\EPSI_3eme\jenkins\runtime\workspace
set JENKINS_PORT=8090
set JENKINS_CONTEXT=/jenkins

java -jar jenkins.war --httpPort=%JENKINS_PORT% --httpListenAddress=127.0.0.1 --prefix=%JENKINS_CONTEXT% --webroot="%JENKINS_HOME%"