
# boto is Amazon's python library

import boto
import configparser

# Thaw takes a single configuration file of the format:
#
# 	[SECTION]
# 	configitem = value
#
# It expects one section with the values:
# [DEFAULT]
# aws_access_key_id = <value>
# aws_secret_access_key = <value>
# aws_sns_topic_arn = <value>
# aws_glacier_vault_id = <value>


config = configparser.ConfigParser()

ACCESS_KEY_ID = config['DEFAULT']['aws_access_key_id']
SECRET_ACCESS_KEY = config['DEFAULT']['aws_secret_access_key']
SNS_TOPIC = config['DEFAULT']['aws_sns_topic_arn']
VAULT_ID = config['DEFAULT']['aws_glacier_vault_id']

# Connection to Glacier

glacier_connection = boto.connect_glacier(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

# Connect to specific vault

vault = glacier_connection.get_vault(VAULT_ID)

# initiate a job to retrieve the vault inventory

inventory_job = vault.retrieve_inventory(sns_topic=SNS_TOPIC)

print(inventory_job)