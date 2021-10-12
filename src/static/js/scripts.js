/*!
* Start Bootstrap - Agency v7.0.8 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// initialization
const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const imgBox2 = document.getElementById('img-box2')
const form = document.getElementById('p-form')
const image = document.getElementById('id_image')
const image2 = document.getElementById('id_image2')
const btnBox = document.getElementById('btn-box')
const customRange = document.getElementById('customRange')
const customRange3 = document.getElementById('customRange3')
const outputRange = document.getElementById('rangeOutputId')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

// array for all buttons
const btns = [...btnBox.children]
// take back and save image from storage
const mediaURL = window.location.href + 'media/'
console.log(mediaURL)

const url = ""

// alert
const handleAlerts = (type, text) =>{
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                            ${text}
                        </div>`
}

// if there's change in id_image, so
image.addEventListener('change', ()=>{
    const img_data = image.files[0] //blob
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = `<img src="${url}" width="100%">`
    btnBox.classList.remove('not-visible')
    customRange.classList.remove('not-visible')
})

// same w the top, but for id_image 2
image2.addEventListener('change', ()=>{
    const img_data2 = image2.files[0]
    const url2 = URL.createObjectURL(img_data2)
    console.log(url2)
    imgBox2.innerHTML = `<img src="${url2}" width="100%">`
    })
    
// get the filter from which botton clicked
let filter = null
btns.forEach(btn => btn.addEventListener('click', ()=>{
    filter = btn.getAttribute('data-filter')
    console.log(filter)
}))

//if brigthening, showing range and set valuelet
let customRangeVal = 0
customRange3.onchange = function(event){
  outputRange.innerHTML = customRange3.value;
  console.log(customRange3.value)
  customRangeVal = customRange3.value
}



let pixel = outputRange.value
// if (filter != 'BRIGHTENING'){
//     pixel
// }
console.log(pixel)

// gather the data and send using AJAX
let id = null
form.addEventListener('submit', e=>{
    e.preventDefault()

    // Create new instance contain all data
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('image', image.files[0])
    fd.append('image2', image.files[0])
    fd.append('customRange', customRangeVal)
    fd.append('action', filter)
    fd.append('id', id)
    if(image2){
        fd.append('image2', image2.files[0])
    }
    // gather using ajax
    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response){
            const data = JSON.parse(response.data)
            console.log(data)
            imgBox.innerHTML = `<img src="${mediaURL + data[0].fields.image}" width="100%">`
            // though that we just show image result in 1 place.
            // if(image2){
            //     imgBox2.innerHTML = `<img src="${mediaURL + data[0].fields.image}" width="100%">`
            // }
            const sText = `successfully saved ${response.name}`
            handleAlerts('success', sText)
            setTimeout(()=>{
                alertBox.innerHTML = ""
            }, 3000)
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'ups..something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

console.log(form)