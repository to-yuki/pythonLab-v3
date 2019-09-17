# データ構造の定義
birthday = {
    'Yamada' : [1931, 'September', 13],
    'Tanaka': [1984, 'July', 10],
    'Suzuki': [1968, 'May', 31]
}

# 山田さんの誕生年を取得
yamada_year = birthday['Yamada'][0]
print('Yamada-san was born in {0}.'.format(yamada_year))

# 田中さんの誕生月を取得
tanaka_month = birthday['Tanaka'][1]
print('In what month was Tanaka-san born?  In {0}.'.format(tanaka_month)) 

# 鈴木さんの誕生年、月、日をそれぞれ取得 
suzuki_year = birthday['Suzuki'][0]
suzuki_month = birthday['Suzuki'][1]
suzuki_day = birthday['Suzuki'][2]
print('Suzuki-san was born on {2}/{1}/{0}.'.format(suzuki_year, suzuki_month, suzuki_day))