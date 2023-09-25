import toml

with open('./alacritty.toml', 'r') as f:
    config = toml.load(f)
    print(config['env']['TERM'])


#
# with open('./prueba.toml', 'r') as f:
#     config = toml.load(f)
#     print(config['server']['host'])
