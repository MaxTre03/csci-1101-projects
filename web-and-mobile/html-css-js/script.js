window.addEventListener("load",function()
{
    // Get button element refrences .
    let clickCounterElemet = document.getElementById("click-counter");
    let clickButtonElemet = document.getElementById("click-button");

    // counter value.
    let counter = 0;

    //Click button function.
    let clickButtonFunction = function()
    {
        // Increment counter
        counter++;

        // Update click counter value.
        clickCounterElemet.innerHTML = counter;
    };

    // Attach click button.
    clickButtonElemet.addEventListener("click",clickButtonFunction);
});