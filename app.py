from faker import Factory
import csv


class Company:

	def __init__(self,fake):

		self.data = {}
	
		self.data['name'] = fake.company()
		self.data['file_number'] = fake.random_number()
		self.data['jurisdiction'] = fake.lexify(text="????")
		self.data['status'] = fake.word()
		self.data['inactivationDate'] = fake.date()
		self.data['struck_off_date'] = fake.date()
		self.data['registrationData'] = fake.bs()

	def toRow(self):
		fields = self.data.keys()
		row = []
		for f in fields:
			row.append(self.data[f])
		return row

	def getHeader(self):
		return list(self.data.keys())
		


class Officer:

	def __init__(self,fake):

		self.data = {}

		self.data['name'] = fake.name()
		self.data['certificateNumber'] = fake.random_number()
		self.data['numbershares'] = fake.random_number()
		self.data['classofshares'] = fake.word()
		self.data['dateofissue'] = fake.date()
		self.data['ceasedmembership'] = fake.date()
		self.data['transferdata'] = fake.sentence()
		self.data['sharestransferred'] = fake.random_number()
		self.data['newcertificate'] = fake.boolean()
		self.data['custodianname'] = fake.name()
		self.data['custodianaddress'] = fake.address()
		self.data['citizenship'] = fake.country()
		self.data['pep'] = fake.word()
		self.data['rst'] = fake.word()
		self.data['registerlocation'] = fake.country()

	def toRow(self):
		fields = self.data.keys()
		row = []
		for f in fields:
			row.append(self.data[f])
		return row

	def getHeader(self):
		return list(self.data.keys())

class Address:

	def __init__(self,fake):

		self.data = {}

		self.data['name'] = fake.address()

	def toRow(self):
		fields = self.data.keys()
		row = []
		for f in fields:
			row.append(self.data[f])
		return row

	def getHeader(self):
		return list(self.data.keys())


class Client:

	def __init__(self,fake):

		self.data = {}

		self.data['name'] = fake.name()
		self.data['status'] = fake.random_element(elements=("active", "inactive"))
		self.data['client_number'] = fake.random_number()
		self.data['client_name'] = fake.name()
		self.data['prospect_date'] = fake.date()
		self.data['active_since'] = fake.date()
		self.data['country'] = fake.country()
		self.data['city'] = fake.city()
		self.data['former_name'] = fake.name()
		self.data['cross_reference'] = fake.name()
		self.data['activity'] = fake.lexify(text="?????")
		self.data['classification'] = fake.random_element(elements=("HNW", "EWLR", "WKJE"))
		self.data['subclassification'] = fake.file_name()
		self.data['region'] = fake.country_code()
		self.data['compliance_classification'] = fake.lexify("???")

	def toRow(self):
		fields = self.data.keys()
		row = []
		for f in fields:
			row.append(self.data[f])
		return row

	def getHeader(self):
		return list(self.data.keys())

def generate():
	companies = [Company(fake) for i in range(100)]
	officers = [Officer(fake) for i in range(100)]
	addresses = [Address(fake) for i in range(100)]
	clients = [Client(fake) for i in range(100)]

	with open('data/companies.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(companies[0].getHeader())
		for c in companies:
			writer.writerow(c.toRow())

	with open('data/officers.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(officers[0].getHeader())
		for c in officers:
			writer.writerow(c.toRow())

	with open('data/addresses.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(addresses[0].getHeader())
		for c in addresses:
			writer.writerow(c.toRow())

	with open('data/clients.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(clients[0].getHeader())
		for c in clients:
			writer.writerow(c.toRow())



if __name__ == "__main__":
	fake = Factory.create()
	generate()
	


