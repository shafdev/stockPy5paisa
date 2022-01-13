from py5paisa import FivePaisaClient

#get these cred from 5 paisa site
cred={
    "APP_NAME":"5P59739795",
    "APP_SOURCE":"7664",
    "USER_ID":"oBXx0tNQ",
    "PASSWORD":"RHLIRDxN",
    "USER_KEY":"dhGVcNwjbjM0YZzpIbU3Ue5UW",
    "ENCRYPTION_KEY":"vJMuM77ZuKNiAEOTCJJE5v3D"
    }
client = FivePaisaClient(email="email_here", passwd="password_here", dob="dateOfBirth_here",cred=cred)
client.login()