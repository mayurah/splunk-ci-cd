# Splunk CI/CD Template via Ansible

Collection of snippets that can be added to CI/CD pipeline. 


> Note: All these could be containerized for once and all, and could be used in Github Actions or GitLab CI for seamless deployment experience.


## Pre-req to build pipeline

### Authentication

#### Create Token

Tip: Ensure user you create token out of has a `sc_admin` role.

[Create authentication token in Splunk Cloud](https://docs.splunk.com/Documentation/SplunkCloud/9.0.2208/Security/CreateAuthTokens)

### Install Brew

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`


### Install ACS CLI (admin config services)

```
brew tap splunk/tap
brew install acs
```


### Docker Image that could be used in a CI pipeline



### Setting up Env Var

[Docs 📜](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Config/ACSCLI)


```
Read credentials more securely via corresponding environment variables (STACK_USERNAME, STACK_PASSWORD, STACK_TOKEN, SPLUNK_USERNAME, SPLUNK_PASSWORD)
```

Example:
```
export STACK_NAME=wf-poc
export STACK_TYPE=victoria
export STACK_TOKEN=<token>
```



#### Test Playbook:

```sh
cd splunk-ci-cd/splunk-cloud/ansible
ansible-playbook main.yaml


# Apps
ansible-playbook main.yaml --tags "acs,apps"

# Index
ansible-playbook main.yaml --tags "acs,apps"


# Clean ACS Config
ansible-playbook main.yaml --tags "acs-clean"
```



#### Test ACS CLI

```sh
acs config add-stack $STACK_NAME --stack-type $STACK_TYPE
acs config use-stack $STACK_NAME
acs login
acs config current-stack
```


#### Enable REST API via ACS

```sh
# Note that allowing 0.0.0.0/0 means anyone can reach REST API. 
# Maintain allowlist CIDR of internal corporate IP ranges to apply IP based restrictions.
acs ip-allowlist create search-api --subnets=0.0.0.0/0
```


#### Troubleshooting

By default, playbook will return success with no message.

If response is desired, tweak playbook or use `ANSIBLE_STDOUT_CALLBACK=json` before ansible-playbook command.

Playbook shall return stderr if command fails (exit code other than 0). 

Check the values set in environmental variable: $ `env` 
