/*
==================================================================================


                          Table of Contents



1. navMotion: Function that displays category dropdown.

2. navChangeColor: Function that turns navBar visible when scrolled (PC).

3. arrowMotion: Function that allows arrows in main page to slide among images (PC).

4. arrowMotion2: Function that allows arrows in about page to slide among images MADE WITH JQUERY

5. serviceActive: Function that allows service section to disappear typography and to show logo MADE WITH JQUERY

6. mainApp: Function that activates all of them in one main function.


=================================================================================
*/

/*
===============================================================
                        1. navMotion

            Function that displays category dropdown


===============================================================
*/

function navMotion(){
    const categoryDropdownButton = document.querySelector('#nav-bar-dropdown a:first-child');
    const categoryDropdownListContainer = document.querySelector('#category-dropdown-list-container');
    


    categoryDropdownButton.addEventListener('click', function() {
        categoryDropdownListContainer.toggleAttribute('hidden');    
      });

}






/*
===============================================================
                        6. mainApp 

    Function that activates all of them in one main function


===============================================================
*/
function mainApp(){
    navMotion()

    


}
mainApp();










