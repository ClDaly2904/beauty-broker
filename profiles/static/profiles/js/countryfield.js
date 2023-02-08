// JS for country selector in profile form
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#848a8a');
};
// get the value of the country input on change
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#848a8a');
    } else {
        // change to black if country is selected
        $(this).css('color', '#000');
    }
});