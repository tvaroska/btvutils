from btvutils.google import BucketPrefix, make_gs

def test_strings():
    response = make_gs('bucket')
    assert response == 'gs://bucket'

    response = make_gs('bucket', 'prefix/another')
    assert response == 'gs://bucket/prefix/another'

    response = make_gs('bucket', '/prefix/another')
    assert response == 'gs://bucket/prefix/another'

def test_tuple():
    response = make_gs(bucketprefix=BucketPrefix('bucket', 'prefix'))
    assert response == 'gs://bucket/prefix'
