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

function getCartFromItems(arr) {
    return arr.map(item=>{
        return `${item[0]}=${item[1]}@${item[2]}`;
    }).join(',')
}

let addCartButtons = document.querySelectorAll('.cartbuttons')
console.log(addCartButtons);
function addtocart(e) {
    // console.log(e, e.target.tagName);
    if(e.target.tagName.toLowerCase() == 'button') {
        let parentDiv = e.target.parentElement;
        let itemName = parentDiv.querySelector('.item-head').innerText;
        let itemQty = parentDiv.querySelector('input').value;
        let itemPrice = parentDiv.querySelector('.itemprice').innerText.split(' ')[1];
        if(itemQty === "") {
            parentDiv.querySelector('input').value = 1;
            itemQty = 1;
        }
        // console.log(itemName, itemQty);
        let currentItemsInCart = localStorage.getItem('itemincart') || '';
        let itemsArr = getItemsFromCart()
        let index = itemsArr.map(item => {
            return item[0];
        }).indexOf(itemName);
        if(index != -1) {
            itemsArr[index][1] = parseInt(itemsArr[index][1]) + parseInt(itemQty);
            currentItemsInCart = getCartFromItems(itemsArr)
        }
        else {
            currentItemsInCart += `,${itemName}=${itemQty}@${itemPrice}`
        }
        localStorage.setItem('itemincart', currentItemsInCart);
        console.log(currentItemsInCart);

        e.target.innerHTML = 'Added to Cart';
        e.target.style.background = 'lightgreen';
        setTimeout(() => {
            e.target.innerHTML = 'Add to Cart';
            e.target.style.background = 'orange';
        }, 3000)
    }
}
addCartButtons.forEach(button => {
    button.addEventListener('click', addtocart);
})