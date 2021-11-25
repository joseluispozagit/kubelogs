from kubernetes.client.rest import ApiException
from kubernetes import client, config
import sys,os

#controlling the number of arguments
print(len(sys.argv))
if len(sys.argv) != 2:
    print("The args number is incorrect") 
    print("Please run: kubelogs.py [deploymentname]")
    exit()

deployment_name = sys.argv[1]

config.load_kube_config()
#pod_name = "counter"
try:
    api_instance = client.CoreV1Api()
    #you go over all the pods from a deployment    
    ret = api_instance.list_pod_for_all_namespaces( watch=False)
    
    #opening the output log file    
    file_object= open(os.path.join(os.path.dirname(os.path.realpath(__file__)), './', deployment_name+'.log'), 'a',encoding="utf-8")
    for i in ret.items:
        if   deployment_name in i.metadata.name:             
            api_response_log = api_instance.read_namespaced_pod_log(name=i.metadata.name, namespace='default')            
            file_object.write("Getting logs from pod: %s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name)+ '\n')
            file_object.write(api_response_log+ '\n')
    file_object.close()
    print("You can see the log in the file: "+ deployment_name+'.log')
except ApiException as e:
    print('Found exception in reading the logs')