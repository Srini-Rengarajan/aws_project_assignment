import boto3
from boto3.session import Session

from flask import *

app = Flask(__name__)


@app.route("/list",methods = ['GET'])
def listFilesInS3Bucket():
    s3 = boto3.resource('s3')

    #my_bucket = s3.Bucket('1834-testbucket')

    #for file in my_bucket.objects.all():
        #print(file.key)
        
    ky=""
    prefix=request.args.get('prefix')

    your_bucket = s3.Bucket('1834-testbucket')
    
    for s3_file in your_bucket.objects.filter(Prefix=prefix+'/'):
        ky=s3_file.key
        
    #response = s3.list_objects(Bucket=your_bucket, MaxKeys=1)    
   
    return ky


if __name__ == '__main__':
    app.run(debug=True)

