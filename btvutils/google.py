from typing import NamedTuple

BucketPrefix = NamedTuple('BucketPrefix', [('bucket', str), ('prefix', str)])

def split_gs(uri:str) -> BucketPrefix:

    splits = uri.split('/')

    bucket = splits[2]
    prefix = '/'.join(splits[3:])

    return BucketPrefix(bucket, prefix)

def make_gs(bucket:str = None, prefix:str = None, bucketprefix:BucketPrefix = None) -> str:
    if bucket:
        l_bucket = bucket
        if prefix:
            if prefix[0] == '/':
                l_prefix = prefix[1:]
            else:
                l_prefix = prefix
        else:
            l_prefix = None
    else:
        l_bucket = bucketprefix.bucket
        l_prefix = bucketprefix.prefix

    if l_prefix:
        return f'gs://{l_bucket}/{l_prefix}'
    else:
        return f'gs://{l_bucket}'        