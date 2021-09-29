# assignment

##################################################################################################
Assignment 1

File name : assignmentq1.json

Cloudformation template creates VPC with Private Subnets in 2 AZs 

Gives option to choose different Availability Zones for Subnet 1 and Subnet 2 , creates internet & NAT gateways and respective route table associations.

Enables VPC Flow Logs Role and creates the role if does not already exists

Creates required security group websg, appsg & databasesg with ingress rules for the 3 tiers.

For launching EC2 for web ,app and DB instance gives option to select the required EC2 instance type. Also created autoscaling group and launch configurations for the web ,app and DB layer to provide High Availibility.

####################################################################################################
Assignment 2

File name : meatadataquery.sh

This a bash script to curl the metadata of ec2  (http://169.254.169.254/latest/dynamic/instance-identity/document)

Input should be provided as the metatdata key that should be queries (i.e region ,accountId)


####################################################################################################

Assignment 3

File name: extractValue.py

This a python code written to extract value for a given key in 3 level nested object.

Code has function written to take two input one a nested object and the other keys separated by '/' deliminator.

Same file has few test written to test both poitive nad negative scenario.

(Note: key and value are considered as String)





