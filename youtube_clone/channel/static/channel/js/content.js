async function fetchVideos(params) {
  fetch("http://127.0.0.1:8000/channel/content/videos", {
    headers: {
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data.name);
      document.getElementById("dynamic").innerHTML = data.name;
    });
}
async function fetchShorts(params) {
  fetch("http://127.0.0.1:8000/channel/content/shorts", {
    headers: {
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const dynamic = document.getElementById("dynamic");
      const table = document.createElement("table");

      const headers = table.insertRow(0);
      const title = headers.insertCell(-1);
      const visibility = headers.insertCell(-1);
      const restrictions = headers.insertCell(-1);
      const date = headers.insertCell(-1);
      const views = headers.insertCell(-1);
      const comments = headers.insertCell(-1);
      const likes = headers.insertCell(-1);

      title.innerHTML = "<th>Video</th>";
      visibility.innerHTML = "<th>visibility</th>";
      restrictions.innerHTML = "<th>restrictions</th>";
      date.innerHTML = "<th>date</th>";
      views.innerHTML = "<th>views</th>";
      comments.innerHTML = "<th>comments</th>";
      likes.innerHTML = "<th>likes</th>";
      dynamic.appendChild(table);
      console.log(data);
    });
}
