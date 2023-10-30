# Patterns
[Python_k_vershinam_masterstva_2_e_izd.pdf:p.337]

## Strategy - p.337
### Strategy based on classes
```python

from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


class Order(NamedTuple): # контекст
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None
    
    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


class Promotion(ABC): # Стратегия: абстрактный базовый класс
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Вернуть скидку в виде положительной суммы в долларах"""


class FidelityPromo(Promotion): # первая конкретная стратегия
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    
    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)


class BulkItemPromo(Promotion): # вторая конкретная стратегия
    """10%-ная скидка для каждой позиции LineItem, в которой заказано не менее 20 единиц"""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
            return discount


class LargeOrderPromo(Promotion): # третья конкретная стратегия
    """7%-ная скидка для заказов, включающих не менее 10 различных позиций"""
    
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)
```

```python
>>> joe = Customer('John Doe', 0) 
>>> ann = Customer('Ann Smith', 1100)
>>> cart = (LineItem('banana', 4, Decimal('.5')), 
...
LineItem('apple', 10, Decimal('1.5')),
...
LineItem('watermelon', 5, Decimal(5)))
>>> Order(joe, cart, FidelityPromo()) 
<Order total: 42.00 due: 42.00>
>>> Order(ann, cart, FidelityPromo()) 
<Order total: 42.00 due: 39.90>
>>> banana_cart = (LineItem('banana', 30, Decimal('.5')), 
...
LineItem('apple', 10, Decimal('1.5')))
>>> Order(joe, banana_cart, BulkItemPromo()) 
<Order total: 30.00 due: 28.50>
>>> long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) 
...
for sku in range(10))
>>> Order(joe, long_cart, LargeOrderPromo()) 
<Order total: 10.00 due: 9.30>
>>> Order(joe, cart, LargeOrderPromo())
<Order total: 42.00 due: 42.00>
```




### Strategy based on functions
```python

from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import NamedTuple, Optional, Callable

class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


@dataclass(frozen=True)
class Order(NamedTuple): # контекст
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None
    
    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'



def fidelity_promo(order: Order) -> Decimal:
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    rate = Decimal('0.05')
    if order.customer.fidelity >= 1000:
        return order.total() * rate
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    """10%-ная скидка для каждой позиции LineItem, в которой заказано не менее 20 единиц"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
        return discount


def large_order_promo(order: Order) -> Decimal:
    """7%-ная скидка для заказов, включающих не менее 10 различных позиций"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
```

```python

>>> joe = Customer('John Doe', 0) 
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, Decimal('.5')),
... LineItem('apple', 10, Decimal('1.5')),
... LineItem('watermelon', 5, Decimal(5))]
>>> Order(joe, cart, fidelity_promo) 
<Order total: 42.00 due: 42.00>
>>> Order(ann, cart, fidelity_promo)
<Order total: 42.00 due: 39.90>
>>> banana_cart = [LineItem('banana', 30, Decimal('.5')),
... LineItem('apple', 10, Decimal('1.5'))]
>>> Order(joe, banana_cart, bulk_item_promo) 
<Order total: 30.00 due: 28.50>
>>> long_cart = [LineItem(str(item_code), 1, Decimal(1))
... for item_code in range(10)]
>>> Order(joe, long_cart, large_order_promo)
<Order total: 10.00 due: 9.30>
>>> Order(joe, cart, large_order_promo)
<Order total: 42.00 due: 42.00>
```


## Command - p.344



















