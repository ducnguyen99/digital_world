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
                // addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
        }
    })
}

// Can optimize this
var radioBtns = document.getElementById('pickup').onclick = function() {
    var deliveryOption = this.dataset.option
    updateOrderDelivery(deliveryOption)
}
var radioBtns = document.getElementById('standard-delivery').onclick = function() {
    var deliveryOption = this.dataset.option
    updateOrderDelivery(deliveryOption)
}
var radioBtns = document.getElementById('express-delivery').onclick = function() {
    var deliveryOption = this.dataset.option
    updateOrderDelivery(deliveryOption)
}

// Can optimize this

if (shipping_option === "Express Delivery") {
    document.getElementById('express-delivery').checked = true

} else if (shipping_option === "Standard Delivery") {
    document.getElementById('standard-delivery').checked = true
} else {
    document.getElementById('pickup').checked = true
    document.getElementById("shipping-info").classList.add('hidden');
}


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

// function shippingInfo() {
//     var radioBtns = document.getElementById('standard-delivery')
//     if (radioBtns.checked()) {
//         document.getElementById("shipping-info").classList.remove('hidden');
//     }
// }