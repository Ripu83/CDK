#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack


app = cdk.App()
CdkStack(app, "CdkStack",
    env={
    'account':'511283279300', 
    'region': 'us-east-1'
  }
    )

app.synth()
