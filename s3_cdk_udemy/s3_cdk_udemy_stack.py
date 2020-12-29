from aws_cdk import (
    aws_s3 as _s3,
    core
)


class S3CdkUdemyStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "BucketId",
            bucket_name="mycdkmobs399",
            versioned=False,
            encryption=_s3.BucketEncryption.KMS_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL

        )

        mybucket = _s3.Bucket(
            self,
            "myBucketId2"
            )

        # value validation example #################
        snstopicname="abcdef123"

        if not core.Token.is_unresolved(snstopicname) and len(snstopicname) > 10:
            raise ValueError ("Maximum value can not exceed 10 characters")
        
        print (mybucket.bucket_name)
        ################################
        output_1 = core.CfnOutput(
            self,
            "myBucket2Output1",
            value=mybucket.bucket_name,
            description=f"My first CDK Bucket",
            export_name="myBucket2Output1"
        )
