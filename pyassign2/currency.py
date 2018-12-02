"""currency.py: Currency online

__author__ = 'Sang'
__pkuid__ = '1600017765'
__email__ = 'johnbirdsang@pku.edu.cn'
"""

from urllib.request import urlopen

def get(currency_from, currency_to, amount_from):
    """get the string from the given website.
    """
    parameter = 'from=' + currency_from\
                + '&to=' + currency_to\
                + '&amt=' + str(amount_from)
    urllink = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'\
              + parameter
    doc = urlopen(urllink)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

    
def exchange(currency_from, currency_to, amount_from):
    """operate on the string from function get()
    """
    jstr = get(currency_from, currency_to, amount_from)
    amount_to = jstr.split('"')[7].split(' ')[0]
    error = jstr.split('"')[13]
    return amount_to, error

    
def testget():
    """test the function get()
    """
    assert ('{ "from" : "2.5 United States Dollars", \
"to" : "2.1589225 Euros", "success" : true, "error" : "" }' \
            == get('USD', 'EUR', 2.5)), 'Test 1 of get() failed.'
    assert ('{ "from" : "", "to" : "", "success" : false, \
"error" : "Exchange currency code is invalid." }' \
            == get('USD', 'XXX', 1)), 'Test 2 of get() failed.'

    
def testexc():
    """test the function exchange()
    """
    assert ('6.8521' == exchange('USD', 'CNY', 1)[0]),\
            'Test 1 of exchange() failed.'
    assert ('2.9219186437939' == exchange('JPY', 'VUV', 3)[0]), \
            'Test 2 of exchange() failed.'


def testall():
    """test
    """
    testget()
    testexc()
    print('All tests pass!!')
    

def main():
    """main
    """
    testall()
    
    
if __name__ == '__main__':
    main()
