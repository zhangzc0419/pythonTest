import re



if __name__ == '__main__':
    # if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
    #     print('ok')
    # else:
    #     print('failed')
    #
    # re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    # print re_telephone.match('010-12345').groups()
    # print re_telephone.match('010-8086').groups()
    # if re.match(r'^\w*.*\w*[@]\w*.\w*$', 'bill.gates@microsoft.com'):
    #     print('ok')
    # else:
    #     print('failed')

    if re.match(r'<\w+\s\w+>\s(\w+|\w+\.\w+)@(\w+)\.(com|cn|org)$', '<Tom Paris> tom@voyager.org'):
        print('ok')
    else:
        print('failed')

    m = re.match(r'<(\w+\s\w+)>\s(\w+|\w+\.\w+)@(\w+)\.(com|cn|org)$', '<Tom Paris> tom@voyager.org')
    print m.group(1)
