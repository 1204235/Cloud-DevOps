# Cloud-DevOps

Steps followed to complete the Challenge for Cloud DevOps
1. created 2 EC2 Instances(1 for Ansible and 1 for Jenkins) using CloudFormation templates(CF-EC2-For-Ansible.yml / CF-EC2-For-Jenkins.yml).
2. Established SSH connectivity between above 2 ec2 Instances.
3. Created Java playbook on Ansible EC2 instance and installed java on Jenkins ec2 instance.
4. Created Dependencies playbook on Ansible EC2 instance and installed dependencies required for Jenkins on Jenkins ec2 instance.
5. Created jenkins playbook on Ansible EC2 instance and installed Jenkins on Jenkins ec2 instance.

Post creation of 2 EC2 instances using Cloud Formation templates (CF-EC2-For-Ansible.yml / CF-EC2-For-Jenkins.yml) Followed below steps to setup ssh connectivity between Ansible and Jenkins instance to install the Java 8 and jenkins using ansible.
  a. login to Ansible EC2 instance and generate SSH keys.
  b. ssh-keygen
  c. sudo cat ~/.ssh/id_rsa.pub #copy content of this file and paste it in Jenkins EC2 instance.
  d. sudo vi ~/.ssh/authorized_keys # This file on Jenkins EC2.
  e. Now try doing SSH from anisble to Jenkins EC2 server using cmd 'ssh IPAdress'
  f. Update the ansible.cfg on ansible server at path 'vi /etc/ansible/hosts'
      [My_Group]
      18.206.153.92 ansible_ssh_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa

Installd Java using playbook.
sudo vi installJava11.yml
sudo ansible-playbook installJava11.yml

Install Jenkins dependencies using playbook.
sudo vi installDependencies.yml
sudo ansible-playbook installDependencies.yml

Install Jenkins using playbook.
sudo vi installJenkins.yml
sudo ansible-playbook installJenkins.yml

Post successful installation of jenkins, able to access URL http://{PUBLIC_IP}:8080

Got the initial password from path :- cat /var/lib/jenkins/secrets/initialAdminPassword on Jenkins EC2 instance.

Installd Docker on jenkins ec2 server to create the docker image and run containers.
sudo amazon-linux-extras install docker
sudo service docker start
sudo service docker status

After successful Jenkins UI setup followed below steps to create jenkins pipeline.
    New Item -> Item Name -> Selected Pipeline -> Under General tab selected GitHub project and added my githut repo url -> under pipeline tab, added contents of         file(Jenkins-pipeline-script) in Scripts.
    

While running the pipeline, got below issue
"sudo: no tty present and no askpass program specified" 
Added below line in visudo file on Jenkins EC2 instance to fix it.
jenkins ALL=(ALL) NOPASSWD: ALL
      
* Post Slack account open, install the 'slack notification' plugin in jenins under manage jenkins > manage plugin.
* Go to Manage jenkins > Configure System > at bottom add slack details.
      
  

