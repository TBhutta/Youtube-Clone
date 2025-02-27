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
  // getting video id
  const video = document.querySelector("video");
  const video_id = video.getAttribute("data-video-id");
  const new_comment = document.getElementById("new-comment").value;

  let content = {
    new_comment: new_comment,
  };

  // FIXME: How to send this as properly formatted url string that django recognizes?
  const uri = url;
  fetch(uri, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}

async function getComments() {
  const video_id = video.getAttribute("data-video-id");
  let query = {
    video_id: video_id,
  };

  const uri = `{% url 'get-comments' video_id=0 %}`.replace(
    "0",
    video_id.toString()
  );

  fetch(uri, {
    method: "POST",
  });
}

window.onload = function () {
  console.log("loaded");
};
