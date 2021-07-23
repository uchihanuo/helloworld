ad = \
    {
        'Wangxian': '52253@any3.com',
        'Gannengqiang': '41996@any3.com',
        'Lanjianhua': '48765@any3.com',
        'Zhongling': '60000@any.com',
        'Yangnuo': '50855@any3.com'
    }
print("Lanjianhua's address is", ad['Lanjianhua'])

del ad['Yangnuo']
print('\nThere are {} contacts in the address-book.'.format(len(ad)))

for name, address in ad.items():
    print('Contact {} at {}'.format(name, address))

ad['Youhongyi'] = '52356@any3.com'

if 'Youhongyi' in ad:
    print("\nYouhongyi's address is", ad['Youhongyi'])
