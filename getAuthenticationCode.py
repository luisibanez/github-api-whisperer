#!/usr/bin/env python
#---------------------------------------------------------------------------
# Copyright 2013 Kitware Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------
#
# This script implements the first step of the Web Application Flow:
#
# http://developer.github.com/v3/oauth/#web-application-flow
#
#---------------------------------------------------------------------------

import requests
import json

jsonFile=open('LocalConfiguration/accountCredentials.json')
accountCredentials=json.load(jsonFile)
jsonFile.close()

clientID=accountCredentials['Client ID']
redirectURI=accountCredentials['Redirect URI']
scopes=accountCredentials['Scopes']
state=accountCredentials['State']

clientIdString='client_id='+clientID

payload={'client_id':clientID,'redirect_uri':redirectURI,'scope':scopes,'state':state}

url='https://github.com/login/oauth/authorize'

r = requests.get(url,data=json.dumps(payload))

print r
print r.status_code

