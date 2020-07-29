# DFly is a software development platform that enables developers to seamlessly develop and deploy their applications to public cloud. For now, dfly offers its PaaS on AWS. To develop applications on dfly, it is expected that developers are familiar with Kubernetes ecosystem and basic usage of kubectl.
#**************************|**************************|**************************|**************************
#Candidate should provide every developer a website with a simple message: "Welcome to Dfly"
#**************************|**************************|**************************|**************************
#2. The web application should be checked into a git repository (github or gitlab) and should be open for other developers to submit Pull-Requests
#3. The repository should be equipped with a CI-CD pipeline. It can be a Jenkins/Travis-CI/Circle-CI/any-CI pipieline that does the continuous deployments
#4. Provision a Kubernetes Cluster on AWS - can be EKS or KOPS using Terraform or CloudFormation
#5. Dockerize the application developed in step(1) and deploy the application to the kubernetes cluster provisioned above
#6. Submit a Pull-Request to the git repository in step(2) and the CI-CD pipeline should push the changes to Kubernetes cluster
