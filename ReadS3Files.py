import boto3
from boto3.session import Session

from flask import *

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to S3 Demo Project!'

@app.route("/list",methods = ['GET'])
def listFilesInS3Bucket():
    s3 = boto3.resource('s3')

    #my_bucket = s3.Bucket('1834-testbucket')

    #for file in my_bucket.objects.all():
        #print(file.key)
        
    keys=[]

    prefix=request.args.get('prefix')

    your_bucket = s3.Bucket('1834-testbucket')
   
    if prefix:

        for s3_file in your_bucket.objects.filter(Prefix=prefix+'/'):
        
            keys.append(s3_file.key)
    
        if len(keys)==0:

            return "No Objects found with the key "+prefix
    
    else:

        return "No prefix provided! Kindly provide a prefix"

    #response = s3.list_objects(Bucket=your_bucket, MaxKeys=1)    
   
    return jsonify(keys)


if __name__ == '__main__':
    app.run(debug=True)

