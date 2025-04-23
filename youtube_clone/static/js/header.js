function displayMenu() {
  // TODO: Complete
  let dropdownMenu = document.getElementById("dropdown-menu")
  if (dropdownMenu.style.display === "none") {
    dropdownMenu.style.display = "block"
  } else {
    dropdownMenu.style.display = "none"
  }
}

function toggleSidebar() {
  // FIXME: Messes up web page styles when hidden
  let sidebarMenu = document.getElementById("sidebar")
  if (sidebarMenu.style.display === "none") {
    sidebarMenu.style.display = "block"
  } else {
    sidebarMenu.style.display = "none"
  }
}