/*
==================================================================================


                          Table of Contents



1. navMotion: Function that displays category dropdown.

2. navChangeColor: Function that turns navBar visible when scrolled (PC).

3. arrowMotion: Function that allows arrows in main page to slide among images (PC).

4. messageMotion: Function that animates Success Messages

6. mainApp: Function that activates all of them in one main function.


=================================================================================
*/

/*
===============================================================
                        1. navMotion

            Simple Function that displays category dropdown


===============================================================
*/

function navMotion(){
    const categoryDropdownButton = document.querySelector('#nav-bar-dropdown a:first-child');
    const profileBtn = document.querySelector('.profile-link-container');
    const categoryDropdownListContainer = document.querySelector('#category-dropdown-list-container');
    const profileDropdownListContainer = document.querySelector('#profile-dropdown-list-container');
    


    

    categoryDropdownButton.addEventListener('click', function() {
        categoryDropdownListContainer.toggleAttribute('hidden');    
        
      });


      if (profileBtn == null){
        return;
      }
    
      else{
        profileBtn.addEventListener('click', function() {
          profileDropdownListContainer.toggleAttribute('hidden');    
        });
      }
     













}

/*
===============================================================
                        2. bannerMotion

            Function that activates banner carousel


===============================================================
*/

function bannerMotion(){

  

    // Banner button opacity function
    function btnOpacity(){
        const btnLeft = document.querySelector('.prev_button');
        const btnRight = document.querySelector('.next_button');
        const banner = document.querySelector('.banner-img-container');
        const btns = [btnLeft, btnRight];


        // if the current page is not the home page, and therefore it is null, then you return.
        if (banner == null){
          return;
        }

        // Else, it will do the following display of the banner.
        else {
          banner.addEventListener('mouseenter', btnOpacityMouseEnter);
          banner.addEventListener('mouseleave', btnOpacityMouseLeave);

          function btnOpacityMouseEnter(event) {
              if (event.isTrusted == true){
                  btns[0].classList.add('btn-active');
                  btns[1].classList.add('btn-active');

              }

          }

          function btnOpacityMouseLeave(event) {
              if (event.isTrusted == true){
                  btns[0].classList.remove('btn-active');
                  btns[1].classList.remove('btn-active');

              }


          }
              // console.log("FIRED")

          // Banner slide function
          window.onload = function () {
            const helpers = (function () {
              function getDOMElements(DOMSelectors) {
                let DOMElements = {};
                for (let selector in DOMSelectors) {
                  if (DOMSelectors.hasOwnProperty(selector)) {
                    DOMElements[selector] = document.querySelector(
                      DOMSelectors[selector]
                    );
                  }
                }
                return DOMElements;
              }
              return {
                getDOMElements
              };
            })();
          
            const modal = (function () {
              const state = {
                counter: 0,
                intervalID: 0
              };
              let CONSTANTS = {
                ACTIVE_CLASS_NAME: "active",
                TIMER: 5000,
                TRANSITION: "all .6s ease-out"
              };
              function addConstant(key, value) {
                CONSTANTS[key] = value;
              }
          
              return {
                state,
                CONSTANTS,
                addConstant
              };
            })();
          
            const view = (function (helpers) {
              const DOMSelectors = {
                carouselInnerSlider: ".banner-img-slide",
                dots: ".dots",
                slide: "#slide",
                prevButton: ".prev_button",
                nextButton: ".next_button",
                carouselImages: ".banner-img-slide img",
                dot: ".dot",
              };
              const DOMElements = helpers.getDOMElements(DOMSelectors);
              const CAROUSEL_IMAGES = [
                ...document.querySelectorAll(DOMSelectors.carouselImages)
              ];
              const DOTS = [...document.querySelectorAll(DOMSelectors.dot)];
              function moveSliderToIndex(IMAGE_SIZE, index) {
                DOMElements.carouselInnerSlider.style.transform = `translateX(-${
                  IMAGE_SIZE * index
                }px)`;
              }
              function addClassToIndex(className, index) {
                CAROUSEL_IMAGES[index].classList.add(className);
              }
              function removeClassToIndex(className, index) {
                CAROUSEL_IMAGES[index].classList.remove(className);
              }
              function addBackGroundToCurrentIndex(index) {
                DOTS[index].style.background = "#FFFFFF";
              }
              function removeBackGroundToCurrentIndex(index) {
                DOTS[index].style.background = "transparent";
              }
              function setTransition(element, transition) {
                element.style.transition = `${transition}`;
              }
              return {
                DOMSelectors,
                moveSliderToIndex,
                addClassToIndex,
                removeClassToIndex,
                addBackGroundToCurrentIndex,
                removeBackGroundToCurrentIndex,
                setTransition
              };
            })(helpers);
          
            const controller = (function (modal, view, helpers) {
              const DOMSelectors = view.DOMSelectors;
              const DOMElements = helpers.getDOMElements(DOMSelectors);
              
              function initApp() {
                const imageSize = DOMElements.carouselInnerSlider.clientWidth;
                // DOMElements.carouselImages.style.margin = `${1.1 + 6}`;
                const imagesCount =
                  [...document.querySelectorAll(DOMSelectors.carouselImages)].length - 1;
                modal.addConstant("IMAGE_SIZE", imageSize);
                modal.addConstant("TOTAL_IMAGES", imagesCount);
                view.moveSliderToIndex(modal.CONSTANTS.IMAGE_SIZE, modal.state.counter);
                handleAdding();
                DOMElements.nextButton.addEventListener("click", handleNextImage);
                DOMElements.prevButton.addEventListener("click", handlePrevImage);
                DOMElements.dots.addEventListener("click", handleDotClick);
              }
              function removeEventListeners() {
                DOMElements.nextButton.removeEventListener("click", handleNextImage);
                DOMElements.prevButton.removeEventListener("click", handlePrevImage);
                DOMElements.dots.removeEventListener("click", handleDotClick);
              }
              function handleNextImage() {
                handleRemove();
                if (modal.state.counter === modal.CONSTANTS.TOTAL_IMAGES) {
                  modal.state.counter = -1;
                }
                modal.state.counter += 1;
                handleAdding();
                view.moveSliderToIndex(modal.CONSTANTS.IMAGE_SIZE, modal.state.counter);
              }
              function handlePrevImage() {
                handleRemove();
                if (modal.state.counter === 0) {
                  modal.state.counter = modal.CONSTANTS.TOTAL_IMAGES + 1;
                }
                modal.state.counter -= 1;
                handleAdding();
                view.moveSliderToIndex(modal.CONSTANTS.IMAGE_SIZE, modal.state.counter);
              }
              function handleDotClick(event) {
                const value = Number(event.target.value);
                if (!isNaN(value)) {
                  handleRemove();
                  modal.state.counter = value;
                  view.moveSliderToIndex(modal.CONSTANTS.IMAGE_SIZE, modal.state.counter);
                  handleAdding();
                }
              }
              function handleSlide() {
                const isChecked = true;
                if (isChecked) {
                  modal.state.intervalID = setInterval(() => {
                    handleNextImage();
                  }, modal.CONSTANTS.TIMER);
                } else {
                  clearInterval(modal.state.intervalID);
                  modal.state.intervalID = null;
                }

                
              }
              handleSlide();

              function handleRemove() {
                view.removeClassToIndex(
                  modal.CONSTANTS.ACTIVE_CLASS_NAME,
                  modal.state.counter
                );
                view.removeBackGroundToCurrentIndex(modal.state.counter);
              }
              function handleAdding() {
                view.addClassToIndex(
                  modal.CONSTANTS.ACTIVE_CLASS_NAME,
                  modal.state.counter
                );
                view.addBackGroundToCurrentIndex(modal.state.counter);
              }
              DOMElements.carouselInnerSlider.addEventListener(
                "transitionstart",
                removeEventListeners
              );
              DOMElements.carouselInnerSlider.addEventListener("transitionend", initApp);
              view.setTransition(
                DOMElements.carouselInnerSlider,
                modal.CONSTANTS.TRANSITION
              );
              return {
                initApp,
                removeEventListeners
              };
            })(modal, view, helpers);
          
            controller.initApp();
          
            window.addEventListener("resize", () => {
              controller.removeEventListeners();
              controller.initApp();
            });
        


        };




        }

         
    }
        
      btnOpacity()
      

}


