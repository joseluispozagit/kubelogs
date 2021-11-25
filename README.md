
# Kubelogs

## Requirements
This script have used the follow technologies:

- Operative System: Windows 10
- Python version: 3.9.4


#### Docker Desktop 

Install Docker Desktop in Windows followin the instructions in the next link:

https://docs.docker.com/desktop/windows/install/

####  Minikube

##### You have to install minikube on a Windows host following the follow  link intructions.

#####Open a Power Shell session in admin mode and run the next command in order to install the last version:

    New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
    Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing

#####Add the binary in to your PATH by lauching this command:

    $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
    if ($oldPath.Split(';') -inotcontains 'C:\minikube'){ `
      [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine) `
    }

#####Start your cluster in a Windows Power Shell **with admin perms**, running:
`minikube start`

#####Update to kubectl v1.22.3
`minikube kubectl -- get po -A`

#####Checking the correct installation by running:
`kubectl get po -A`

####Install an nginx deployment in the cluster 


#####Create the Deployment by running the following command:

`kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml`

#####Check if the Deployment was created.

`kubectl get deployments
`
If should appears this output:

`nginx-deployment   1/1     1            1           2d1h
`
#####Then you  make the NGINX container available to the network with the command:

`kubectl expose deployment nginx-deployment --type=NodePort --port=8080
`
Run this command to access to the web, so you can generate logs to see later. Once you have the url in your explorer, you can perform several calls so that you populate the log files in all the pods.

`minikube service nginx-deployment
`
#### Cloning the repo

In your Git bash shell console, choose a dir where you want to clone the report and type:

`git clone https://github.com/joseluispozagit/kubelogs.git kubelogs
`

####  Create and activate venv environment

In your powershell console (with admin user), go to he kubelogs dir and  type:

mkdir venv
python3 -m venv ./venv
source ./venv/bin/activate

####  installing python libs

In your powershell console (with admin user), go to he kubelogs dir and  type:

`pip install -r requirements.txt
`
####  Run the program

In order to run de script, open  a powershell console (with admin user), then go to he kubelogs dir and  type:

`python3 ./kubelogs.py [deploymentname]`
