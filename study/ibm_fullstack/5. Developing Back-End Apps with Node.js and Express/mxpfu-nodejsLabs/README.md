# Node.js

use below command to POST Data using curl
curl --request POST 'localhost:5001/user?firstName=Jon&lastName=Lovato&email=jonlovato@theworld.com&DOB=10/10/1995'

use below command to UPDATE Data using curl
curl --request PUT 'localhost:5001/user/johnsmith@gamil.com?DOB=1/1/1971'

use below command to DELETE Data using curl
curl --request DELETE 'localhost:5001/user/johnsmith@gamil.com'

use below command to Login using curl
curl -X POST -H "Content-Type: application/json" -d '{"user":{"name":"abc","id":1}}' localhost:5001/login
