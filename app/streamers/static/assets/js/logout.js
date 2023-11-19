function confirmLogOut() {
    var ask = confirm("Do you want to logout?");
      if (ask) {
          return location.href = "{% url 'logout' %}";;
      } else {
          return false;
      }
  }
