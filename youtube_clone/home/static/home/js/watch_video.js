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

async function addComment() {
  // getting video instance
  // const video = document.querySelector("video");
  // const video_id = video.getAttribute("data-video-id");
  const new_comment = document.getElementById("new-comment").value;

  let content = {
    new_comment: new_comment,
  };

  const uri = url;
  // FIXME: CSRF token not being passed
  console.log("csrf token: \n");
  const csrftoken = getCookie("csrftoken");
  console.log(csrftoken);

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
      console.log(data);
    });

  getComments()
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

async function getComments() {
  const uri = comments_url;

  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const fetchedComments = JSON.parse(data.comments)
      const NUM_COMMENTS = Object.keys(fetchedComments).length
      console.log(fetchedComments[1])
      document.getElementById("num-comments").innerHTML = `${NUM_COMMENTS} comments`;

      for (let i = 1; i < NUM_COMMENTS+1; i++) {
        const commentsContainer = document.getElementById("comments-container")

        const comment = document.createElement("section");
        comment.setAttribute("class", "comment");

        const profile = document.createElement("div")
        profile.setAttribute("class", "profile")

        const profileImage = document.createElement("img")
        profileImage.setAttribute("src", "https://picsum.photos/seed/picsum/40/40")
        profileImage.setAttribute("alt", "[fetched image]")
        profileImage.setAttribute("width", "40")
        profileImage.setAttribute("height", "40")

        const divContainer = document.createElement("div")

        const channelAndAge = document.createElement("div")
        channelAndAge.setAttribute("class", "channel-and-age")

        const channel = document.createElement("p")
        channel.setAttribute("class", "channel")
        channel.innerHTML = fetchedComments[i].commenter;

        const commentAge = document.createElement("p")
        commentAge.setAttribute("class", "age")
        commentAge.innerHTML = fetchedComments[i].date_posted; // TODO: Find difference between current time and date posted and set that as age

        const commentContent = document.createElement("p")
        commentContent.setAttribute("class", "content")
        commentContent.innerHTML = fetchedComments[i].content;

        const optionButtons = document.createElement("div")
        optionButtons.setAttribute("class", "options")

        const likeButton = document.createElement("button")
        likeButton.setAttribute("class", "option-btn")
        likeButton.innerHTML = "like"

        const dislikeButton = document.createElement("button")
        dislikeButton.setAttribute("class", "option-btn")
        dislikeButton.innerHTML = "dislike"

        const replyButton = document.createElement("button")
        replyButton.setAttribute("class", "option-btn")
        replyButton.innerHTML = "reply"


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

window.onload = function () {
  getComments();
};
