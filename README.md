# splunk-ci-cd
Collection of snippets that can be added to CI/CD pipeline. 



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
