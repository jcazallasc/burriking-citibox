from typing import List, Optional

from orders.domain.entities.order_entity import OrderEntity
from orders.domain.entities.product_option_entity import ProductOptionEntity
from orders.domain.entities.subproduct_entity import SubproductEntity


class CombineChecker:

    def __init__(self, combine: dict, order: OrderEntity, *args, **kwargs) -> None:
        self.combine = combine
        self.order = order

    def __check_product_id(self, quantity: int, product_id: Optional[str], *args, **kwargs) -> bool:
        if not product_id:
            return True

        _total_occurs = 0
        for _lines in self.order.lines:
            if _lines.product_id == product_id:
                _total_occurs += 1

        return _total_occurs >= quantity

    def __check_product_option_id(self, quantity: int, product_option_id: Optional[str], *args, **kwargs) -> bool:
        if not product_option_id:
            return True

        _total_occurs = 0
        for _line in self.order.lines:
            _total_occurs += self.__count_in_product_option(_line.product_options, product_option_id)
            _total_occurs += self.__count_in_subproducts(_line.subproducts, product_option_id)

        return _total_occurs >= quantity

    def __count_in_product_option(self, product_options: List[ProductOptionEntity], product_option_id: str) -> int:
        _count = 0

        for _product_option in product_options:
            if _product_option.id == product_option_id:
                _count += 1

        return _count

    def __count_in_subproducts(self, subproducts: List[SubproductEntity], product_option_id: str) -> int:
        _count = 0

        for _subproduct in subproducts:
            for _subproduct_option in _subproduct.subproduct_options:
                if _subproduct_option["id"] == product_option_id:
                    _count += 1

        return _count

    def check(self) -> bool:
        for _combo in self.combine:
            _quantity = _combo["quantity"]
            _product_id = _combo.get("product_id")
            _product_option_id = _combo.get("product_option_id")

            if _product_id and not self.__check_product_id(_quantity, _product_id):
                return False

            if _product_option_id and not self.__check_product_option_id(_quantity, _product_option_id):
                return False

        return True
