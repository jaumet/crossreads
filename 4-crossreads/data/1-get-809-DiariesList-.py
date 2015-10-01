import urllib2

for n in range(0,8):
    url = 'http://transcripts.sl.nsw.gov.au/api/entity_node/?fields=nid,title,url,percentage_unlocked,record_number&parameters[collection]=4&parameters[type]=transcipt_document&page={:d}&pagesize=500&sort=percentage_unlocked&direction=ASC'.format(n)
    #print url
    response = urllib2.urlopen(url)
    html = response.read()
    print html
    print "######################################"
