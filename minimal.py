from eve import Eve
from file_store import ufile
from ucloud.ufile import baseufile
from flask import jsonify, request
from pprint import pprint
from flask_cors import cross_origin

public_key = ''  # 添加自己的账户公钥
private_key = ''  # 添加自己的账户私钥

if public_key == '' or private_key == '':
    try:
        from key import public_key, private_key
    except EnvironmentError:
        pass

app = Eve()
app.register_resource('ufile', ufile)


@app.route('/getauth', methods=['GET', 'POST'])
@cross_origin()
def getauth():
    print(request.method)
    if request.method != 'POST':
        return jsonify({
            'msg': 'methods need post!'
        })

    method = request.json.get('method')
    bucket = request.json.get('bucket')
    key = request.json.get('key')
    header = request.json.get('header')
    mime_type = request.json.get('mime_type')

    auth = baseufile.BaseUFile(public_key, private_key)
    auth_key = auth.authorization(method, bucket, key, header, mime_type)
    return jsonify({
        'key': auth_key
    })


if __name__ == '__main__':
    app.run(debug=True)
