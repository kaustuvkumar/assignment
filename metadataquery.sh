#!/bin/bash
yum install -y jq
echo enter the metadata key 
read INPUT
OUTPUT=`curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq .$INPUT -r`
ECHO $OUTPUT