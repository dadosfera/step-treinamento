#!/bin/bash

pip3 install pyOpenSSL --upgrade
pip3 install awscli pandas
aws codeartifact login --tool pip --domain dadosfera --domain-owner 611330257153 --region us-east-1 --repository dadosfera-pip
pip3 install dadosfera==1.6.0b1 dadosfera_logs==1.0.3