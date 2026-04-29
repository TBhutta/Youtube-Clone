
function showExtraOptions() {
  const extraOptionsBtn = document.getElementById("extra-options")
  if (extraOptionsBtn.style.display === "none") {
    extraOptionsBtn.style.display = "block"
  } else {
    extraOptionsBtn.style.display = "none"
    extraOptionsBtn.style.zIndex = "0"
  }

}



function showButtons() {
  console.log("clicked");
  document.querySelectorAll(".buttons").forEach((item) => {
    item.style.display = "block";
  });
}

function hideButtons() {
  console.log("clicked");
  document.querySelectorAll(".buttons").forEach((item) => {
    item.style.display = "none";
  });
}

function likeVideo() {
  const uri = like_url;

  fetch(uri)
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(err => console.error(err))
}

function dislikeVideo() {
  const uri = dislike_url;

  fetch(uri)
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(err => console.error(err))
}

async function addComment() {
  // getting video instance
  const new_comment = document.getElementById("new-comment").value;

  let content = {
    new_comment: new_comment,
  };

  const uri = url;
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
    .then((data) => {});

  document.getElementById("new-comment").value = ""
  console.log("getting comments")
  getComments()
}



function getComments() {
  const uri = comments_url;

  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const commentsContainer = document.getElementById("comments-container")
      commentsContainer.innerHTML = "" // Resetting the container

      const fetchedComments = JSON.parse(data.comments)
      const NUM_COMMENTS = Object.keys(fetchedComments).length
      const video_ids = Object.keys(fetchedComments)
      document.getElementById("num-comments").innerHTML = `${NUM_COMMENTS} comments`;

      for (let i = 0; i < NUM_COMMENTS; i++) {
        const comment = document.createElement("section");
        comment.setAttribute("class", "comment");

        const profile = document.createElement("div")
        profile.setAttribute("class", "profile")

        const profileImage = document.createElement("img")
        profileImage.setAttribute("src", fetchedComments[video_ids[i]].commenter_profile_pic)
        profileImage.setAttribute("alt", "[fetched image]")
        profileImage.setAttribute("width", "40")
        profileImage.setAttribute("height", "40")

        const divContainer = document.createElement("div")

        const channelAndAge = document.createElement("div")
        channelAndAge.setAttribute("class", "channel-and-age")

        const channel = document.createElement("p")
        channel.setAttribute("class", "channel")
        // The code below gets the index of the correct video, according to the id of the video
        channel.innerHTML = fetchedComments[video_ids[i]].commenter;

        const commentAge = document.createElement("p")
        commentAge.setAttribute("class", "age")
        commentAge.innerHTML = fetchedComments[video_ids[i]].date_posted; // TODO: Find difference between current time and date posted and set that as age

        const commentContent = document.createElement("p")
        commentContent.setAttribute("class", "content")
        commentContent.innerHTML = fetchedComments[video_ids[i]].content;

        const optionButtons = document.createElement("div")
        optionButtons.setAttribute("class", "options-container")


        const likeButtonIcon = "" +
            "<svg height=\"24\" width=\"24\" viewBox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\">\n" +
            "\t<g fill=\"none\">\n" +
            "\t\t<path d=\"m15 10l-.986-.164A1 1 0 0 0 15 11v-1ZM4 10V9a1 1 0 0 0-1 1h1Zm16.522 2.392l.98.196l-.98-.196ZM6 21h11.36v-2H6v2ZM18.56 9H15v2h3.56V9Zm-2.573 1.164l.805-4.835L14.82 5l-.806 4.836l1.973.328ZM14.82 3h-.214v2h.214V3Zm-3.543 1.781L8.762 8.555l1.664 1.11l2.516-3.774l-1.665-1.11ZM7.93 9H4v2h3.93V9ZM3 10v8h2v-8H3Zm17.302 8.588l1.2-6l-1.96-.392l-1.2 6l1.96.392ZM8.762 8.555A1 1 0 0 1 7.93 9v2a3 3 0 0 0 2.496-1.336l-1.664-1.11Zm8.03-3.226A2 2 0 0 0 14.82 3v2l1.972.329ZM18.56 11a1 1 0 0 1 .981 1.196l1.961.392A3 3 0 0 0 18.561 9v2Zm-1.2 10a3 3 0 0 0 2.942-2.412l-1.96-.392a1 1 0 0 1-.982.804v2ZM14.606 3a4 4 0 0 0-3.329 1.781l1.665 1.11A2 2 0 0 1 14.606 5V3ZM6 19a1 1 0 0 1-1-1H3a3 3 0 0 0 3 3v-2Z\" fill=\"currentColor\"/>\n" +
            "\t\t<path d=\"M8 10v10\" stroke=\"currentColor\" strokeWidth=\"2\"/>\n" +
            "\t</g>\n" +
            "</svg>"
        const likeButton = document.createElement("button")
        likeButton.setAttribute("class", "option-btn")
        likeButton.setAttribute("onclick", "likeComment()")
        likeButton.innerHTML = likeButtonIcon

        const dislikeButtonIcon = "" +
            "<svg height=\"24\" width=\"24\" viewBox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\">\n" +
            "\t<path d=\"M20 3H6.693A2.01 2.01 0 0 0 4.82 4.298l-2.757 7.351A1 1 0 0 0 2 12v2c0 1.103.897 2 2 2h5.612L8.49 19.367a2.004 2.004 0 0 0 .274 1.802c.376.52.982.831 1.624.831H12c.297 0 .578-.132.769-.36l4.7-5.64H20c1.103 0 2-.897 2-2V5c0-1.103-.897-2-2-2zm-8.469 17h-1.145l1.562-4.684A1 1 0 0 0 11 14H4v-1.819L6.693 5H16v9.638L11.531 20zM18 14V5h2l.001 9H18z\" fill=\"currentColor\"/>\n" +
            "</svg>"
        const dislikeButton = document.createElement("button")
        dislikeButton.setAttribute("class", "option-btn")
        dislikeButton.setAttribute("onclick", "DislikeComment()")
        dislikeButton.innerHTML = dislikeButtonIcon

        const replyButton = document.createElement("button")
        replyButton.setAttribute("class", "option-btn reply-btn")
        replyButton.setAttribute("onclick", "replyComment()")
        replyButton.innerHTML = "<p class='reply-label'>Reply</p>"

        profile.appendChild(profileImage)
        comment.appendChild(profile)

        channelAndAge.appendChild(channel)
        channelAndAge.appendChild(commentAge)
        divContainer.appendChild(channelAndAge)

        divContainer.appendChild(commentContent)

        optionButtons.appendChild(likeButton)
        optionButtons.appendChild(dislikeButton)
        optionButtons.appendChild(replyButton)
        divContainer.appendChild(optionButtons)
        comment.appendChild(divContainer)

        commentsContainer.appendChild(comment)
      }
    });
}