/*
===============================================================
                        4. messageMotion

            Function that animates Success Messages

===============================================================
*/

function messageMotion (){
  const successMessage = document.querySelector('.message-success-container');

  if (successMessage == null){
    return
  }

  else{
    document.addEventListener('DOMContentLoaded', () => {
      successMessage.style.animation = `successMessageMotion 1s ease forwards`;
  
    });
  
    function messageDisappear(){
      successMessage.style.animation = `successMessageMotionDisappear 1s`
    }
  
  
    function messageOpacityZero(){
      successMessage.classList.add('message-success--active')
      setTimeout(messageDisappear, 1500)
      
  
    }
    setTimeout(messageOpacityZero, 5000);
  
  }
  



}



/*
===============================================================
                  6. Add and Remove from cart

            Function Adds and removes items from cart


===============================================================
*/



function cartFunctionality(){
  var updateAnchors = document.getElementsByClassName("update-cart")


  for (i=0; i < updateAnchors.length; i++){
    updateAnchors[i].addEventListener("click", function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        if (user != "anonymousUser"){
          updateUserOrder(productId, action)
        }
        
    })
  }



}

function updateUserOrder(productId, action){
  var url = '/api/update_item'
  fetch(url, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({'productId': productId, 'action': action})
  })
  .then((response) => {
    return response.json();
  })
  .then((data) => {

    if (window.location.pathname != "/"){
      var productItem = document.querySelector(`[data-product="prod-${data[1].product}"]`);
      var cartItemPrice = productItem.querySelector(".product-item-price")
      var cartItemNoDiscountPrice = productItem.querySelector(".product-item-del-price")
    }

    var cartItemCounters = document.querySelectorAll('.cart-items')
    var cartItemsTotal = document.querySelectorAll('.cart-total')


    cartItemCounters.forEach((item) =>{
      item.textContent = data[0].get_cart_amount_of_items;

    })

    if (data[1].quantity === 0){
      productItem.remove();
    }

    if (data[1].total_amount != cartItemPrice){
      cartItemPrice.textContent = data[1].total_amount
    }
    if (data[1].total_amount_without_discount != cartItemNoDiscountPrice){
      cartItemNoDiscountPrice.textContent = data[1].total_amount_without_discount
    }
    cartItemsTotal.forEach((item) => {
      if (data[0].get_cart_total != item){
        item.textContent = data[0].get_cart_total
      }
    })

  })
}



/*
===============================================================
                        7. mainApp 

    Function that activates all of them in one main function


===============================================================
*/
function mainApp(){
    navMotion();
    bannerMotion();
    messageMotion();
    cartFunctionality();


}
mainApp();










