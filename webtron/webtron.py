import boto3
import click

session = boto3.Session(profile_name='solvimm')
s3 = session.resource('s3')

@click.group() # cria grupo
def cli():
    "webtron deploys websites to AWS"
    pass

@cli.command('list-buckets') # adiciona comando dentro do grupo
def list_buckets(): # comando propriamente dito
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bctname') # adiciona argumento
def list_bucket_objects(bctname): #  passa argumento como parametro na função
    "List objects in an s3 bucket"
    for obj in s3.Bucket(bctname).objects.all(): #percorre e printa os arquivos
        print(obj)

if __name__ == '__main__':
    cli()