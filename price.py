# shopping() 함수

def shopping(shop_file):
  
  with open("./data/" + shop_file , mode = 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    shop_dict = {}
    for line in lines:
      xx = line.strip()
      if xx == '':
        continue
      name, cost = xx.split()
      if  cost != 'A' and cost != 'B':
        shop_dict[name] = cost  
  
  R_shop = shop_dict.values()
  D = str(R_shop).replace('원', '')
  D = D.replace('dict_values', '')
  D = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', D)
  D = D.split()
  
  return dict(zip(shop_dict.keys(), D))
      
# item_price() 함수

def item_price(shop_file, item):
    
  with open("./data/" + shop_file , mode = 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    shop_dict = {}
    for line in lines:
      xx = line.strip()
      if xx == '':
        continue
      name, cost = xx.split()
      if cost != 'A':
        shop_dict[name] = cost 

  R_shop = shop_dict.values()
  D = str(R_shop).replace('원', '')
  D = D.replace('dict_values', '')
  D = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',D)
  D = D.split()
  return dict(zip(shop_dict.keys(), D))[item], '원'

"init"
