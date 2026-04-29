
function fetchFeed() {
  const filter = document.querySelector("input[name='filter']:checked").value
  let content = {
    filter: filter,
  };

  console.log('filter_videos_url: ', filter_videos_url)
  const uri = filter_videos_url;
  const csrftoken = getCookie("csrftoken");

  // posts to url 'filter_videos' and thus calls filter_videos() in home/views.py
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
<!--            onerror attrs are used in case bandwidth cap is exceedd on backblaze, so using default assets temporarily-->
            <img
              src="${ video.thumbnail }"
              alt="video thumbnail"
              width="373"
              height="209"
              onerror="this.src='/static/img/thumbnail.png'"
            />
            <section class="video-info">
              <div class="channel-icon">
                <a href=${channel_url}>
                  <img
                    src=${video.author__profile_pic}
                    width="40"
                    height="40"
                   alt=${video.author__profile_pic}
                   onerror="this.src='/static/img/default-user-icon.jpg'"
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



$(document).ready(function(){
  fetchFeed();
})