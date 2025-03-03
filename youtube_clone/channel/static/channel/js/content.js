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
      // Clearing section before any new query
      const dynamic = document.getElementById("dynamic");
      dynamic.innerHTML = "";

      // Creating new table with headers
      const table = document.createElement("table");
      const headers = table.insertRow(0);
      const video = headers.insertCell(-1);
      const visibility = headers.insertCell(-1);
      const restrictions = headers.insertCell(-1);
      const upload_date = headers.insertCell(-1);
      const views = headers.insertCell(-1);
      const comments = headers.insertCell(-1);
      const likes = headers.insertCell(-1);

      // Setting header names
      video.innerHTML = "<th>Video</th>";
      visibility.innerHTML = "<th>visibility</th>";
      restrictions.innerHTML = "<th>restrictions</th>";
      upload_date.innerHTML = "<th>upload_date</th>";
      views.innerHTML = "<th>views</th>";
      comments.innerHTML = "<th>comments</th>";
      likes.innerHTML = "<th>likes</th>";
      dynamic.appendChild(table);

      // Adding data to table
      for (let i = 0; i < data.titles.length; i++) {
        // Creating new row
        video_row = table.insertRow(-1);
        const current_video = video_row.insertCell(-1);
        const current_video_visibility = video_row.insertCell(-1);
        const current_video_restrictions = video_row.insertCell(-1);
        const current_video_date = video_row.insertCell(-1);
        const current_video_views = video_row.insertCell(-1);
        const current_video_comments = video_row.insertCell(-1);
        const current_video_likes = video_row.insertCell(-1);

        // Creating tags and elements to store data for a video
        const video_container = document.createElement("section");
        video_container.setAttribute("class", "video-container");

        const video_thumbnail = document.createElement("img");
        video_thumbnail.setAttribute("src", data.thumbnails[i]);
        video_thumbnail.setAttribute("alt", data.thumbnails[i]);
        video_thumbnail.setAttribute("width", "120");
        video_thumbnail.setAttribute("height", "68");

        const video_info = document.createElement("div");
        video_info.setAttribute("class", "video-info");

        const video_title = document.createElement("p");
        video_title.setAttribute("class", "title");
        video_title.innerHTML = data.titles[i];
        video_info.appendChild(video_title);

        const video_description = document.createElement("p");
        video_description.setAttribute("class", "description");
        video_description.innerHTML = data.descriptions[i];
        video_info.appendChild(video_description);

        video_container.appendChild(video_thumbnail);
        video_container.appendChild(video_info);

        current_video.appendChild(video_container);
        current_video_visibility.innerHTML = "Public";
        current_video_restrictions.innerHTML = "None";

        current_video_date.innerHTML = data.dates[i];
        current_video_views.innerHTML = data.views[i];
        current_video_comments.innerHTML = "comments";
        current_video_likes.innerHTML = data.likes[i];
      }
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
      // Clearing section before any new query
      const dynamic = document.getElementById("dynamic");
      dynamic.innerHTML = "";

      // Creating new table with headers
      const table = document.createElement("table");
      const headers = table.insertRow(0);
      const video = headers.insertCell(-1);
      const visibility = headers.insertCell(-1);
      const restrictions = headers.insertCell(-1);
      const upload_date = headers.insertCell(-1);
      const views = headers.insertCell(-1);
      const comments = headers.insertCell(-1);
      const likes = headers.insertCell(-1);

      // Setting header names
      video.innerHTML = "<th>Video</th>";
      visibility.innerHTML = "<th>visibility</th>";
      restrictions.innerHTML = "<th>restrictions</th>";
      upload_date.innerHTML = "<th>upload_date</th>";
      views.innerHTML = "<th>views</th>";
      comments.innerHTML = "<th>comments</th>";
      likes.innerHTML = "<th>likes</th>";
      dynamic.appendChild(table);

      // Adding data to table
      for (let i = 0; i < data.titles.length; i++) {
        // Creating new row
        video_row = table.insertRow(-1);
        const current_video = video_row.insertCell(-1);
        const current_video_visibility = video_row.insertCell(-1);
        const current_video_restrictions = video_row.insertCell(-1);
        const current_video_date = video_row.insertCell(-1);
        const current_video_views = video_row.insertCell(-1);
        const current_video_comments = video_row.insertCell(-1);
        const current_video_likes = video_row.insertCell(-1);

        // Creating tags and elements to store data for a video
        const video_container = document.createElement("section");
        video_container.setAttribute("class", "video-container");

        const video_thumbnail = document.createElement("img");
        video_thumbnail.setAttribute("src", data.thumbnails[i]);
        video_thumbnail.setAttribute("alt", data.thumbnails[i]);
        video_thumbnail.setAttribute("width", "120");
        video_thumbnail.setAttribute("height", "68");

        const video_info = document.createElement("div");
        video_info.setAttribute("class", "video-info");

        const video_title = document.createElement("p");
        video_title.setAttribute("class", "title");
        video_title.innerHTML = data.titles[i];
        video_info.appendChild(video_title);

        const video_description = document.createElement("p");
        video_description.setAttribute("class", "description");
        video_description.innerHTML = data.descriptions[i];
        video_info.appendChild(video_description);

        video_container.appendChild(video_thumbnail);
        video_container.appendChild(video_info);

        current_video.appendChild(video_container);
        current_video_visibility.innerHTML = "Public";
        current_video_restrictions.innerHTML = "None";

        current_video_date.innerHTML = data.dates[i];
        current_video_views.innerHTML = data.views[i];
        current_video_comments.innerHTML = "comments";
        current_video_likes.innerHTML = data.likes[i];
      }
    });
}
