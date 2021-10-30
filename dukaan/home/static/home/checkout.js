function getItemsFromCart() {
    let itemsincart = localStorage.getItem('itemincart');
    if(itemsincart === null) {
        return [];
    }
    let itemsList = itemsincart.split(',').filter(item=>item!=="")
    itemsList = itemsList.map(item => {
        // name=qty@price
        let item_name = item.split('=')[0];
        let item_qty = item.split('=')[1].split('@')[0];
        let item_price = item.split('=')[1].split('@')[1];
        return [item_name, item_qty, item_price]
    })
    return itemsList;
}

function clearLocalStorage() {
    localStorage.setItem('itemincart', '');
    alert('Order Placed');
}
console.log(getItemsFromCart())

let itemsArr = getItemsFromCart()
let form = document.querySelector('form')
let formGroup = document.querySelector('.form-group')
let sum = 0;
// console.log(formGroup);
itemsArr.forEach((item, index) => {
    let newFormGroup = formGroup.cloneNode(true);
    let nameinputs = newFormGroup.querySelector('input:first-child');
    let qtyinputs = newFormGroup.querySelector('input:nth-child(2)');
    let priceinputs = newFormGroup.querySelector('input:nth-child(3)');
    let inputsarr = [nameinputs, qtyinputs, priceinputs]
    let tr = document.createElement('tr');
    for(let i=0; i<3; i++) {
        let td = document.createElement('td');
        td.innerHTML = item[i];
        tr.appendChild(td);
        let num = index + 1;
        inputsarr[i].id += num.toString()
        inputsarr[i].name += num.toString()
    }
    let td = document.createElement('td');
    td.innerHTML = parseFloat(item[1]) * parseFloat(item[2]);
    sum += parseFloat(item[1]) * parseFloat(item[2]);
    tr.appendChild(td);

    document.querySelector('table').append(tr);
    nameinputs.value = item[0];
    qtyinputs.value = item[1];
    priceinputs.value = item[2];
    form.appendChild(newFormGroup)
    form.insertBefore(newFormGroup, document.querySelector('#checkoutbtn'))
})
let tr =  document.createElement('tr');
let td = document.createElement('td');
td.innerHTML = "Total";
td.colSpan = 3
tr.appendChild(td);

td = document.createElement('td');
td.innerHTML = sum;
tr.appendChild(td);
document.querySelector('table').append(tr);


document.querySelector('.form-group:first-of-type').remove();


let printBtn = document.querySelector('#print')
printBtn.addEventListener('click', () => {
    print();
})

