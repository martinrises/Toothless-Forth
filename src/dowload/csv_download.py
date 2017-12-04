import urllib.request

data_indices = ['002302.XSHE', '000012.XSHE', '603688.XSHG', '002271.XSHE', '000786.XSHE', '603663.XSHG', '000877.XSHE', '600678.XSHG', '002457.XSHE', '603385.XSHG', '600553.XSHG', '300715.XSHE', '300344.XSHE', '000023.XSHE', '300080.XSHE', '000935.XSHE', '300093.XSHE', '000885.XSHE', '600876.XSHG', '000672.XSHE', '002088.XSHE', '603616.XSHG', '002162.XSHE', '300554.XSHE', '000511.XSHE', '300179.XSHE', '000795.XSHE', '002080.XSHE', '600539.XSHG', '600585.XSHG', '603838.XSHG', '002297.XSHE', '600668.XSHG', '600449.XSHG', '300196.XSHE', '603826.XSHG', '002392.XSHE', '600145.XSHG', '603268.XSHG', '600586.XSHG', '000827.XSHE', '300690.XSHE', '002066.XSHE', '002233.XSHE', '002785.XSHE', '603578.XSHG', '603021.XSHG', '300160.XSHE', '300234.XSHE', '000546.XSHE', '603612.XSHG', '002571.XSHE', '600516.XSHG', '600172.XSHG', '600720.XSHG', '300374.XSHE', '600819.XSHG', '300409.XSHE', '600293.XSHG', '600660.XSHG', '601636.XSHG', '600176.XSHG', '600801.XSHG', '601992.XSHG', '600425.XSHG', '603601.XSHG', '002596.XSHE', '000789.XSHE', '600286.XSHG', '002623.XSHE', '300606.XSHE', '000401.XSHE', '002225.XSHE', '600802.XSHG', '600529.XSHG', '300089.XSHE', '002671.XSHE', '300224.XSHE', '300700.XSHE', '601012.XSHG', '002205.XSHE', '600883.XSHG', '300395.XSHE', '300064.XSHE', '002742.XSHE', '600881.XSHG', '300073.XSHE', '002201.XSHE']


def save_csv(filename, content_str):
    with open('../../data/origin/{}.csv'.format(filename), 'w', newline='') as f:
        f.write(content_str)


for index in data_indices:

    headers = {
        'Host':r'www.ricequant.com',
        'Connection': r'keep-alive',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': 1,
        'Referer': r'https://www.ricequant.com/research/user/user_306589/edit/data/toothless_forth/{}_daily_price.csv'.format(index),
        'Accept-Encoding': r'gzip, deflate, br',
        'Accept-Language': r'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
        'Cookie': r'jupyter-hub-token-user_306589="2|1:0|10:1512394613|29:jupyter-hub-token-user_306589|44:OWUzZjcxNmM5MGQ3NDViZWJlZmYyNDQyNjlmYjUxNWQ=|1d756dba5989ee79de1cf0761afd6673d3511f0acbce0bc32159390607eb964b"; gr_user_id=4bbc8223-2791-4fb8-9e46-763c9811ebf9; Hm_lvt_000da5d64c4979d5cb3c97442284b724=1490540886; jupyter-hub-token-user_306589="2|1:0|10:1511704093|29:jupyter-hub-token-user_306589|44:OWUzZjcxNmM5MGQ3NDViZWJlZmYyNDQyNjlmYjUxNWQ=|246f8bb1b2bfba49ad5048d14c078b84139429c95af2399bd183831fc231fbbe"; jupyter-hub-token="2|1:0|10:1511704093|17:jupyter-hub-token|44:OWUzZjcxNmM5MGQ3NDViZWJlZmYyNDQyNjlmYjUxNWQ=|f1bd820f09576efbb0bc50a30f72f611d0202735e7463c59dc215fdf74fdc984"; tgw_l7_route=d0bf4a9ab78d53762b596c0a48da8e7f; sid=cec1e6df-184c-4464-b9d7-f43eb0135792|981565d3af245452ba8af65c380f4a9254e0346c44660840eb0c68dae37c681dccf555fbdd7683beefef7243b6a5733fa5e65e0eba8cba8d1a1951d9e8a5a41e; Hm_lvt_cb81fd54150b99e25d085d58bbaf4a07=1511263137,1511703982,1512394596; Hm_lpvt_cb81fd54150b99e25d085d58bbaf4a07=1512397512; gr_session_id_9bc6807c25b59135=b425d2ac-b48b-498d-8fad-e858a35e0701; gr_cs1_b425d2ac-b48b-498d-8fad-e858a35e0701=user_id%3A306589'
    }
    url = 'https://www.ricequant.com/research/user/user_306589/tree/data/toothless_forth/{}_daily_price.csv?download=1'.format(index)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_str = response.read().decode('gbk', 'ignore')
        print(response_str)
        save_csv(index, response_str)