// TODO: I can pass in parameters according to chosen topic from nav bar to select videos
function getRecommendedVideos() {
  const uri = get_recommendations_url;

  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const recommendedVideosContainer = document.getElementById("recommended-videos");
      const fetchedVideos = JSON.parse(data.videos)
      const NUM_VIDEOS = Object.keys(fetchedVideos).length
      const videoIDs = Object.keys(fetchedVideos)

      for (let i = 0; i < NUM_VIDEOS; i++) {
        const videoID = videoIDs[i]
        const video_url = `/watch/${videoID}` // FIXME: try to implement a way with django's url format
        recommendedVideosContainer.innerHTML += `
          <a href=${video_url} class="video-container">
            <div class="recommended-video">
              <img
                src=${fetchedVideos[videoIDs[i]].thumbnail}
                alt="[fetched image]"
                width="168"
                height="94"
              />
            </div>
            <section class="video-info">
              <p class="recommended-video-title">${fetchedVideos[videoIDs[i]].title}</p>
              <p class="recommended-video-channel">${fetchedVideos[videoIDs[i]].author}</p>
              <div class="views-and-age">
                <p class="views">${fetchedVideos[videoIDs[i]].views} views . </p>
                <p class="age"> ${fetchedVideos[videoIDs[i]].upload_date}</p>
              </div>
            </section>
          </a>
        `
      }


    })
}



function getTime() {
  const video = document.getElementById("current-video")

  // if (video.currentTime === video.duration || video.currentTime === 30) {
  const uri = increment_views_url;
  const csrftoken = getCookie("csrftoken");

  fetch(uri, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
    });
    // }
}

function getPlaylists() {
  const uri = get_playlists_url

  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      const playlists = Object.values(data.playlists)
      let user_playlists = document.getElementById("user-playlists")

      for (let [k, v] of Object.entries(data.playlists)) {
        if (data["video_saved_playlists"].includes(parseInt(k))) {
          user_playlists.innerHTML += `
            <li>
              <input type="checkbox" name="playlist" id="${k}" value="${k}" onclick="addToPlaylist(this.id)" checked  >
              <label for="${k}">${v}</label>
            </li>
          `
        } else {
          user_playlists.innerHTML += `
            <li>
              <input type="checkbox" name="playlist" id="${k}" value="${k}" onclick="addToPlaylist(this.id)"  >
              <label for="${k}">${v}</label>
            </li>
          `
        }
      }
    })
}

function addToPlaylist(id) {
  const checkbox = document.getElementById(id);
  const action = checkbox.checked ? "checked" : "unchecked"

  let uri = add_video_to_playlist_url.replace('11', id)
  // console.log(uri);

  let content = {
    action: action
  };

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
      console.log(data)
    });

}

function makeNewPlaylist() {
  let modal_content = document.getElementById("modal-content")

  modal_content.innerHTML = ""
  modal_content.innerHTML += `
    <h1>New playlist</h1>
    <input type="text" placeholder="Choose a title" id="playlist-name">
    <select name="visibility" id="visibility">
      <option value="public">Public</option>
      <option value="unlisted">Unlisted</option>
      <option value="private" selected>Private</option>
    </select>
    <div>
      <button>Cancel</button>
      <button onclick="createAndAddToPlaylist()">Create</button>
    </div>
  `
}

function createAndAddToPlaylist() {
  const playlist_name = document.getElementById("playlist-name").value
  // TODO: Store playlist visibility as well
  const playlist_visibility = document.getElementById("visibility")

  const csrftoken = getCookie("csrftoken");
  let uri = create_playlist_url;
  fetch(uri, {
    method: "POST",
    body: JSON.stringify({name: playlist_name, id: video_id}),
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("playlist-modal").style.display = "none";
      document.getElementById("modal-content").style.display = "none";

    });

}


document.addEventListener("DOMContentLoaded", () => {
  console.log(is_subscribed)
  if (is_subscribed === "True") {
    let subscribe_btn = document.getElementById("subscribe-btn")
    subscribe_btn.textContent = "Unsubscribe"
  }
})

window.onload = function () {
  getComments();
  getRecommendedVideos();


  let playlist_modal = document.getElementById("playlist-modal")
  let save_btn = document.getElementById("save-btn")
  let close_btn = document.getElementById("playlist-modal-close-btn")

  save_btn.onclick = function () {
    playlist_modal.style.display = "block"
  }

  close_btn.onclick = function () {
    playlist_modal.style.display = "none"
  }

  getPlaylists()
};

setTimeout(getTime, 30000)
