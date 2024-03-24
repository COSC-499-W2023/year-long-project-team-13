/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
    document.getElementById("mySidebar").style.width = "350px";
    document.querySelector("#filled-container").style.marginLeft = "250px";
  }

  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.querySelector("#filled-container").style.marginLeft = "0";
  }

  function toggleNav() {
    if (document.getElementById("mySidebar").style.width == "350px") {
      closeNav();
    } else {
      openNav();
    }
  }
