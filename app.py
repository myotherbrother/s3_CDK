#!/usr/bin/env python3

from aws_cdk import core

from s3_cdk_udemy.s3_cdk_udemy_stack import S3CdkUdemyStack


app = core.App()
S3CdkUdemyStack(app, "s3-cdk-udemy")

app.synth()
