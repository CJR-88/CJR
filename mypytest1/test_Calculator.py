import yaml
import pytest

def get_datas():
    with open('./datas.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
        return [adddatas, myids]

class TestCalculator:
    def setup_class(self):
        print("开始计算跨境商品利润")

    def teardown_class(self):
        print("跨境商品利润计算结束")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('name,tradtype,price,rebate,sellingprice,rate,netprofit',get_datas()[0],ids=get_datas()[1])
    def test_profit(self,name,tradtype,price,rebate,sellingprice,rate,netprofit):
        if tradtype==0:
            profit=(sellingprice-price)+price*rebate
            profit=round(profit,2)
            assert profit == netprofit
            print(f'{name}商品的利润是{profit}')

        elif tradtype==1:
            profit=(price*rebate+sellingprice-price)/(1+rate)
            profit = round(profit, 2)
            assert profit == netprofit
            print(f'{name}商品的利润是{profit}')

        elif tradtype==2:
            profit=(sellingprice-price)+price*rebate
            profit=round(profit,2)
            assert profit == netprofit
            print(f'{name}商品的利润是{profit}')



