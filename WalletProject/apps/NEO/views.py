import logging
import time
import json
import requests
from django.views.generic import View
from django.http import JsonResponse
from apps.NEO.models import NEOAddress, NEOAddressInfo
from django.db import transaction
from utils.connect_neo_cli import connect_neo


logger = logging.getLogger("WalletProject")


# /other/getaddress?count=value
class ReturnOtherAddressView(View):
    """返回其他类型币种的地址"""

    def get(self, request):
        # 接受参数
        address_count = request.GET.get('count')

        # 判断参数
        if address_count is None:
            return JsonResponse({'status': 0, 'detail': 'parameter error'})

        # 业务处理
        address_list = []
        address_count = int(address_count)
        # 设置事务保存点
        save_id = transaction.savepoint()
        try:
            for i in range(address_count):
                address = NEOAddress.objects.filter(IsUse=False).order_by('id').first()
                address.IsUse = True
                address.save()
                address_list.append(address.Myaddress)
        except Exception as e:
            return JsonResponse({'status': 0, 'detail': 'handle failure'})

        # 提交事务
        transaction.savepoint_commit(save_id)

        # 返回值
        return JsonResponse({'status': 1, 'detail': 'success', 'address': address_list})


# /other/createaddress?number=value
class CreateAddressView(View):
    """创建币种地址"""

    def get(self, request):
        # 获取参数
        coin_type = request.GET.get('type')
        number = request.GET.get('number')

        # 校验参数
        if not all([coin_type, number]):
            return JsonResponse({'status': 0, 'detail': 'parameter error'})

        try:
            number = int(number)
        except Exception as e:
            return JsonResponse({'status': 0, 'detail': 'number non-integer'})

        # 业务处理
        # 连接币种客户端，创建地址
        data = {
            "jsonrpc": "2.0",
            "method": "getnewaddress",
            "params": [],
            "id": 1
        }
        try:
            for i in range(number):
                headers = {'Content-Type': 'application/json'}
                url = "http://127.0.0.1:10332"
                time.sleep(1)
                response_json = requests.post(url=url, headers=headers, data=json.dumps(data))

                req_dict = json.loads(response_json.content.decode('utf-8'))

                result = req_dict['result']
                NEOAddress.objects.get_or_create(
                    CoinCode=coin_type,
                    Myaddress=result,
                )
        except Exception as e:
            return JsonResponse({'status': 0, 'detail': 'create address failure'})

        # 返回值
        return JsonResponse({'status': 1, 'detail': 'create address success'})


class RechargeView(View):
    """充值"""

    def post(self, request):
        """充值"""
        # 接受参数
        response_str = connect_neo(request)
        response_dict = json.loads(response_str)

        tx_id = response_dict["result"]["txid"]  # 交易id
        vouts= response_dict["result"]["vout"]  # 装出列表

        # 校验参数
        if not all([tx_id, vouts]):
            return JsonResponse({'status': 0, 'detail': 'parameter error'})

        # 业务处理
        for vout in vouts:
            asset = response_dict["result"]["vout"]["asset"]  # 资产类型
            value = response_dict["result"]["vout"]["value"]  # 充值金额
            address = response_dict["result"]["vout"]["address"]  # 充值地址

            try:
                neo = NEOAddress.objects.get(address=address)

                if neo:
                    # 是我们生成的地址，需要添加进地址信息表
                    NEOAddressInfo.objects.get_or_create(asset=asset, tx_id=tx_id, address=address, category = "receive", amount = value)
            except:
                pass

        return JsonResponse({'status': 1, 'detail': '充值成功'})






        # 返回值