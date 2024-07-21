input = input("Enter file name: ")
fileHandle = open(input)
counts = dict()
domainList = list()
length = 0
# This for cycle iterates through the file and finds all the lines that starts with "From", splits the line
# by " " to determine the e-mail address, splits email address by "@" to find the domain, puts all the
# domains in a list and determines the length on the longest domain to know how far to justify all domains
# when printing the result. 
for line in fileHandle:
    if line.startswith("From"):
        email = line.split(" ")
        domain = email[1].split("@")
        domainList.append(domain[1].strip())
        if len(domain[1].strip()) > length:
            length = len(domain[1].strip())
# This 'for' cycle counts how many times each domain name pops up
for domain in domainList:
    if domain not in counts:
        counts[domain] = 1
    else:
        counts[domain] = counts[domain] + 1
print(counts)
print("")
print("SORTED:")
for count in counts:
    histogram = "*" * counts[count]
    print(count.rjust(length), ": ", str(counts[count]).ljust(2), " " + histogram)