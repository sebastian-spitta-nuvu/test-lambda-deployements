from aws_cdk import core
from lambda_stack import LambdaStack

app = core.App()
LambdaStack(app, "MyLambdaStack")
