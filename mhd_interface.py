'''

	Author:  Lasha Zakariashvili
	Details: A MojoHelpDesk Interface for Python


	Example Object passed to createTicket():
	{
		'company_id':
		'custom_fields': {
			'abc':'123'
		},
		'description':
		'priority_id':
		'subject':
		'title': 
		'user_id':
	}


'''

import requests
from lxml import etree

#URL example:  company.mojohelpdesk.com
class MHD():
	def __init__(self, url, apikey):
		self.baseurl = "http://" + url + "/api/"
		self.apikey = apikey 

	def createTicket(self, obj):
		url = self.baseurl + "tickets"

		params = {
			'access_key': self.apikey
		}

		headers = {
			'Accept': 'application/xml',
			'Content-type': 'application/xml',
		}

		ticket = etree.Element('ticket')
		etree.SubElement(ticket, 'title').text = obj['title']
		etree.SubElement(ticket, 'description').text = obj['description']
		etree.SubElement(ticket, 'company_id').text = obj['company_id']
		etree.SubElement(ticket, 'priority_id').text = obj['priority_id']
		if (len(obj['custom_fields']) > 0):
			for field in obj['custom_fields']:
				etree.SubElement(ticket, field).text = obj['custom_fields'][field]
		etree.SubElement(ticket, 'user_id').text = obj['user_id']

		ticket = etree.tostring(ticket)

		print "URL: " + url
		print "Params: " + str(params)
		print "Header: " + str(headers)
		print "Data: " + ticket
		r = requests.post(url, params=params, headers=headers, data=ticket)
		print "URL SENT: " + r.url
		print "----MojoHelpDesk Returned This:-----"
		print r.text

