




$(document).ready(function() {
  // const selected_content = document.querySelector("input[name='navigate-channel']:checked").value
  const selected_content = window.location.pathname.split('/').at(-2)
  if (selected_content === 'home') {
    document.getElementById("home").classList.add('active')
  }

})