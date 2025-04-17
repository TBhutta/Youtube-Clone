
function fetchFeed() {
  const filter = document.querySelector("input[name='filter']:checked").value
  console.log(filter)

  let content = {
    filter: filter,
  };

  const uri = filter_videos_url;
  // uri = uri.replace("1234", filter)

  const csrftoken = getCookie("csrftoken");

  fetch(uri, {
    method: "POST",
    body: JSON.stringify(content),
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const videos_container = document.getElementById("videos-container")
      videos_container.innerHTML = ""

      const NUM_VIDEOS = Object.keys(data).length

      for (let i = 0; i < NUM_VIDEOS; i++) {
        const video = data[i]
        let channel_url = view_channel_url.replace("1234", video.author__username)

        const video_url = `/watch/${video.id}`
        videos_container.innerHTML += `
        <a href=${video_url} class="video-link">
          <div class="video">
            <!-- TODO: Make it so that the video is played a few seconds after hovering over the thumbnail. -->
            <img
              src=${ video.thumbnail }
              alt="video thumbnail"
              width="373"
              height="209"
            />
            <section class="video-info">
              <div class="channel-icon">
                <a href=${channel_url}>
                  <img
                    src=${video.author__profile_pic}
                    alt="profile"
                    width="40"
                    height="40"
                  />
                </a>
              </div>
              <section>
                <p class="video-title" style="">
                  ${video.title}
                </p>
                <a href=${channel_url} class="video-channel" >
                  ${video.author__username}
                </a>
                <p class="video-views" style="color: rgb(163, 161, 161)">
                  ${video.views} views
                </p>
              </section>
            </section>
          </div>
        </a>
        `
      }
    });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

window.onload = function () {
    console.log("home loaded")
    fetchFeed();
}