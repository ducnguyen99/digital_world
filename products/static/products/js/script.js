function getCSRF(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCSRF('csrftoken');


var updateBtns = document.getElementsByClassName('update-cart')
for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user === 'AnonymousUser') {
            console.log('Not authenticated')
            addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
        }
    })
}

// Can optimize this



function updateUserOrder(productId, action) {
    console.log('User is authenticated')
    var url = '/update_cart/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            location.reload()
        })
}


function updateOrderDelivery(deliveryOption) {
    console.log('User is authenticated')
    var url = '/update_order_delivery/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'deliveryOption': deliveryOption })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            location.reload()
        })
}


function addCookieItem(productId, action) {
    console.log('not log in')
    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    console.log('Cart', cart)
    location.reload()

}