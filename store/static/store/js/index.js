//window.onload = function() {
//  let modal = document.getElementById("myModal");
//  modal.style.display = "block";
//  let yesBtn = document.getElementById("yesBtn");
//  let noBtn = document.getElementById("noBtn");
//  yesBtn.onclick = function() {
//    modal.style.display = "none";
//  };
//  noBtn.onclick = function() {
//    /*window.location.href = "https://example.com";*/
//		let restrict = document.querySelector('.restrict');
//		restrict.style.display = 'block';
//  };
//};

window.onload = function() {
	let modal = $('#myModal');
	modal.css('display', 'block');

	let yesBtn = $('#yesBtn');
	let noBtn = $('#noBtn');

	yesBtn.click(function() {
		modal.css('display', 'none');	
	});

	noBtn.click(function() {
		let restrict = $('.restrict');
		restrict.css('display', 'block');
	});
};

let currentTime = new Date();
let hours = currentTime.getHours();
let minutes = currentTime.getMinutes();
let seconds = currentTime.getHours();

let time = `${hours}:${minutes}`;
