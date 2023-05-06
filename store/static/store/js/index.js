window.onload = function() {
  let modal = document.getElementById("myModal");
  modal.style.display = "block";
  let yesBtn = document.getElementById("yesBtn");
  let noBtn = document.getElementById("noBtn");
  yesBtn.onclick = function() {
    modal.style.display = "none";
  };
  noBtn.onclick = function() {
    /*window.location.href = "https://example.com";*/
		let restrict = document.querySelector('.restrict');
		restrict.style.display = 'block';
  };
};
