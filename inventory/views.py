from django.shortcuts import render
from .models import Inventory
from .forms import OrderForm

def process_order(request):
    # Get the inventory record
    inventory, created = Inventory.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # here we can order customer input
            legs_required = form.cleaned_data['legs']
            wings_required = form.cleaned_data['wings']
            flesh_required = form.cleaned_data['flesh']

            # Calculate the number of chickens needed
            chickens_needed = max(
                (legs_required + 1) // 2,  # each chicken has 2 legs
                (wings_required + 1) // 2,  # each chicken has 2 wings
                flesh_required  # each chicken has 1 flesh portion
            )

            print(chickens_needed)

            # Weight constants
            leg_weight = 0.25  # kg per leg
            wing_weight = 0.25  # kg per wing
            flesh_weight = 1.00  # kg per flesh portion
            chicken_weight = 2.00  # kg per whole chicken

            # Check if there are enough chickens in inventory
            if chickens_needed > inventory.chickens:
                message = "Order cannot be fulfilled. Not enough chickens in inventory."
            else:
                # Calculate total order weight
                total_order_weight = (
                    (legs_required * leg_weight) +
                    (wings_required * wing_weight) +
                    (flesh_required * flesh_weight)
                )

                # Calculate remaining parts of the chicken used
                remaining_legs = (chickens_needed * 2) - legs_required
                remaining_wings = (chickens_needed * 2) - wings_required
                remaining_flesh = chickens_needed - flesh_required

                # reduce the chicken numbers from inventory and update
                inventory.chickens -= chickens_needed
                inventory.save()

                # here we can calculate the remaining parts
                remaining_parts_weight = (
                    (remaining_legs * leg_weight) +
                    (remaining_wings * wing_weight) +
                    (remaining_flesh * flesh_weight)
                )

                print(remaining_parts_weight)

                total_remaining_weight = inventory.chickens * chicken_weight

                message = (
                    f"Chickens needed: {chickens_needed}. "
                    f"Total order weight: {total_order_weight:.2f} kg. "
                    f"Remaining parts from last chicken used: {remaining_legs} legs, "
                    f"{remaining_wings} wings, {remaining_flesh} flesh portions. "
                    f"Remaining parts weight: {remaining_parts_weight:.2f} kg. "
                    f"Total remaining weight of the inventory: {total_remaining_weight:.2f} kg."
                )
        else:
            message = "Invalid form submission."

    else:
        form = OrderForm()

    return render(request, 'inventory/order_form.html', {
        'form': form,
        'message': message if 'message' in locals() else ''
    })
