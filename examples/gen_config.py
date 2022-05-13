from dydx3.constants import SYNTHETIC_ASSET_ID_MAP
from dydx3.constants import ASSET_RESOLUTION

for x in sorted(SYNTHETIC_ASSET_ID_MAP.keys()):
    print('   case ', x, ' extends Currency("', x, '")', sep='')

for x in sorted(ASSET_RESOLUTION.keys()):
    print(x, ' -> ', ASSET_RESOLUTION[x][2:], ',', sep='')

for x in sorted(SYNTHETIC_ASSET_ID_MAP.keys()):
    print(x, '-> BigInt("', format(SYNTHETIC_ASSET_ID_MAP[x], 'x'), '",16),', sep='')
