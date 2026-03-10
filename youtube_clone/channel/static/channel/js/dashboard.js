function displayVideoUploader() {
  const uploader = document.getElementById("video-uploader-container");
  uploader.style.display = "block";
}





window.onload = function () {
  const dialog = document.querySelector("dialog");
  const showButton = document.querySelector("dialog + button");
  const closeButton = document.getElementById("close-dialog-btn");

  // TODO: Figure out how dialogs work. Try to make the close button close the dialog
  // "Show the dialog" button opens the dialog modally
  showButton.addEventListener("click", () => {
    dialog.showModal();
  });

  // "Close" button closes the dialog
  closeButton.addEventListener("click", () => {
    dialog.close();
  });

}