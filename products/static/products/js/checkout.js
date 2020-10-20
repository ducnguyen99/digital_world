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

var form = document.getElementById('form')
form.addEventListener('submit', function(e) {
    e.preventDefault()
    console.log('Form submitted....')
    document.getElementById('form-button').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
})

function submitFormData() {
    console.log('Payment button clicked')
    var shippingInfo = {
        'address': null,
        'city': null,
        'state': null,
        'zipcode': null
    }

    shippingInfo.address = form.address.value
    shippingInfo.city = form.city.value
    shippingInfo.state = form.state.value
    shippingInfo.zipcode = form.zipcode.value

    var url = '/process_order/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'shipping': shippingInfo
            })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('Success:', data);
        })
}