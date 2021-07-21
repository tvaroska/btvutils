from btvutils.google import split_gs

def test_full():
    response = split_gs('gs://bucket/prefix')

    assert response.bucket == 'bucket'
    assert response.prefix == 'prefix'

    response = split_gs('gs://bucket/prefix/onemore')

    assert response.bucket == 'bucket'
    assert response.prefix == 'prefix/onemore'


def test_bucket():

    response = split_gs('gs://bucket')

    assert response.bucket == 'bucket'
    assert response.prefix == ''

    response = split_gs('gs://bucket/')

    assert response.bucket == 'bucket'
    assert response.prefix == ''


