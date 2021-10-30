from django.contrib.auth.models import User
from django.shortcuts import redirect, render
# from reportlab.platypus.doctemplate import SimpleDocTemplate
from .models import Invoice, Item, Quantity
from .forms import InvoiceForm, ItemForm
import datetime
import calendar
# Create your views here.


def test(request):
    form = ItemForm(None)
    if request.method == 'POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            item = Item.objects.last()
            item.margin = item.selling_price - item.cost_price
            item.save()
            return redirect('/admin/')
    return render(request, "test.html", {"form": form})


list_of_products = {}
def display_items(request):
    form = InvoiceForm()
    list_of_items = Item.objects.all()
    if request.method=="POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method=="GET":
        print(request.GET.get('itemnames'))
        print(request.GET.get('productquantity'))
        list_of_products[request.GET.get('itemnames')]= request.GET.get('productquantity')
        for items in list_of_products:
            print(items)
    return render(request, 'home.html', {"form": form, "list": list_of_items})

# category_list = ['Essential', 'Electronics', 'Misc', 'Luggage & Bags']

def get_category_list():
    category_list = []
    for item in Item.objects.all():
        if item.category not in category_list:
          category_list.append(item.category)
    return category_list


def get_popular_item_from_itemset(itemset):
    score_dict = {}
    for item in itemset:
        score_dict[item.name] = [0, 0]
        score_dict[item.name][1]=item.selling_price
        quantity_obj_for_that_item = Quantity.objects.filter(item_selected__name=item.name)
        for quantity in quantity_obj_for_that_item:
            score_dict[item.name][0]+=quantity.quantity
    
    score_list = [(i, score_dict[i][0], score_dict[i][1]) for i in score_dict.keys()]
    score_list.sort(key= lambda x: x[1], reverse=True)
    score_list = score_list[:5]
    d = {}
    for item in score_list:
        d[item[0]] = [item[1], item[2]]
    return d

def return_items_by_key(search_key):
    item_list = {}
    for item in Item.objects.all():
        if (item.name.lower()).find(search_key.lower())>=0:
            item_list[item.name] = item.stock_left
    return item_list


def home_page(request):
    print(get_popular_item_from_itemset(Item.objects.all()))
    context_dict = {
        "all_categories": get_popular_item_from_itemset(Item.objects.all())
    }

    for category in get_category_list():
        context_dict[category] = get_popular_item_from_itemset(Item.objects.filter(category=category))
    context_dict['category_list'] = list(context_dict.keys())
    # print(context_dict)
    try:
        search_key = request.GET.get('searchbar')
        context_dict['items_list'] = return_items_by_key(search_key)
        return render(request, 'home.html', context=context_dict)
    except:
        return render(request, 'home.html', context=context_dict)

def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_data = dict(request.POST)
            form_data = {key: form_data[key][0] for key in form_data.keys()}
            num_keys = (len(form_data.keys())-1)//3
            price = 0
            curr = User.objects.get(pk=request.user.pk)
            print(curr)
            inv = Invoice(user_id = curr, payment_status=False, total_price = 0, profit=0)
            inv.save()
            for i in range(1, num_keys+1):
                item_name = form_data['itemname'+str(i)]
                item_qty = form_data['itemqty'+str(i)]
                q = Quantity(invoice_selected = inv, quantity=item_qty, item_selected = Item.objects.filter(name=item_name).first())
                q.save()
                print(item_name, item_qty)
                item_price = form_data['itemprice'+str(i)]
                print(item_price)
            # bill.save()
            # print(form_data)
    return render(request, 'checkout.html')

def chart(request):
    list_passed = list(Quantity.objects.all())
    month_dict = {}
    current_month = datetime.datetime.now().month
    for i in range(1, current_month+1):
        month_dict[calendar.month_name[i]] = 0
    for quantity in list_passed:
        month_dict[calendar.month_name[quantity.invoice_selected.date.month]]+=quantity.quantity

    list_str_by_month = "[" + ",".join([str(month_dict[i]) for i in month_dict.keys()]) + "]"

    # list_str = "[" + ",".join([str(i.quantity) for i in list_passed]) + "]"
    # print(list_str)
    # month_list = []
    print(Invoice.objects.all())
    for i in Invoice.objects.all():
        print(i.date.month)
        month_list = set(calendar.month_name[i.date.month])
        print(month_list)
    
    
    
    profit = 0
    for item in Invoice.objects.all():
        profit+= item.total_price
    pending_payment = []
    for item in Invoice.objects.all():
        if item.payment_status==False:
            pending_payment.append(item)
    return render(request, 'chart.html', { "profit": profit, "pending_payments": pending_payment, "list_by_month": list_str_by_month})