class Product:

    # class 초기화 w/ 품목번호, 품명, 가격, 재고수량
    def __init__(self, num, name, price, quantity):
        self.num = num
        self.name = name
        self.price = price
        self.quantity = quantity

    # 수량(self.quantity)을 변경하는 메소드: 매개변수로 받은 quantity 만큼 감소

    def set_quantity(self, quantity):
        self.quantity -= quantity

    # class 정보를 출력하는 메소드 / print()로 클래스 객체 출력시 호출
    def __str__(self):
        return f'{self.num}: {self.name} - {self.price}원  ({self.quantity}개)'


class Changes:
    
    # class 초기화 w/ 품목번호, 품명, 가격, 재고수량
    def __init__(self, chg):
        self.chg_total = chg
        self.dims = [[50000, 0],[10000, 0], [5000,0], [1000,0], [500,0],[50,0],[10,0],[1,0]]

     def print_chg_dims(self):
        chgs = self.chg_total
        i = 0
        msg = ""
        if chgs == 0:
            print("[INFO] 지급할 거스름돈이 없습니다.")
        else:
            for dim in self.dims:
                i = chgs // dim[0]
                if i != 0:
                    dim[1] = i
                    chgs -= dim[0] * i
                    msg += f"{dim[0]}원 * {i}개, "
                else:
                    continue
            
            msg = msg[:-2:1]
            print("[INFO]  " + msg + "로 지급합니다.")
        print('-'*50)

            


class Vending_Machine():

    # 생성할 때, 판매 품목, 수량 등을 입력으로 전달 받음
    # 메뉴/재고 출력
    # 금액 입력
    # 주문 입력 => 주문 내역을 basket에 담아서 리턴
    # 투입한 금액 이내 / 재고가 있는 경우에만 basket에 주문 내역 포함
    # 주문처리 => basket에 담긴 주문을 처리하고(재고 반영), 총 비용 계산
    # 주문 내역을 출력 / 주문 내역 확인 (y/n)
    # 주문취소 => basket의 내용을 참조해서 재고 원복
    # 주문확인 => basket을 활용하여 각 품목별 sub_total / 총금액 / 거스름돈 계산 및 영수증 출력
    # 거스름돈을 지불한 지폐 개수 출력

    def __init__(self, products):
        self.products = products
        self.minimum_cash = 800

    def __str__(self):
        pass

    def order_initialize(self):
        self.basket = []
        self.grand_total = 0
        self.sub_total = 0
        self.chgs = 0
        self.inserted_cashs = 0

        print()
        print()
        print("***** 판매 상품 목록 *****")

        for product in products:
            print(product)

    def run(self):
        self.order_initialize()

    def product_minimum_price(self, products):
        product_prices = []

        for product in products:
            if product.quantity > 0:
                product_prices.append(product.price)

        if len(product_prices) == 0:
            minimum_price = 0
        else:
            minimum_price = min(product_prices)

        return minimum_price

    def insert_cash(self):
        print()
        self.inserted_cashs = int(input("지불할 비용을 입력해 주세요: "))
        while self.inserted_cashs < self.product_minimum_price(self.products):
            self.inserted_cashs = int(
                input(f"{self.product_minimum_price(self.products)}원 이상 입력해 주세요: "))
        print(f"{self.inserted_cashs}원을 입력하셨습니다.")

    def order_product(self):

        loop_break_flag = False

        while True:

            if loop_break_flag == True:
                break

            while True:
                
                print()
                product_code = int(input("주문할 상품 번호를 입력해 주세요 (주문완료: 0): "))

                if product_code < 0 or product_code > len(self.products):
                    print("존재하지 않는 상품번호 입니다.")
                    break

                if product_code == 0:
                    loop_break_flag = True
                    break

                product_qty = int(input("주문할 상품 수량을 입력해 주세요 (주문완료: 0): "))

                if product_qty > self.find_product_with_num(product_code).quantity:
                    print("주문한 상품의 재고 수량이 부족합니다.")
                    break

                if product_qty == 0:
                    loop_break_flag = True
                    break

                self.sub_total = self.find_product_with_num(
                    product_code).price * product_qty
                self.grand_total += self.sub_total

                if self.grand_total > self.inserted_cashs:
                    print(self.inserted_cashs)
                    print("지불한 비용을 초과하였습니다. 다시 주문해 주세요")
                    self.grand_total -= self.sub_total
                    self.sub_total = 0
                    break

                self.find_product_with_num(
                    product_code).quantity -= product_qty

                self.basket.append({'name': self.find_product_with_num(product_code).name, 'price': self.find_product_with_num(
                    product_code).price, 'quantity': product_qty, 'sub_total': self.find_product_with_num(product_code).price * product_qty})

                print()
                print(
                    f"{self.find_product_with_num(product_code).name} * {product_qty} = {self.sub_total}원 장바구니에 추가되었습니다.")

        self.chgs = self.inserted_cashs - self.grand_total
        # print(self.basket)
        # print(self.chgs)

    def find_product_with_num(self, num):
        for product in self.products:
            if product.num == num:
                result = product
            else:
                continue
        return result

    def print_receipt(self):
        print()
        print()
        print("*** <주문 내역 및 영수증> ***")
        i = 1
        for basket_item in self.basket:
            print(
                f"({i}) " + f"{basket_item['name']}:   {basket_item['price']} * {basket_item['quantity']} = {basket_item['sub_total']}원")
            i += 1

        print('-'*50)
        print(f"주문 총액: {self.grand_total}원")
        print(
            f"거스름돈 ({self.chgs}원) = 지불금액({self.inserted_cashs}원) - 주문총액({self.grand_total}원)")
        # print('-'*50)


# main 함수 선언
if __name__ == "__main__":
    # 판매제품을 저장하기 위한 빈 리스트를 생성하고, Product 클래스를 사용하여 판매 제품 객체를 생성하고 products 리스트에 추가
    products = []
    products.append(Product(1, '콜라', 1000, 10))
    products.append(Product(2, '사이다', 900, 10))
    products.append(Product(3, '환타', 800, 10))

    vending_machine_on = True
 
    obj = Vending_Machine(products)
    
    while vending_machine_on:
        print()
        print()
        prompt = input("주문을 계속하시겠습니까? (아무키나 클릭하세요 / exit: 프로그램 종료) : ")

        if prompt == 'exit':
            vending_machine_on = False
        else:
            obj.run()
            obj.insert_cash()
            obj.order_product()
            obj.print_receipt()
            obj_chg = Changes(obj.chgs)
            obj_chg.print_chg_dims()
            obj.order_initialize()
            del obj_chg

        










