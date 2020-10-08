# knighthacks-azure-functions-workshop

/cloud/ contains the four Azure Functions that manage Create, Read, Update, and Delete
functionality for your CosmosDB subscription. Please input the correct variables in
/cloud/util/cosmos_connection.py with your unique private keys before testing!

/local/ contains the test_demo.py script that can be executed via command line on your
personal computer, and is not deployed on the cloud. This function *tests* the cloud
functions you are deploying in the /cloud/ folder. Please input the correct cloud
function URLs in /local/test_demo.py before testing!