#!/usr/bin/env python3
import cdk
from cdk.lambda_stack import LambdaStack

app = cdk.App()
LambdaStack(app, "LambdaStack")
app.synth()
