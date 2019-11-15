Install Homebrew
Setting Up Elastic Beanstalk

You will need an AWS Account

[AWS Setup](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)

## Prep for Elastic Beanstalk(Python 3.6+)

1. Install [Homebrew](https://brew.sh)
  1. ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```
2. Install Python 3 (via Homebrew)
  1. ```brew install python3```
  2. Make python3 the default
      1. Open _~/.zshrc_
      2. Add ```alias python=/usr/local/bin/python3```
      3. Save & Exit
      4. ```source ~/.zshrc```

## Restructure your project
1. Move all files into Root directory
2. rename app.py to application.py
3. change all references of ```app``` to ```application```
4. comment out ```app.run()```
5. comment out any methods that have external dependencies, such as Redis
6. Remove any virtual environment directories
7. Install virtualenv
  1. ```pip3 install virtualenv```
8. Create virtual environment
  1. ```virtualenv virt```
9. Activate virtual environment
  1. ```source virt/bin/activate```
10. Install Flask
  1. ```pip install Flask```
11. Create new requirements.txt
  1. ```pip freeze > requirements.txt```
6. Test that it works
  1. ```env FLASK_APP=application.py flask run```

## Setup The application in Elastic Beanstalk
1. Create .ebignore file
  1. add
  >virt
  2. And anything else you don't really need to operate the application
1. Install EB CLI
  2. ```git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git```
  3. ```python3 aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py```
2. Setup the EB repository
  1. ```eb init -p python-3.6 flask-demo --region us-east-1```
  2. If you log into AWS and pick EB you should see your new Application listed
2. Create and deploy
  1. ```eb create flask-dev```
  2. If you log into AWS and pick EB you should see your new environment  listed in your previously created application.
3. Try it out!
  1. ```eb open```
  2. You will probably get a browser to an error page, try adding ```/hello```

Things created with Elastic Beanstalk

- **EC2 instance**
>An Amazon Elastic Compute Cloud (Amazon EC2) virtual machine configured to run web apps on the platform that you choose.
    Each platform runs a specific set of software, configuration files, and scripts to support a specific language version, framework, web container, or combination of these. Most platforms use either Apache or nginx as a reverse proxy that sits in front of your web app, forwards requests to it, serves static assets, and generates access and error logs.
- **Instance security group**
>An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic from the load balancer reach the EC2 instance running your web app. By default, traffic isn't allowed on other ports.
- **Load balancer**
>An Elastic Load Balancing load balancer configured to distribute requests to the instances running your application. A load balancer also eliminates the need to expose your instances directly to the internet.
- **Load balancer security group**
>An Amazon EC2 security group configured to allow inbound traffic on port 80. This resource lets HTTP traffic** from the internet reach the load balancer. By default, traffic isn't allowed on other ports.
- **Auto Scaling group**
>An Auto Scaling group configured to replace an instance if it is terminated or becomes unavailable.
- **Amazon S3 bucket**
>A storage location for your source code, logs, and other artifacts that are created when you use Elastic Beanstalk.
- **Amazon CloudWatch alarms**
>Two CloudWatch alarms that monitor the load on the instances in your environment and that are triggered if the load is too high or too low. When an alarm is triggered, your Auto Scaling group scales up or down in response.
- **AWS CloudFormation stack**
>Elastic Beanstalk uses AWS CloudFormation to launch the resources in your environment and propagate configuration changes. The resources are defined in a template that you can view in the AWS CloudFormation console.
- **Domain name**
>A domain name that routes to your web app in the form subdomain.region.elasticbeanstalk.com.

## Adding Redis support via [ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html)

1. Click create
2. Name your cluster
3. Take note of the port number should be _6379_
4. Change Node type to "_cache.t2.micro_"
  1. Since this is only a demo we don't need really need much space.
5. Click _Create_
6. You will be back at the ElastiCache Dashboard
  1. You should see your new Cluster with a status of _creating_
7. Get your _Primary Endpoint_
8. Replace any local redis hosts with the _Primary Endpoint_
