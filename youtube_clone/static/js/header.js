function displayMenu() {
  // TODO: Complete
  let dropdown_menu = document.getElementById("dropdown-menu")
  if (dropdown_menu.style.display === "none") {
    dropdown_menu.style.display = "block"
  } else {
    dropdown_menu.style.display = "none"
  }
}