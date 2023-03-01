import sys

def show_package_and_modeule_stats():
    print('rpc', sys.modules.get('rpc'))
    print('rpc.product', sys.modules.get('rpc.product'))



def function_a():
    print('执行function_a')

def function_b():
    from rpc.product import get_products
    
    print(get_products())
    print('执行function_b')


print('没有导入rpc.product')
show_package_and_modeule_stats()
function_a()


print('导入rpc.product模块')
show_package_and_modeule_stats()
function_b()
show_package_and_modeule_stats()

