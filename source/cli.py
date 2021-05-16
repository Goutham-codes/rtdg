# import statements
from rtdg import all_func
import argparse
import sys
import csv


def checkinputs(fields,total,filename):
	# check for errors
	if fields<=0 or fields>10:
		raise ValueError("argument 'fields' must be in the range 1 to 10")
	if total<=0 or total>100:
		raise ValueError("argument 'total' must be in the range 1 to 100")
	namecheck = filename.split('/')[-1].split('.')
	if not (len(namecheck)==2 and namecheck[1]=="csv" and namecheck[0].isalnum()):
		raise ValueError("argument 'filename' must be a valid csv file name")
	return True

def printdetail():
	# print additional details
	print('{:<20}'.format('domain'),end="")
	print('subdomain')
	print()
	for domain in all_func:
		print('{:<20}'.format(domain),end="")
		print(*all_func[domain],sep=", ")

def writedata(filename,total,fieldnames,functions):
	# write randomly generated data to the file
	try:
		with open(filename,'w',newline='') as file:
			writer = csv.writer(file)
			# write the columns to csv file
			writer.writerow(fieldnames)
			for idx in range(total):
				data = []
				for func in functions:
					val = func()
					data.append(val)
				# write data to csv file
				writer.writerow(data)
		return True
	except:
		return False

def main(args):
	fields=args.fields
	total = args.total
	filename=args.filename
	functions = []
	fieldnames = []

	if not checkinputs(fields,total,filename):
		sys.exit()
	
	if args.verbose:
		printdetail()

	# get user input
	while len(fieldnames)<fields:
		print(f'Enter field {len(fieldnames)+1}')
		domain = input("Enter a domain: ")
		if domain in all_func:
			subdomain = input("Enter a subdomain: ")
			if subdomain in all_func[domain]:
				functions.append(all_func[domain][subdomain])
				fieldnames.append(subdomain)
			else:
				print("Invalid Subdomain!")
		else:
			print("Invalid Domain!")
		if input("Enter y to continue: ").lower()=="y":
			continue
		else:
			sys.exit()

	if writedata(filename,total,fieldnames,functions):
		print("Data has been written to the file successfully!")
	else:
		print('Error writing data to the file')


if __name__=='__main__':
	parser = argparse.ArgumentParser(prog='rtdg', description='test data generation')
	parser.add_argument('fields', type=int,  help='total number of fields')
	parser.add_argument('total', type=int, help='total number of data')
	parser.add_argument('filename', help='path of file (Note: only csv files)')
	parser.add_argument("-v", "--verbose", help="increase output verbosity")
	args = parser.parse_args()
	main(args)