/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
    - Through Code Institute walkthrough
*/

// get client secret and public key from template, remove quotes */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
// create instance of stripe elements */
var elements = stripe.elements();

// create styles for card element */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Source Serif Pro", serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// create card element and attach styles */
var card = elements.create('card', {style: style});
// mount to div in checkout.html */
card.mount('#stripe-card-element');


/* Handle validation errors on the card element each time
there is a change */
card.addEventListener('change', function (event) {
    var stripeErrorDiv = document.getElementById('stripe-errors');
    // display errors in checkout.html */
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(stripeErrorDiv).html(html);
    } else {
        stripeErrorDiv.textContent = '';
    }
});


/* Handle form submit */
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // prevent default submit method
    ev.preventDefault();
    // disable submit button to prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('stripe-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            // enable submit button if error to allow resubmission
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // submit form if no errors
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});