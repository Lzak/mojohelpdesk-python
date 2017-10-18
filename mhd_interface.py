'''

	Author:  Lasha Zakariashvili
	Details: A MojoHelpDesk Interface for Python


	Example Object:
	{
		'location': 
		'subject':
		'description':
		'tixType':
	}


'''

import requests

def createTicket(obj):

	headers = {
		'Accept': 'application/xml',
		'Content-type': 'application/xml',
	}

	data = "<ticket><title>" + obj['location'] + " - " + obj['subject'] + "</title>" + \
			"<description>"  + obj['description'] + "</description>" + \
			"<company_id>"   + obj['company_id'] + "</company_id>" + \
			"<priority_id>"  + obj['priority'] + "</priority_id>" + \
			"<user_id>" 	 + obj['user_id'] + "</user_id></ticket>"

	r = requests.post(url_ticket, headers=headers, data=data)
	print "MojoHelpDesk Returned This:"
	print r.text
