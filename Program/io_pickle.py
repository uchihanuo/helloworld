import pickle


shoplistfile = 'shoplist.data'
shoplist = ['Switch ns', 'Xbox one X', 'RX570']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f =open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
