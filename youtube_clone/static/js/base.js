// Gets all channels that have been subscribed to
function getSubscriptions() {
  const uri = get_subscriptions_url;

  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      const subscriptionsList = document.getElementById("subscriptions-list");
      subscriptionsList.innerHTML = "";

      const fetchedSubscriptions = JSON.parse(data.subscriptions)
      const NUM_SUBSCRIPTIONS = Object.keys(fetchedSubscriptions).length
      const channel_ids = Object.keys(fetchedSubscriptions)

      for (let i = 0; i < NUM_SUBSCRIPTIONS; i++) {
        // console.log(fetchedSubscriptions[channel_ids[i]].profile_pic)
        // console.log(channel_ids[i])

        subscriptionsList.innerHTML += `
        <li>
          <a href="/view-channel/${fetchedSubscriptions[channel_ids[i]].username}">
              <img src=${fetchedSubscriptions[channel_ids[i]].profile_pic} 
                  alt="channel icon" width="30" height="30"
              />
              ${fetchedSubscriptions[channel_ids[i]].username}
          </a>
        </li>
        `
      }
    })
}


document.addEventListener("DOMContentLoaded", function() {
  const modal = document.getElementById("disclaimer-modal");
  const closeBtn = document.getElementById("close-disclaimer");

  if (!localStorage.getItem("disclaimerShown")) {
    console.log('disclaimer not found');
    modal.style.display = "flex";
  }

  closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
    localStorage.setItem("disclaimerShown", "true");
  })
});


$(document).ready(function(){
  getSubscriptions();
});