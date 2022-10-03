.PHONY: clean config apps

ANSIBLE_ROOT := ./splunk-cloud/ansible
COLON := :


config: 
	cd $(ANSIBLE_ROOT); \
	pwd; \
	ansible-playbook main.yaml --tags "acs"

apps:
	ansible-playbook main.yaml --tags "apps"


clean:
	ansible-playbook main.yaml --tags "acs-clean"

help:
	echo clean 
