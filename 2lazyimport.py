import rpc
import sys


def show_package_and_modeule_stats():
    print('rpc', sys.modules.get('rpc'))
    print('rpc.product', sys.modules.get('rpc.product'))

print('触发模块导入前')
show_package_and_modeule_stats()

print(rpc.product.get_products())
print('触发模块导入后')
show_package_and_modeule_stats()
