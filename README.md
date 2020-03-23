# Introduction

This package is to provide aliyun oss policy and sign from the backend
to clients such as Android, iOS devices and specially mini programs 
on Weixin. 

Many examples and demos even on the official page put access key
and secrets directly in the clients, which can be very dangerous 
since all the code are actually not encrypted. 

This package obtain policy and its encrypted sign  in the backend, 
which is then passed by a request 

# Requirements

The package is based on django restframework, so both django and 
django rest framework should be installed. 

If not, you can import from 'oss_poly_sign.generators' to generate
the policy code and auth. 


# How to Use

1. Step 1: `pip install oss-policy-sign`
2. Added the following settings in your settings.py:
```
OSS_ACCESS_KEY = ""
OSS_ACCESS_SECRET = ""
OSS_TIMEOUT = 60 # 60 minutes, an hour
OSS_MAXSIZE = 10 # 10M
```
3. Added the following to your urls.py:
```
  from oss_policy_sign.views import OssAuthViewSet
  urlpatterns = [
        #  ...
        url(r'^oss/auth/', OssAuthViewSet),
    ]
```

4. test it by making a request
