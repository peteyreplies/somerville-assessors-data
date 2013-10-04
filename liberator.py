#built using the https://views.scraperwiki.com/run/python_mechanize_cheat_sheet/

import mechanize

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

response = br.open('http://data.visionappraisal.com/SomervilleMA/main.asp')
#print response.read()      # the text of the page

#for form in br.forms():
#    print "Form name:", form.name
#    print form

br.select_form("SearchByLocation") # works when form has a name
br.form[ 'StreetNum' ] = '31'
br.form[ 'StreetName'] = 'aberdeen rd'

# Get the search results
results = br.submit()
print results.read()


