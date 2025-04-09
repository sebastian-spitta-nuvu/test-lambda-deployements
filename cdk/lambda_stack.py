from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_iam as iam

class LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Crear la función Lambda
        function = _lambda.Function(
            self, "MyLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset('lambda'),
        )

        # Permiso para invocar la función (opcional)
        function.add_to_role_policy(
            policy=iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[function.function_arn]
            )
        )
