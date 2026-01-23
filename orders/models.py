from django.db import models
class OrderStatus(models.model):
    name= models.CharFeild(max_length=50,unique=True)

    def__str__(self)
      return self.name
    
    class Order(model.Model):
        customer_name = models.CharFeild(max_length=100)
        created_at = models.DateTimeFeild(auto_now_add=True)

    status= models.ForeignKey(
        Orderstatus,
        on_delete=models.SET_NULL,
        blank=True
    )
    def def__str__(self):
        return f"Order #{self.id}"
 from django.db import models
  class OrderStatus(models.Model):
    name = models.charField(max_length=50, unique=True)

    def __str __(self):
        return self.name
    
    from django.db import models
    class Coupon(models.MOdel):
        code = models. CharField(max_length=50, unique=True)
        discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
        is_active = models.BooleanField(default=True)
        valid_from = models. DateField()
        valid_until = models.DateField()

        def __str __(self):
            return self.code
